"""Bài 03 — đọc HTTP response GIẢ, không gọi urlopen/network."""

from bot_course.http_foundation import parse_json_response

FIXTURE = b'{"lesson": 13}'


def main() -> None:
    """TODO: assert lesson==13 và xử lý status 500 bằng except ValueError."""
    # TODO 1: data = parse_json_response(200, FIXTURE)
    # TODO 2: print("Lesson:", data["lesson"])
    # TODO 3: thử status 500 và bắt ValueError, không in success khi lỗi.
    print("TODO 03: có thể gọi parse_json_response(200, FIXTURE)")
    # Dòng dưới minh họa hàm đang có (khi hoàn thành có thể thay bằng TODO).
    assert parse_json_response(200, FIXTURE)["lesson"] == 13


if __name__ == "__main__":
    main()
