"""Official solution for defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"illegal local action: {action!r}")
    return action
