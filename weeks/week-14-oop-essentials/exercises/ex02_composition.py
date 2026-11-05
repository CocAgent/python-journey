"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Bot sử dụng composition để ủy nhiệm việc chọn hành động cho một chiến lược."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Ủy nhiệm việc chọn hành động cho chiến lược hiện tại."""
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    """Chọn hướng di chuyển tới mục tiêu ở cả hai chiều hoặc đứng yên khi đã đến."""
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Ưu tiên đứng yên nếu đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Di chuyển theo hướng tới mục tiêu; tại đích thì đứng yên."""
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    return move_toward_goal(state)


if __name__ == "__main__":
    bot = Bot(balanced)
    print("Balanced (pos 1 -> goal 4):", bot.choose_action({"position": 1, "goal": 4}))
    bot.strategy = defensive
    print(
        "Defensive (pos 3 -> goal 0, opponent 4):",
        bot.choose_action({"position": 3, "goal": 0, "opponent_position": 4}),
    )
