"""Starter Student Bot for the course-local Line Arena."""


def choose_action(state: dict[str, int]) -> str:
    """Return a safe local action while the learner adds decision rules."""
    # TODO W07: Inspect simple state values and return left, right, or wait.
    # TODO W08: Explain how structured state changes the decision.
    return "wait"


def main() -> None:
    """Show that the starter is syntactically valid and runnable."""
    teaching_state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    print(choose_action(teaching_state))


if __name__ == "__main__":
    main()
