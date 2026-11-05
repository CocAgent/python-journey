"""Biến course-local structured state thành một action."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Áp dụng ba rule dễ đọc trên teaching state."""
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


def explain(state: dict[str, int], action: str) -> str:
    """Giải thích action bằng data đã quan sát."""
    return (
        f"position={state.get('position')}, goal={state.get('goal')} "
        f"→ action={action}"
    )


def main() -> None:
    """Chạy normal, boundary và missing-optional-field cases."""
    states = [
        {"position": 1, "opponent_position": 3, "goal": 4},
        {"position": 4, "opponent_position": 2, "goal": 4},
        {"position": 3, "goal": 0},
    ]

    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    for state in states:
        action = choose_action(state)
        print(explain(state, action))
        print(f"legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
