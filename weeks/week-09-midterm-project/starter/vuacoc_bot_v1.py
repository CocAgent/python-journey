"""Course-local VuaCóc Bot V1 teaching model; not a production contract."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Choose a legal action from structured course-local state."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    min_position = state.get("min_position", 0)
    max_position = state.get("max_position", goal)
    opponent_position = state.get("opponent_position")

    # Rule 1: do not move after reaching the goal or beyond the board.
    if position == goal:
        return "wait"
    if position < min_position or position > max_position:
        return "wait"

    # Rule 2: avoid moving into a position occupied by the opponent.
    next_position = position + 1 if position < goal else position - 1
    if opponent_position is not None and next_position == opponent_position:
        return "wait"

    # Rule 3: otherwise move one step toward the goal.
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def explain_action(state: dict[str, int], action: str) -> str:
    """Explain the chosen action using observed state fields."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    opponent = state.get("opponent_position")
    return (
        f"position={position}, goal={goal}, opponent_position={opponent}; "
        f"chosen action={action}"
    )


def main() -> None:
    """Smoke-test representative normal and boundary states."""
    states = [
        {"position": 0, "goal": 4, "opponent_position": 4, "min_position": 0, "max_position": 4},
        {"position": 4, "goal": 4, "opponent_position": 0, "min_position": 0, "max_position": 4},
        {"position": 2, "goal": 4, "opponent_position": 3, "min_position": 0, "max_position": 4},
    ]
    print("COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT")
    for state in states:
        action = choose_action(state)
        print(explain_action(state, action))
        print(f"legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
