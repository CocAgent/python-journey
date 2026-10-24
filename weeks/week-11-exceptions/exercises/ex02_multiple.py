"""Exercise 02: defensive validation.

Reject actions outside the local action contract with a useful ValueError.
Do not silently replace an invalid action with a default.
"""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    """Return a legal local action or raise ValueError."""
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"illegal local action: {action!r}")
    return action


def main() -> None:
    # Valid actions pass through unchanged.
    for action in ("left", "right", "wait"):
        assert validate_action(action) == action

    # Invalid actions must fail loudly and mention the bad value.
    try:
        validate_action("teleport")
    except ValueError as error:
        assert "teleport" in str(error)
        print(f"Rejected invalid action: {error}")
    else:
        raise AssertionError("invalid action was accepted")

    print("Exercise 02 checks: PASS")


if __name__ == "__main__":
    main()
