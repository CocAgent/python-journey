"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"illegal local action: {action!r}")
    return action


if __name__ == "__main__":
    print(validate_action("wait"))
    try:
        validate_action("teleport")
    except ValueError as error:
        print(error)
