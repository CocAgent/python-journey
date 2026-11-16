"""Ví dụ 6: HTTP status + JSON + dữ liệu bài học là BA tầng kiểm.

Không gọi API. Chạy từ week root:
    python -m examples.ex06_http_error_cases
"""

from __future__ import annotations

from bot_course.http_foundation import parse_json_response


def read_lesson(status: int, body: bytes) -> int:
    """Trả lesson dương; lỗi của status/JSON khác lỗi dữ liệu nghiệp vụ."""
    data = parse_json_response(status, body)
    lesson = data.get("lesson")
    if isinstance(lesson, bool) or not isinstance(lesson, int) or lesson < 1:
        raise ValueError("JSON phải có lesson là số nguyên dương")
    return lesson


def main() -> None:
    cases = [
        ("200 + JSON hợp lệ", 200, b'{"lesson": 13}'),
        ("503 + JSON hợp lệ", 503, b'{"lesson": 13}'),
        ("200 + JSON sai", 200, b"not-json"),
        ("200 + thiếu lesson", 200, b"{}"),
        ("200 + lesson sai", 200, b'{"lesson": -1}'),
    ]
    for title, status, body in cases:
        try:
            result = read_lesson(status, body)
        except ValueError as error:
            print(f"{title} => LỖI: {error}")
        else:
            print(f"{title} => OK: lesson={result}")


if __name__ == "__main__":
    main()
