"""Exercise 02: compose Bot with a replaceable strategy."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Delegate action selection to an injected strategy."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
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


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    for strategy in (defensive, balanced, aggressive):
        bot = Bot(strategy)
        print(f"{strategy.__name__}: {bot.choose_action(state)}")

    reverse_state = {"position": 3, "opponent_position": 4, "goal": 0}
    print(f"goal=0: {Bot(balanced).choose_action(reverse_state)}")
