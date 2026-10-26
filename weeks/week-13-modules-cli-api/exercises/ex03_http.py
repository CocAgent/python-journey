"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect a successful offline response fixture."""
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13
    print(data)

    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print(error)
    else:
        raise AssertionError("A 500 response should raise ValueError")


if __name__ == "__main__":
    main()
