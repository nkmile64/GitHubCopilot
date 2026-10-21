import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""


def _db_path() -> Path:
    # Read per call so tests can override via the environment.
    return Path(os.environ.get("URL_SHORT_DB", "data/urls.db"))


@contextmanager
def connect():
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    try:
        conn.execute(SCHEMA)
        with conn:
            yield conn
    finally:
        conn.close()


def get_or_create(url: str) -> int:
    with connect() as conn:
        conn.execute("INSERT OR IGNORE INTO urls (url) VALUES (?)", (url,))
        row = conn.execute("SELECT id FROM urls WHERE url = ?", (url,)).fetchone()
        return row[0]


def get_by_id(id_: int) -> str | None:
    with connect() as conn:
        row = conn.execute("SELECT url FROM urls WHERE id = ?", (id_,)).fetchone()
        return row[0] if row else None
