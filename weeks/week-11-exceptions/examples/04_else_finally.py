"""Use else for the success path and finally for guaranteed cleanup work."""


def parse_score(raw: str, audit_log: list[str]) -> int | None:
    """Return a valid score and always record that parsing was attempted."""
    try:
        score = int(raw)
    except ValueError:
        return None
    else:
        return score if 0 <= score <= 10 else None
    finally:
        audit_log.append(f"parsed={raw!r}")


events: list[str] = []
print(parse_score("8", events))
print(parse_score("eight", events))
print(events)
