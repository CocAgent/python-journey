"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect successful and unsuccessful offline response fixtures."""
    response = parse_json_response(200, fixture)
    assert response["lesson"] == 13
    print(response)

    try:
        parse_json_response(500, b'{"error": "server error"}')
    except ValueError as error:
        print(f"Handled unsuccessful response: {error}")
    else:
        raise AssertionError("HTTP 500 response was accepted")


if __name__ == "__main__":
    main()
