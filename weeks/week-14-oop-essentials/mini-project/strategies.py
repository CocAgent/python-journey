"""Module chứa các hàm chiến lược độc lập cho Bot.

Mỗi hàm chiến lược nhận trạng thái `state` và trả về hành động.
Các hàm không làm biến đổi (mutate) dữ liệu bên trong `state`.
"""


def move_toward_goal(state: dict[str, int]) -> str:
    """Hàm phụ trợ: điều hướng Bot về phía mục tiêu trên trục 1 chiều."""
    pos = state["position"]
    goal = state["goal"]
    if pos < goal:
        return "right"
    if pos > goal:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Chiến lược phòng thủ: ưu tiên an toàn khi đối thủ ở quá gần.

    Nếu đối thủ cách vị trí hiện tại tối đa 1 ô (khoảng cách <= 1),
    Bot sẽ dừng lại ("wait") để phòng thủ. Nếu không có đối thủ hoặc
    đối thủ ở xa, Bot sẽ tiến về đích.
    """
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Chiến lược cân bằng: di chuyển đều đặn về phía đích."""
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Chiến lược tấn công cơ bản trong mô hình 1 chiều: luôn tiến về đích."""
    return move_toward_goal(state)
