"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    """Bot ủy nhiệm việc chọn hành động cho strategy được truyền vào."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def _move_toward_goal(state: State) -> str:
    """Đi về goal ở cả hai chiều; nếu đã đến đích thì đứng yên."""
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    """Đứng yên khi đối thủ cách tối đa 1 ô; nếu không thì đi về đích."""
    opponent_position = state.get("opponent_position")
    if (
        opponent_position is not None
        and abs(opponent_position - state["position"]) <= 1
    ):
        return "wait"
    return _move_toward_goal(state)


def balanced(state: State) -> str:
    """Di chuyển thẳng về đích."""
    return _move_toward_goal(state)


def aggressive(state: State) -> str:
    """Chiến lược cơ bản: chủ động tiến về đích trong mô hình 1 chiều."""
    # Bài tập chưa mô hình hóa luật tấn công; hành vi di chuyển giống balanced.
    return _move_toward_goal(state)


if __name__ == "__main__":
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    bot = Bot(defensive)
    print(bot.choose_action(state))  # wait: đối thủ ở sát
    bot.strategy = balanced
    print(bot.choose_action(state))  # left: đích nằm bên trái
