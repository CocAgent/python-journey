"""Reference 04 — structured state and deterministic heuristic.

COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT.
"""


ACTIONS = {"left", "right", "wait"}


def validate_state(state: dict[str, object]) -> bool:
    """Validate mandatory keys and optional opponent, each within 0..4."""
    if not isinstance(state, dict):
        return False
    for key in ("position", "goal"):
        if key not in state or type(state[key]) is not int or not 0 <= state[key] <= 4:
            return False
    if "opponent_position" in state:
        opponent = state["opponent_position"]
        if type(opponent) is not int or not 0 <= opponent <= 4:
            return False
    return True


def choose_action(state: dict[str, object]) -> str:
    """Legal fallback for invalid data is wait; explanation distinguishes invalid."""
    if not validate_state(state):
        return "wait"
    position = state["position"]
    goal = state["goal"]
    opponent = state.get("opponent_position")
    if position == goal:
        return "wait"
    if opponent is not None and abs(position - opponent) <= 1:
        return "wait"
    if position < goal:
        return "right"
    return "left"


def explain_decision(state: dict[str, object]) -> str:
    """Use a separate validation status to avoid claiming invalid state is fine."""
    if not validate_state(state):
        return "State không hợp lệ"
    action = choose_action(state)
    return f"position={state['position']}, goal={state['goal']}, action={action}"


if __name__ == "__main__":
    print(explain_decision({"position": 1, "goal": 4, "opponent_position": 3}))
