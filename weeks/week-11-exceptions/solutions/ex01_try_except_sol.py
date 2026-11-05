"""Official solution for expected bad input."""


def safe_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None
