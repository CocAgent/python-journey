"""Official solution for try/except/else/finally flow."""


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
