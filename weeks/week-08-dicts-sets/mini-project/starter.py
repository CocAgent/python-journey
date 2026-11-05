"""Starter for the Week 08 Decision Dashboard."""

REQUIRED_FIELDS = {"position", "goal"}
LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_state(state: dict[str, object]) -> bool:
    """Return whether all required fields exist."""
    # TODO: compare REQUIRED_FIELDS with the dictionary keys.
    return False


def summarize_state(state: dict[str, object]) -> str:
    """Return a short learner-readable summary."""
    # TODO: use required values and .get() for an optional value.
    return "Chưa có summary"


def recommend_action(state: dict[str, object]) -> str:
    """Return one recommendation from 2–4 explainable rules."""
    # TODO: return a value from LOCAL_ACTIONS.
    return "wait"


def main() -> None:
    """Run the dashboard on a small nested teaching model."""
    dashboard = {
        "state": {
            "position": 1,
            "opponent_position": 3,
            "goal": 4,
        },
        "tags": {"course-local", "week-08"},
    }
    state = dashboard["state"]
    if not isinstance(state, dict):
        print("State không hợp lệ")
        return

    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(f"valid={validate_state(state)}")
    print(summarize_state(state))
    action = recommend_action(state)
    print(f"action={action}, legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
