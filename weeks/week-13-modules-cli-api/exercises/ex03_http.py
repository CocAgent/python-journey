"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Kiểm tra phản hồi JSON offline và HTTP status."""
    response = parse_json_response(200, fixture)
    assert response["lesson"] == 13
    print("HTTP 200:", response)
    print("Lesson:", response["lesson"])

    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print("HTTP 500 được xử lý:", error)
    else:
        raise AssertionError("HTTP 500 phải gây ra ValueError")


if __name__ == "__main__":
    main()
