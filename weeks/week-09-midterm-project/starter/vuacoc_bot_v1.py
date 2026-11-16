"""Starter for the course-local VuaCóc Bot V1 midterm track."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Return a safe action while the learner implements 2–4 rules."""
    # TODO: read position, goal and optional opponent_position.
    # TODO: handle the goal boundary before movement rules.
    # TODO: return only left, right or wait.
    return "wait"


def explain_action(state: dict[str, int], action: str) -> str:
    """Explain which observed state values led to an action."""
    # TODO: improve this explanation with the fields your rules use.
    return f"state={state}, action={action}"


def main() -> None:
    """Smoke-test one structured course-local state."""
    state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    action = choose_action(state)
    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(explain_action(state, action))
    print(f"legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
