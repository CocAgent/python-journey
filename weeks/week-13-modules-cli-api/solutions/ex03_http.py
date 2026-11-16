"""Lời giải 03 — xử lý dữ liệu HTTP giả lập và lỗi rõ ràng."""

from bot_course.http_foundation import parse_json_response

FAKE_BODY = b'{"lesson": 13}'


def main() -> None:
    data = parse_json_response(200, FAKE_BODY)
    assert data["lesson"] == 13
    print("Lesson:", data["lesson"])
    try:
        parse_json_response(500, b"{}")
    except ValueError as error:
        print("Đã bắt lỗi:", error)


if __name__ == "__main__":
    main()
