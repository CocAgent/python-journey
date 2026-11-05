"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect successful and unsuccessful offline response fixtures."""
    response = parse_json_response(200, fixture)
    assert response["lesson"] == 13
    print(f"success: {response}")

    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print(f"expected error: {error}")
    else:
        raise AssertionError("HTTP 500 should raise ValueError")


if __name__ == "__main__":
    main()
