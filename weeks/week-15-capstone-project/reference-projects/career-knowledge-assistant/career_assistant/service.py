"""Application logic shared by the CLI, optional API and dashboard."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from career_assistant.storage import database


def _required(text: str, label: str) -> str:
    value = text.strip()
    if not value:
        raise ValueError(f"{label} không được rỗng")
    if len(value) > 2000:
        raise ValueError(f"{label} quá dài")
    return value


def _tags(raw: str) -> list[str]:
    return sorted({tag.strip().lower() for tag in raw.split(",") if tag.strip()})


def add_note(
    db_path: str | Path, title: str, body: str, tags: str = ""
) -> int:
    """Create a knowledge note; return its database ID."""
    title = _required(title, "Tiêu đề")
    body = _required(body, "Nội dung")
    with database(db_path) as connection:
        cursor = connection.execute(
            "INSERT INTO notes(title, body, tags_json, created_at) VALUES (?, ?, ?, ?)",
            (
                title,
                body,
                json.dumps(_tags(tags), ensure_ascii=False),
                datetime.now(timezone.utc).isoformat(),
            ),
        )
        return int(cursor.lastrowid)


def list_notes(db_path: str | Path) -> list[dict]:
    """Return notes with parsed tags, newest ID first."""
    with database(db_path) as connection:
        rows = connection.execute(
            "SELECT id, title, body, tags_json, created_at FROM notes ORDER BY id DESC"
        ).fetchall()
    return [
        {
            "id": row["id"],
            "title": row["title"],
            "body": row["body"],
            "tags": json.loads(row["tags_json"]),
            "created_at": row["created_at"],
        }
        for row in rows
    ]


def search_notes(db_path: str | Path, query: str) -> list[dict]:
    """Case-insensitive literal search over title/body/tags."""
    needle = _required(query, "Từ khóa").casefold()
    return [
        note
        for note in list_notes(db_path)
        if needle in (
            note["title"] + " " + note["body"] + " " + " ".join(note["tags"])
        ).casefold()
    ]


def delete_note(db_path: str | Path, note_id: int) -> bool:
    """Delete a note by ID; false when it never existed."""
    with database(db_path) as connection:
        result = connection.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        return result.rowcount > 0


def set_skill(
    db_path: str | Path, name: str, level: int, comment: str = ""
) -> None:
    """Create/update an assessed skill with level 0..5."""
    name = _required(name, "Tên kỹ năng")
    if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 5:
        raise ValueError("Mức kỹ năng phải là số nguyên từ 0 đến 5")
    with database(db_path) as connection:
        connection.execute(
            """INSERT INTO skills(name, level, comment) VALUES (?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                level = excluded.level, comment = excluded.comment""",
            (name, level, comment.strip()),
        )


def list_skills(db_path: str | Path) -> list[dict]:
    """Return current skill profile ordered by name."""
    with database(db_path) as connection:
        return [
            dict(row)
            for row in connection.execute(
                "SELECT name, level, comment FROM skills ORDER BY name"
            ).fetchall()
        ]


def summary(db_path: str | Path) -> dict:
    """Simple dashboard data; no external AI model involved."""
    notes = list_notes(db_path)
    skills = list_skills(db_path)
    counts = Counter(tag for note in notes for tag in note["tags"])
    return {
        "note_count": len(notes),
        "skill_count": len(skills),
        "average_level": (
            round(sum(skill["level"] for skill in skills) / len(skills), 2)
            if skills
            else 0
        ),
        "popular_tags": counts.most_common(5),
    }


def export_json(db_path: str | Path, output_path: str | Path) -> Path:
    """Export a readable snapshot (not a backup of SQLite internals)."""
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "schema_version": 1,
        "notes": list_notes(db_path),
        "skills": list_skills(db_path),
    }
    target.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return target
