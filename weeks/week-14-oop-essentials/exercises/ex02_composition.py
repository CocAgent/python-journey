"""Exercise 02: compose Bot with a replaceable strategy."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]
LOCAL_ACTIONS = {"left", "right", "wait"}


def move_toward_goal(state: State) -> str:
    """Move one step toward the goal, including boundary positions."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    """Wait if the opponent is adjacent; otherwise move toward the goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state.get("position", 0)) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> str:
    """Use the straightforward goal-seeking rule."""
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    """Prefer goal progress even when the opponent is nearby."""
    return move_toward_goal(state)


class Bot:
    """Delegate decisions to a strategy supplied by the caller."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        action = self.strategy(state)
        if action not in LOCAL_ACTIONS:
            raise ValueError(f"illegal local action: {action!r}")
        return action


def main() -> None:
    state = {"position": 0, "goal": 4, "opponent_position": 1}
    for name, strategy in (("defensive", defensive), ("balanced", balanced), ("aggressive", aggressive)):
        bot = Bot(strategy)
        print(f"{name}: {bot.choose_action(state)}")

    bot.strategy = balanced
    print(f"swapped strategy: {bot.choose_action({ 'position': 4, 'goal': 0 })}")


if __name__ == "__main__":
    main()
