"""Official solution 04: a structured-state local bot heuristic."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Choose a legal local action with three explainable rules."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    opponent = state.get("opponent_position")

    if position == goal:
        return "wait"
    if opponent is not None and abs(position - opponent) <= 1:
        return "wait"
    if position < goal:
        return "right"
    return "left"


if __name__ == "__main__":
    teaching_state = {"position": 0, "opponent_position": 4, "goal": 4}
    print(choose_action(teaching_state))
