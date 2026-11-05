"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def defensive(state: dict[str, int]) -> str:
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    position = state["position"]
    goal = state["goal"]
    opponent = state.get("opponent_position")
    if opponent is not None and abs(position - opponent) <= 1:
        return "stay"
    if position < goal:
        return "right"
    elif position > goal:
        return "left"
    else:
        return "stay"


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    elif position > goal:
        return "left"
    else:
        return "stay"


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    return balanced(state)


if __name__ == "__main__":
    state = {"position": 2, "goal": 5, "opponent_position": 3}
    bot1 = Bot(defensive)
    bot2 = Bot(balanced)
    bot3 = Bot(aggressive)
    print(bot1.choose_action(state))  # stay
    print(bot2.choose_action(state))  # right
    print(bot3.choose_action(state))  # right
