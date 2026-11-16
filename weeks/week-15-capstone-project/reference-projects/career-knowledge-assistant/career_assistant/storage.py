"""SQLite infrastructure: no network, no ORM, no API keys."""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

SCHEMA = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    tags_json TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS skills (
    name TEXT PRIMARY KEY COLLATE NOCASE,
    level INTEGER NOT NULL CHECK (level BETWEEN 0 AND 5),
    comment TEXT NOT NULL DEFAULT ''
);
"""


@contextmanager
def database(path: str | Path) -> Iterator[sqlite3.Connection]:
    """Open one short transaction and always close the connection."""
    db_path = Path(path).expanduser()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        connection.executescript(SCHEMA)
        with connection:
            yield connection
    finally:
        connection.close()
