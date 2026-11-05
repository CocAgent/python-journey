"""Reference: raise specific input errors with evidence.

COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT.
"""

ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    if type(action) is not str or action not in ACTIONS:
        raise ValueError(f"Illegal local action: {action!r}")
    return action


if __name__ == "__main__":
    print(validate_action("wait"))
