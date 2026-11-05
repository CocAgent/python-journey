"""Example 07: try/except/else/finally and observable event order."""


def parse_action(raw: str, audit: list[str]) -> str | None:
    """Try only conversion; else only success; finally always audit."""
    try:
        number = int(raw)
    except ValueError:
        audit.append("except")
        return None
    else:
        audit.append("else")
        return "right" if number > 0 else "wait"
    finally:
        audit.append("finally")


def main() -> None:
    events: list[str] = []
    print(f"Success action: {parse_action('2', events)}")
    print(f"Success events: {events}")
    events.clear()
    print(f"Invalid action: {parse_action('bad', events)!r}")
    print(f"Invalid events: {events}")
    try:
        parse_action(None, events)  # type: ignore[arg-type]
    except TypeError:
        print("Programming type error: TypeError propagated")
    print(f"Events after TypeError: {events}")


if __name__ == "__main__":
    main()
