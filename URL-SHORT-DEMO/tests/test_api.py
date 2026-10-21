import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("URL_SHORT_DB", str(tmp_path / "test.db"))
    return TestClient(app)


def test_shorten_and_redirect(client):
    r = client.post("/api/shorten", json={"url": "https://example.com/a?b=1"})
    assert r.status_code == 200
    body = r.json()
    assert body["short_url"].endswith("/" + body["code"])

    r = client.get(f"/{body['code']}", follow_redirects=False)
    assert r.status_code == 302
    assert r.headers["location"] == "https://example.com/a?b=1"


def test_same_url_same_code(client):
    a = client.post("/api/shorten", json={"url": "https://example.com"}).json()
    b = client.post("/api/shorten", json={"url": "https://example.com"}).json()
    assert a["code"] == b["code"]


@pytest.mark.parametrize("bad", ["javascript:alert(1)", "ftp://x.com", "not a url", "https://", ""])
def test_rejects_invalid_urls(client, bad):
    assert client.post("/api/shorten", json={"url": bad}).status_code == 422


def test_resolve_full_url_and_bare_code(client):
    created = client.post("/api/shorten", json={"url": "https://example.com/x"}).json()
    for short in (created["short_url"], created["code"]):
        r = client.get("/api/resolve", params={"short": short})
        assert r.status_code == 200
        assert r.json() == {"url": "https://example.com/x"}


def test_unknown_and_invalid_codes(client):
    assert client.get("/api/resolve", params={"short": "zzzz"}).status_code == 404
    assert client.get("/api/resolve", params={"short": "a-b"}).status_code == 404
    assert client.get("/api/resolve", params={"short": ""}).status_code == 400
    assert client.get("/api/resolve", params={"short": "Z" * 30}).status_code == 404
    assert client.get("/zzzz", follow_redirects=False).status_code == 404


def test_index_served(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "URL Shortener" in r.text
