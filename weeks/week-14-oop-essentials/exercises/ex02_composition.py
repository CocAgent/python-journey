"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
    def __init__(self, strategy) -> None:
        # Lưu hàm chiến lược để có thể thay thế khi cần.
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        # Ủy nhiệm việc chọn hành động cho chiến lược hiện tại.
        return self.strategy(state)


def _move_toward_goal(state: dict[str, int]) -> str:
    """Chọn hướng đi tới goal trong mô hình một chiều."""
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Đứng yên nếu đối thủ cách tối đa 1 ô; nếu không thì đi tới đích."""
    opponent_position = state.get("opponent_position")

    if opponent_position is not None:
        distance = abs(state["position"] - opponent_position)
        if distance <= 1:
            return "wait"

    return _move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    return _move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình một chiều cơ bản, đi về đích như balanced."""
    return _move_toward_goal(state)
