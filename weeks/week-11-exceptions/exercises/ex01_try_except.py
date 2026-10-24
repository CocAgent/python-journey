"""Exercise 01: handle expected bad input without hiding programming bugs.

Implement safe_int so that it returns an integer for valid input and None when
the input cannot be parsed as an integer. Catch ValueError only.
"""


def safe_int(raw: str) -> int | None:
    """Convert raw to int; return None if raw is not a valid integer."""
    try:
        return int(raw)
    except ValueError:
        return None


def main() -> None:
    examples = ("42", "-7", "not-a-number", "")
    for raw in examples:
        value = safe_int(raw)
        if value is None:
            print(f"Invalid integer {raw!r}.")
        else:
            print(f"Parsed integer: {value}")

    # Small regression checks for valid, negative, and invalid input.
    assert safe_int("42") == 42
    assert safe_int("-7") == -7
    assert safe_int("not-a-number") is None
    assert safe_int("") is None
    print("Exercise 01 checks: PASS")


if __name__ == "__main__":
    main()
