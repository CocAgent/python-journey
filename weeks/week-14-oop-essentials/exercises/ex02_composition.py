"""Exercise 02: composition with interchangeable strategies."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


def move_toward_goal(state: dict[str, int]) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    return move_toward_goal(state)


class Bot:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


if __name__ == "__main__":
    state = {"position": 3, "opponent_position": 4, "goal": 0}
    for strategy in (defensive, balanced, aggressive):
        print(strategy.__name__, Bot(strategy).choose_action(state))
