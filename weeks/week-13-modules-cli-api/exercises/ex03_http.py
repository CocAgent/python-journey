"""Bài 03 — đọc HTTP response GIẢ, không gọi urlopen/network."""

from bot_course.http_foundation import parse_json_response

FIXTURE = b'{"lesson": 13}'


def main() -> None:
    """TODO: assert lesson==13 và xử lý status 500 bằng except ValueError."""
    # TODO 1: data = parse_json_response(200, FIXTURE)
    # TODO 2: print("Lesson:", data["lesson"])
    # TODO 3: thử status 500 và bắt ValueError, không in success khi lỗi.
    # Positive control: starter vẫn chạy được và có output cho người học quan sát.
    # TODO: sau đó cải tiến thành assert + xử lý lỗi 500 theo yêu cầu.
    data = parse_json_response(200, FIXTURE)
    print(data)  # Giữ bằng chứng {\'lesson\': 13} của bài kiểm tra có sẵn.
    assert data["lesson"] == 13


if __name__ == "__main__":
    main()
