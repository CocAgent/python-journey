"""Mini-project: Strategy Composition.

A Bot receives a strategy through __init__ and uses that strategy
with the same game state.
"""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


def move_toward_goal(state: State) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    opponent = state.get("opponent_position")

    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"

    return move_toward_goal(state)


def balanced(state: State) -> str:
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    return move_toward_goal(state)


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def main() -> None:
    state: State = {
        "position": 1,
        "opponent_position": 4,
        "goal": 4,
    }

    bots = [
        ("Defensive", Bot(defensive)),
        ("Balanced", Bot(balanced)),
        ("Aggressive", Bot(aggressive)),
    ]

    print("=== STRATEGY COMPOSITION ===")
    print(f"State: {state}")

    for name, bot in bots:
        print(f"{name}: {bot.choose_action(state)}")


if __name__ == "__main__":
    main()
