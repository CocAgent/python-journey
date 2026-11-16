"""Reference Bot V1 using an explainable course-local heuristic."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Choose an action from position, goal and optional opponent position."""
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


def explain_action(state: dict[str, int], action: str) -> str:
    """Return a concise explanation using only observed local fields."""
    return (
        f"position={state.get('position')}, "
        f"opponent={state.get('opponent_position')}, "
        f"goal={state.get('goal')} -> {action}"
    )


if __name__ == "__main__":
    sample = {"position": 0, "opponent_position": 4, "goal": 4}
    decision = choose_action(sample)
    print(explain_action(sample, decision))
