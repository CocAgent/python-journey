"""Exercise 04: separate success handling from guaranteed final work."""


def parse_score(raw: str, audit_log: list[str]) -> int | None:
    """Parse a score from 0 to 10 and always append one audit event."""
    # TODO: chuyển raw trong try và chỉ bắt ValueError.
    # TODO: validate range 0..10 trong else.
    # TODO: append f"parsed={raw!r}" trong finally.
    raise NotImplementedError("Complete parse_score")


if __name__ == "__main__":
    events: list[str] = []
    print(parse_score("8", events))
    print(parse_score("eight", events))
    print(events)
