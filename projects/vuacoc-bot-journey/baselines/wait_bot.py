"""WaitBot: the smallest deterministic course-local baseline."""


def choose_action(state: dict[str, int]) -> str:
    """Always return the local ``wait`` action."""
    return "wait"
