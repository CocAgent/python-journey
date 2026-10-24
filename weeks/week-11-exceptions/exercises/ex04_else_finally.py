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
        # Record every attempt, whether parsing succeeds or fails.
        audit_log.append(f"parsed={raw!r}")


def main() -> None:
    events: list[str] = []

    assert parse_score("8", events) == 8
    assert parse_score("bad", events) is None
    assert parse_score("11", events) is None
    assert parse_score("-1", events) is None
    assert events == [
        "parsed='8'",
        "parsed='bad'",
        "parsed='11'",
        "parsed='-1'",
    ]

    print("Parsed score:", parse_score("5", events))
    print("Audit log:", events)
    print("Exercise 04 checks: PASS")


if __name__ == "__main__":
    main()
