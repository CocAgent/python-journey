"""Ví dụ 3: HTTP GET metadata + status + JSON response giả lập, không có mạng."""

from bot_course.http_foundation import build_get_request, parse_json_response


def main() -> None:
    request = build_get_request("https://example.invalid/learning")
    # Request() chưa kết nối. Chúng ta tự tạo body giả lập:
    fake_body = b'{"topic": "http", "network_used": false}'
    print("Method:", request.get_method())
    print("URL demo:", request.full_url)
    print("Dữ liệu đã parse:", parse_json_response(200, fake_body))

    try:
        parse_json_response(503, b'{"message":"temporarily unavailable"}')
    except ValueError as error:
        print("Đã từ chối lỗi HTTP:", error)


if __name__ == "__main__":
    main()
