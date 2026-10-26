"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    # TODO: raise ValueError for an action outside LOCAL_ACTIONS.
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"illegal local action: {action!r}")
    return action


print(validate_action("jump"))
