"""Nghiệp vụ thuần Python: không phụ thuộc CLI, disk hay mạng.

Mỗi hàm nhận danh sách ticket và trả danh sách mới, giúp test dễ hiểu.
"""

from __future__ import annotations

VALID_PRIORITIES = {"low", "normal", "high"}
VALID_STATUSES = {"open", "closed"}


def _validate_ticket(ticket: object) -> dict:
    """Kiểm schema để dữ liệu JSON không tự biến thành dữ liệu đáng tin."""
    if not isinstance(ticket, dict):
        raise ValueError("Mỗi ticket phải là object")
    ticket_id = ticket.get("id")
    if isinstance(ticket_id, bool) or not isinstance(ticket_id, int) or ticket_id < 1:
        raise ValueError("id phải là số nguyên dương")
    title = ticket.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("title không được rỗng")
    priority = ticket.get("priority")
    if not isinstance(priority, str) or priority not in VALID_PRIORITIES:
        raise ValueError("priority không hợp lệ")
    status = ticket.get("status")
    if not isinstance(status, str) or status not in VALID_STATUSES:
        raise ValueError("status không hợp lệ")
    return {
        "id": ticket_id,
        "title": title.strip(),
        "priority": ticket["priority"],
        "status": ticket["status"],
    }


def validate_tickets(items: object) -> list[dict]:
    """Kiểm mọi bản ghi và không cho ID trùng."""
    if not isinstance(items, list):
        raise ValueError("File JSON phải chứa danh sách ticket")
    clean = [_validate_ticket(item) for item in items]
    ids = [item["id"] for item in clean]
    if len(ids) != len(set(ids)):
        raise ValueError("Danh sách có ticket ID trùng")
    return clean


def add_ticket(items: list[dict], title: str, priority: str = "normal") -> list[dict]:
    """Thêm một yêu cầu; ID tự tăng, không sửa trực tiếp input."""
    clean = validate_tickets(items)
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Tiêu đề không được rỗng")
    if not isinstance(priority, str) or priority not in VALID_PRIORITIES:
        raise ValueError("Priority phải là low, normal hoặc high")
    new_id = max((item["id"] for item in clean), default=0) + 1
    return [*clean, {"id": new_id, "title": title.strip(), "priority": priority, "status": "open"}]


def find_ticket(items: list[dict], ticket_id: int) -> dict | None:
    """Tìm theo ID hoặc trả None nếu không tồn tại."""
    clean = validate_tickets(items)
    if isinstance(ticket_id, bool) or not isinstance(ticket_id, int) or ticket_id < 1:
        raise ValueError("ID phải là số nguyên dương")
    return next((item for item in clean if item["id"] == ticket_id), None)


def close_ticket(items: list[dict], ticket_id: int) -> list[dict]:
    """Chỉ đóng ticket open; lỗi phải rõ, không giả báo thành công."""
    clean = validate_tickets(items)
    current = find_ticket(clean, ticket_id)
    if current is None:
        raise ValueError(f"Không tìm thấy ticket #{ticket_id}")
    if current["status"] != "open":
        raise ValueError(f"Ticket #{ticket_id} đã đóng")
    return [
        {**item, "status": "closed"} if item["id"] == ticket_id else item
        for item in clean
    ]


def summarize(items: list[dict]) -> dict[str, int]:
    """Thống kê phản ánh dữ liệu thật, kể cả danh sách rỗng."""
    clean = validate_tickets(items)
    return {
        "total": len(clean),
        "open": sum(item["status"] == "open" for item in clean),
        "closed": sum(item["status"] == "closed" for item in clean),
    }
