"""Student decision policy for the course-local Line Arena."""


def choose_action(state: dict[str, int]) -> str:
    """Move toward this bot goal using the local state contract.

    Invalid or incomplete state returns the safe local action ``wait``.
    """
    position = state.get("position")
    goal = state.get("goal")
    if (not isinstance(position, int) or isinstance(position, bool)
            or not isinstance(goal, int) or isinstance(goal, bool)):
        return "wait"
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def main() -> None:
    """Run a small example of the decision policy."""
    state = {"turn": 1, "max_turns": 6, "position": 0,
             "opponent_position": 4, "goal": 4,
             "min_position": 0, "max_position": 4}
    print(choose_action(state))


if __name__ == "__main__":
    main()
