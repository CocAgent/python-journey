"""Lab 01: catch the expected ValueError, not every exception."""


def safe_int(raw: str) -> int | None:
    """Return parsed integer; invalid numeric text -> None.

    Wrong program input type (e.g. None) should still raise TypeError.
    """
    # TODO: try int(raw), except ValueError: return None.
    # Do NOT add except Exception or bare except.
    raise NotImplementedError("Hoàn thiện safe_int")


if __name__ == "__main__":
    print("Giải TODO và kiểm safe_int('42'), safe_int('bad').")
