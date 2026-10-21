"""Exercise 04: separate success handling from guaranteed final work."""


def parse_score(raw: str, audit_log: list[str]) -> int | None:
    """Parse a score from 0 to 10 and always append one audit event."""
    try:
        score = int(raw)
    except ValueError:
        return None
    else:
        return score if 0 <= score <= 10 else None
    finally:
        audit_log.append(f"parsed={raw!r}")


if __name__ == "__main__":
    events: list[str] = []
    for raw in ("8", "eight", "11"):
        print(parse_score(raw, events))
    print(events)
