"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    def __init__(self, strategy: Strategy) -> None:
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
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return _move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    return _move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    return _move_toward_goal(state)
