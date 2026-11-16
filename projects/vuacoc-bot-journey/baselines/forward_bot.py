"""ForwardBot: move toward the course-local goal when possible."""


def choose_action(state: dict[str, int]) -> str:
    """Move one step toward ``goal``, or wait at the goal."""
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
