"""Reference 03 — Logic bug regression, narrow exceptions, finally audit."""


def distance(start: int, end: int) -> int:
    """Không dựa vào hướng: khoảng cách luôn không âm."""
    if (
        type(start) is not int
        or type(end) is not int
        or not 0 <= start <= 10
        or not 0 <= end <= 10
    ):
        raise ValueError("Vị trí không hợp lệ")
    return abs(end - start)


def parse_score(raw: str, audit: list[str]) -> int | None:
    """ValueError is expected bad input; TypeError is not swallowed."""
    try:
        value = int(raw)
    except ValueError:
        audit.append("invalid")
        return None
    else:
        if not 0 <= value <= 10:
            audit.append("out_of_range")
            return None
        audit.append("accepted")
        return value
    finally:
        audit.append(f"attempt:{raw!r}")


if __name__ == "__main__":
    print(distance(4, 1))
