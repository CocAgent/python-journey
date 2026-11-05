"""Mô phỏng HTTP trả về (status, JSON bytes) — KHÔNG là web server.

Dùng để nối khái niệm service → response và kiểm lỗi HTTP offline.
"""

from __future__ import annotations

import json
from pathlib import Path

from . import service, storage


def make_get_response(path: Path, ticket_id: int) -> tuple[int, bytes]:
    """Đây chỉ là hàm Python, không mở socket hoặc gọi API."""
    items = storage.load_tickets(path)
    result = service.find_ticket(items, ticket_id)
    if result is None:
        status, payload = 404, {"error": "ticket not found"}
    else:
        status, payload = 200, result
    return status, json.dumps(payload, ensure_ascii=False).encode("utf-8")


def main() -> None:
    """Một demo độc lập với file thật: dùng dữ liệu mẫu tĩnh."""
    ticket = {"id": 1, "title": "Học module", "priority": "normal", "status": "open"}
    for ticket_id in (1, 99):
        found = service.find_ticket([ticket], ticket_id)
        status = 200 if found else 404
        body = json.dumps(found if found else {"error": "not found"}, ensure_ascii=False)
        print(f"HTTP giả lập {status}: {body}")


if __name__ == "__main__":
    main()
