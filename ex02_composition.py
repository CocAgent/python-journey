"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def _move_toward_goal(state: dict[str, int]) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return _move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    return _move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    return _move_toward_goal(state)
