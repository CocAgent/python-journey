"""Exercise 01: expected bad input."""


def safe_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


if __name__ == "__main__":
    raw_turn = "not-a-number"
    result = safe_int(raw_turn)
    print(f"Không thể chuyển {raw_turn!r} thành số nguyên." if result is None else result)
