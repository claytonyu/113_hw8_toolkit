"""A tiny JSON API for saving creative ideas in SQLite."""

import json
import os
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

DB_PATH = Path(os.environ.get("IDEA_DB", Path(__file__).with_name("ideas.db")))


def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize():
    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS ideas (id INTEGER PRIMARY KEY, title TEXT NOT NULL, note TEXT NOT NULL DEFAULT '')")


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if urlparse(self.path).path != "/ideas":
            return self.respond(404, {"error": "Not found"})
        with connect() as db:
            ideas = [dict(row) for row in db.execute("SELECT * FROM ideas ORDER BY id DESC")]
        self.respond(200, ideas)

    def do_POST(self):
        if urlparse(self.path).path != "/ideas":
            return self.respond(404, {"error": "Not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 10000:
                raise ValueError()
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError()
            title, note = data.get("title"), data.get("note", "")
            if not isinstance(title, str) or not title.strip() or len(title.strip()) > 100:
                raise ValueError()
            if not isinstance(note, str) or len(note) > 1000:
                raise ValueError()
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            return self.respond(400, {"error": "Provide a title (1–100 characters) and optional note (up to 1000 characters)."})
        with connect() as db:
            cursor = db.execute("INSERT INTO ideas (title, note) VALUES (?, ?)", (title.strip(), note.strip()))
            idea = dict(db.execute("SELECT * FROM ideas WHERE id = ?", (cursor.lastrowid,)).fetchone())
        self.respond(201, idea)

    def do_DELETE(self):
        parts = urlparse(self.path).path.strip("/").split("/")
        if len(parts) != 2 or parts[0] != "ideas" or not parts[1].isascii() or not parts[1].isdigit() or len(parts[1]) > 18:
            return self.respond(404, {"error": "Not found"})
        with connect() as db:
            cursor = db.execute("DELETE FROM ideas WHERE id = ?", (int(parts[1]),))
        if not cursor.rowcount:
            return self.respond(404, {"error": "Idea not found"})
        self.respond(200, {"deleted": True})


if __name__ == "__main__":
    initialize()
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Idea API running on http://127.0.0.1:{port}", flush=True)
    server.serve_forever()
