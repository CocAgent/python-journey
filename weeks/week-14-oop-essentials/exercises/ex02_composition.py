"""Exercise 02: use composition to make a Bot's strategy replaceable."""


def move_toward_goal(state):
    """Choose a horizontal move using both the current position and goal."""
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state):
    """Wait when the opponent is adjacent; otherwise move toward the goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state):
    """Use the direct path toward the goal."""
    return move_toward_goal(state)


def aggressive(state):
    """Use direct movement in this small course-local example."""
    return move_toward_goal(state)


class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    for strategy in (defensive, balanced, aggressive):
        print(strategy.__name__, "->", Bot(strategy).choose_action(state))

    reverse_state = {"position": 3, "opponent_position": 4, "goal": 0}
    for strategy in (defensive, balanced, aggressive):
        print(strategy.__name__, "goal=0 ->", Bot(strategy).choose_action(reverse_state))
