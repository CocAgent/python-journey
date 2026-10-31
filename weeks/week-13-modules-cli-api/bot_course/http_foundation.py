"""Ví dụ HTTP GET/JSON chạy OFFLINE: chỉ xây Request, KHÔNG mở network."""

import json
from urllib.request import Request


def build_get_request(url: str) -> Request:
    """Tạo metadata của GET request; KHÔNG gửi request lên mạng."""
    if not isinstance(url, str) or not url.startswith("https://"):
        raise ValueError("ví dụ học tập chỉ nhận URL bắt đầu bằng https://")
    return Request(url, method="GET")


def parse_json_response(status: int, body: bytes) -> dict[str, object]:
    """Mô phỏng nhận HTTP status + body bytes, chỉ nhận JSON object cho demo."""
    if not isinstance(status, int) or isinstance(status, bool):
        raise ValueError("HTTP status phải là số nguyên")
    if not 200 <= status < 300:
        raise ValueError(f"HTTP không thành công, status={status}")
    if not isinstance(body, bytes):
        raise ValueError("HTTP body phải là bytes")
    try:
        parsed = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("HTTP body không phải JSON UTF-8 hợp lệ") from error
    if not isinstance(parsed, dict):
        raise ValueError("Ví dụ này yêu cầu JSON object (dict), không phải list")
    return parsed
