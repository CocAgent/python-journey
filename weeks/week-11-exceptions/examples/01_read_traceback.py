"""A minimal failing input kept as debugging evidence."""


def parse_turn(raw_turn: str) -> int:
    return int(raw_turn)


try:
    parse_turn("three")
except ValueError as error:
    print(f"type={type(error).__name__}")
    print(f"message={error}")
