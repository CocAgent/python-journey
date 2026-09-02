"""Official solution for Exercise 04.

COURSE TEACHING MODEL — NOT VUACOC RUNTIME CONTRACT.
"""


def choose_action(state: str) -> str:
    """Return a deterministic teaching action for ``state``."""
    if state == "danger":
        return "defend"
    if state == "opportunity":
        return "advance"
    return "wait"


def main() -> None:
    """Print representative decisions."""
    for state in ("danger", "opportunity", "neutral", ""):
        print(f"{state!r} -> {choose_action(state)!r}")


if __name__ == "__main__":
    main()
