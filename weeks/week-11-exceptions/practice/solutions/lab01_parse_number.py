"""Reference: only catch expected numeric conversion errors."""


def safe_int(raw: str) -> int | None:
    try:
        return int(raw)
    except ValueError:
        return None


if __name__ == "__main__":
    print(safe_int("42"))
