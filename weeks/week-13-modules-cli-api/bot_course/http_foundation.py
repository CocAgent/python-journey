"""Offline HTTP request/response foundations using the standard library."""

import json
from urllib.request import Request


def build_get_request(url: str) -> Request:
    return Request(url, method="GET")


def parse_json_response(status: int, body: bytes) -> dict[str, object]:
    if not 200 <= status < 300:
        raise ValueError(f"unexpected HTTP status: {status}")
    data = json.loads(body.decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("expected a JSON object")
    return data
