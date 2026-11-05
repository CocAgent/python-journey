"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Bot quản lý hành vi thông qua việc ủy nhiệm cho strategy (composition)."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Ủy quyền quyết định hành động cho chiến lược hiện tại."""
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    """Hàm phụ trợ: di chuyển về phía mục tiêu, đứng yên khi đã đến đích."""
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    return move_toward_goal(state)

