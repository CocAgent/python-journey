"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    """Return a valid local action or raise ValueError."""
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"illegal local action: {action!r}")
    return action


print(validate_action("wait"))
