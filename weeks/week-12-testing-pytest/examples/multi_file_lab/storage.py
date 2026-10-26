"""Lưu và đọc đơn hàng dưới dạng JSON."""

import json
from pathlib import Path


def save_order(path: Path, order: dict[str, int]) -> None:
    """Ghi dữ liệu đơn hàng vào tệp JSON với mã hóa UTF-8."""
    path.write_text(json.dumps(order, ensure_ascii=False), encoding="utf-8")


def load_order(path: Path) -> dict[str, int]:
    """Đọc dữ liệu; thông báo rõ khi tệp JSON có nội dung sai."""
    content = path.read_text(encoding="utf-8")
    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError("JSON không hợp lệ") from exc
