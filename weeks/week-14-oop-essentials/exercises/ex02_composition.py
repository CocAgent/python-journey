"""Exercise 02: compose Bot with a strategy."""


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


class Bot:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def main() -> None:
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    print(Bot(defensive).choose_action(state))
    print(Bot(balanced).choose_action(state))
    print(Bot(aggressive).choose_action(state))


if __name__ == "__main__":
    main()
