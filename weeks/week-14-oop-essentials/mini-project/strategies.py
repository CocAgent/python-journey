"""Mini-project Tuần 14: Các chiến lược ngoại tuyến một chiều."""

from __future__ import annotations


def move_toward_goal(state: dict[str, int]) -> str:
    """Tiến về phía mục tiêu trên trục 1 chiều; đến nơi thì đứng yên."""
    pos = state["position"]
    goal = state["goal"]
    if pos < goal:
        return "right"
    if pos > goal:
        return "left"
    return "wait"


def balanced(state: dict[str, int]) -> str:
    """Chiến lược cân bằng: di chuyển thẳng về mục tiêu."""
    return move_toward_goal(state)


def defensive(state: dict[str, int]) -> str:
    """Chiến lược phòng thủ: né tránh/dừng lại khi đối thủ áp sát <= 1 ô.

    Xử lý an toàn khi state không có key 'opponent_position'.
    """
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Chiến lược tấn công cơ bản trên trục 1D: tiến tới mục tiêu."""
    return move_toward_goal(state)
