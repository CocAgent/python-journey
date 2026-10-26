"""Exercise 02: compose Bot with a strategy."""


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
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def main() -> None:
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    reverse_state = {"position": 3, "opponent_position": 4, "goal": 0}

    bot = Bot(defensive)
    print("Defensive:", bot.choose_action(state))

    bot.strategy = balanced
    print("Balanced:", bot.choose_action(state))

    bot.strategy = aggressive
    print("Aggressive:", bot.choose_action(state))

    print("Reverse:")
    print("Defensive:", Bot(defensive).choose_action(reverse_state))
    print("Balanced:", Bot(balanced).choose_action(reverse_state))
    print("Aggressive:", Bot(aggressive).choose_action(reverse_state))


if __name__ == "__main__":
    main()
