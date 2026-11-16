"""Ví dụ 2: thay chiến lược của Bot mà không sửa class Bot."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    def __init__(self, strategy: Strategy) -> None:
        # Bot giữ tham chiếu tới hành vi được truyền từ bên ngoài.
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    """Mục tiêu có thể nằm bên trái, bên phải hoặc ngay tại vị trí."""
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


if __name__ == "__main__":
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    bot = Bot(defensive)
    print(bot.choose_action(state))  # wait: đối thủ ở sát
    # Đổi thành phần chiến lược; Bot không cần kế thừa hay viết lại.
    bot.strategy = balanced
    print(bot.choose_action(state))  # left: đích nằm bên trái
