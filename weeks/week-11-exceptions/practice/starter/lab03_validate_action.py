"""Lab 03: raise helpful ValueError, do not silently return 'wait'.

COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT.
"""

ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    """Return the legal action, or raise ValueError with bad value."""
    # TODO: if type(action) is not str or action not in ACTIONS:
    #           raise ValueError(...) include repr(action).
    # TODO: return action only when valid.
    raise NotImplementedError("Hoàn thiện validate_action")


if __name__ == "__main__":
    print("Giải TODO rồi thử validate_action('teleport').")
