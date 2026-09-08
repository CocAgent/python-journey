"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect a successful offline response fixture."""
    # TODO: parse status 200 và assert lesson == 13.
    # TODO: quan sát ValueError với status 500.
    print(parse_json_response(200, fixture))


if __name__ == "__main__":
    main()
