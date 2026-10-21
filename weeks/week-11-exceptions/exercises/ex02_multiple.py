"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"Invalid action: {action}")
    return action

print(validate_action("left"))
print(validate_action("right"))
print(validate_action("wait"))
print(validate_action("son"))