"""Week 14 mini-project: a Bot that accepts interchangeable strategies."""


def move_toward_goal(state):
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state):
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state):
    return move_toward_goal(state)


def aggressive(state):
    return move_toward_goal(state)


class Bot:
    """Delegate action selection to the strategy supplied at construction."""

    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


def run_demo():
    states = [
        {"position": 1, "opponent_position": 4, "goal": 4},
        {"position": 3, "opponent_position": 4, "goal": 0},
        {"position": 2, "opponent_position": 2, "goal": 2},
    ]
    for strategy in (defensive, balanced, aggressive):
        bot = Bot(strategy)
        print(f"\n{strategy.__name__.title()} strategy")
        for state in states:
            print(f"  {state} -> {bot.choose_action(state)}")


if __name__ == "__main__":
    run_demo()
