"""Bài 2 — Lời giải: Bot dùng composition để thay chiến lược."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    def __init__(self, strategy: Strategy) -> None:
        if not callable(strategy):
            raise TypeError("strategy phải là hàm có thể gọi")
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def _move_toward_goal(state: State) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
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
    # Bài mô hình hóa một chiều nên chiến lược này cũng đi thẳng về đích.
    return _move_toward_goal(state)
