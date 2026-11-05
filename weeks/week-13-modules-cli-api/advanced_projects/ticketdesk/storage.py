"""Cơ sở lưu trữ JSON nhỏ trên máy học viên.

Với bài nhiều người dùng, cần database, locking và transaction thực tế.
"""

from __future__ import annotations

import json
from pathlib import Path

from .service import validate_tickets


def load_tickets(path: Path) -> list[dict]:
    """File chưa tồn tại coi là dữ liệu rỗng; file lỗi thì báo lỗi."""
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("File JSON không đọc được hoặc sai định dạng") from error
    return validate_tickets(data)


def save_tickets(path: Path, items: list[dict]) -> None:
    """Không ghi dữ liệu chưa validate. Chỉ dùng file local do người học chọn."""
    clean = validate_tickets(items)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(clean, ensure_ascii=False, indent=2) + "\n"
    path.write_text(payload, encoding="utf-8")
