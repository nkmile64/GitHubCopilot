from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, field_validator

from . import base62, db

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
MAX_URL_LENGTH = 2048
MAX_CODE_LENGTH = 11  # 62**11 exceeds SQLite's 64-bit integer range
MAX_SQLITE_INT = 2**63 - 1

app = FastAPI(title="URL Shortener")


class ShortenRequest(BaseModel):
    url: str

    @field_validator("url")
    @classmethod
    def must_be_http_url(cls, v: str) -> str:
        v = v.strip()
        parsed = urlparse(v)
        if len(v) > MAX_URL_LENGTH or parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise ValueError("must be an absolute http(s) URL")
        return v


def _lookup(code: str) -> str | None:
    if not code or len(code) > MAX_CODE_LENGTH:
        return None
    try:
        id_ = base62.decode(code)
    except ValueError:
        return None
    if id_ > MAX_SQLITE_INT:
        return None
    return db.get_by_id(id_)


@app.post("/api/shorten")
def shorten(body: ShortenRequest, request: Request):
    code = base62.encode(db.get_or_create(body.url))
    return {"code": code, "short_url": f"{request.base_url}{code}"}


@app.get("/api/resolve")
def resolve(short: str):
    segments = [s for s in urlparse(short.strip()).path.split("/") if s]
    if not segments:
        raise HTTPException(400, "Provide a short URL or code")
    url = _lookup(segments[-1])
    if url is None:
        raise HTTPException(404, "Short URL not found")
    return {"url": url}


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# Must stay last so it doesn't shadow other routes.
@app.get("/{code}")
def redirect(code: str):
    url = _lookup(code)
    if url is None:
        raise HTTPException(404, "Short URL not found")
    return RedirectResponse(url, status_code=302)
