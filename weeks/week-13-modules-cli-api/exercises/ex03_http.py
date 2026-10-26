"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Validate a successful fixture and reject a server-error status."""
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13
    print(data)

    try:
        parse_json_response(500, b'{"error": "server unavailable"}')
    except ValueError as error:
        print(f"Expected HTTP error: {error}")
    else:
        raise AssertionError("non-2xx HTTP status should raise ValueError")


if __name__ == "__main__":
    main()
