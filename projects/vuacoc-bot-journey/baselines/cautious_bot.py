"""CautiousBot: pause near an opponent, otherwise move forward."""


def choose_action(state: dict[str, int]) -> str:
    """Use one proximity condition before moving toward the local goal."""
    position = state["position"]
    opponent_position = state["opponent_position"]
    if abs(position - opponent_position) <= 1:
        return "wait"

    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
