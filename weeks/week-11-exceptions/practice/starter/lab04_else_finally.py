"""Reference: success in else, guaranteed auditing in finally."""


def valid_score(raw: str, audit: list[str]) -> int | None:
    try:
        value = int(raw)
    except ValueError:
        audit.append("invalid")
        return None
    else:
        audit.append("converted")
        return value if 0 <= value <= 10 else None
    finally:
        audit.append(f"attempt:{raw!r}")


if __name__ == "__main__":
    events: list[str] = []
    print(valid_score("8", events), events)
