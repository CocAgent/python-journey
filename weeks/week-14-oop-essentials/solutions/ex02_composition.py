"""Lời giải bài 2: Bot ủy nhiệm hành vi cho strategy."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    def __init__(self, strategy: Strategy) -> None:
        if not callable(strategy):
            raise TypeError("strategy phải là một hàm có thể gọi")
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def _move_toward_goal(state: State) -> str:
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return _move_toward_goal(state)


def balanced(state: State) -> str:
    return _move_toward_goal(state)


def aggressive(state: State) -> str:
    # Mô hình bài học chỉ có trục một chiều; hành vi đi đích giống balanced.
    return _move_toward_goal(state)
