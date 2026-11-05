"""Bài 2: composition — Bot ủy nhiệm hành động cho strategy."""


def _move_toward_goal(state: dict[str, int]) -> str:
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


class Bot:
    """Bot chứa một chiến lược có thể thay thế khi chạy chương trình."""

    def __init__(self, strategy) -> None:
        if not callable(strategy):
            raise TypeError("strategy phải là một hàm có thể gọi")
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def defensive(state: dict[str, int]) -> str:
    """Ưu tiên an toàn: đứng yên nếu đối thủ cách không quá một ô."""
    opponent_position = state.get("opponent_position")
    if opponent_position is not None and abs(state["position"] - opponent_position) <= 1:
        return "wait"
    return _move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Di chuyển về phía mục tiêu; đứng yên nếu đã tới đích."""
    return _move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Chiến lược cơ bản: chủ động đi thẳng về mục tiêu."""
    return _move_toward_goal(state)
