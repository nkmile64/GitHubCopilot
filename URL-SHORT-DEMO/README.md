# URL Shortener

A small URL shortener built with FastAPI and SQLite, with a single-page web UI.

## Features

- Shorten any absolute `http`/`https` URL (max 2048 characters).
- Same URL always yields the same short code.
- Short codes are the row ID encoded in base62 (`0-9a-zA-Z`).
- Resolve a short URL back to its original without following the redirect.
- Visiting `/<code>` redirects (302) to the original URL.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Setup and run

```powershell
uv sync
uv run uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 for the web UI.

## API

| Method | Path                    | Description                                              |
| ------ | ----------------------- | -------------------------------------------------------- |
| POST   | `/api/shorten`          | Body `{"url": "https://..."}`. Returns `code`, `short_url`. |
| GET    | `/api/resolve?short=..` | Accepts a short URL or code. Returns `{"url": "..."}`.   |
| GET    | `/{code}`               | Redirects to the original URL, or 404 if unknown.        |

Example:

```powershell
curl -X POST http://127.0.0.1:8000/api/shorten -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
```

## Configuration

| Variable       | Default         | Description              |
| -------------- | --------------- | ------------------------ |
| `URL_SHORT_DB` | `data/urls.db`  | Path to the SQLite file. |

## Tests

```powershell
uv run pytest -q
```

## Project layout

```
app/
  base62.py   base62 encode/decode
  db.py       SQLite storage (get_or_create, get_by_id)
  main.py     FastAPI app and routes
static/       web UI (index.html, app.js, style.css)
tests/        API and base62 tests
```
