"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    # TODO: raise ValueError for an action outside LOCAL_ACTIONS.
    return action


print(validate_action("wait"))
