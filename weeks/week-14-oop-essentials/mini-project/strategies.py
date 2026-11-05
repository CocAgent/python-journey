"""Mini-project: Các chiến lược di chuyển độc lập cho Bot."""


def move_toward_goal(state: dict[str, int]) -> str:
    """Điều hướng bot tiến về ô mục tiêu: 'right', 'left' hoặc 'wait' khi đã tới."""
    pos = state["position"]
    goal = state["goal"]
    if pos < goal:
        return "right"
    if pos > goal:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Chiến lược phòng thủ: Đứng yên ('wait') nếu đối thủ ở cách tối đa 1 ô.

    Nếu an toàn, di chuyển về phía mục tiêu.
    Không làm thay đổi dictionary state đầu vào.
    """
    pos = state["position"]
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - pos) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Chiến lược cân bằng: Luôn tìm đường ngắn nhất hướng về mục tiêu."""
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Chiến lược chủ động: Tiến nhanh về mục tiêu (trong mô hình 1 chiều tương đương balanced)."""
    return move_toward_goal(state)

