"""Hàm mẫu cần được sinh viên viết test, không sửa khi mới làm bài."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(position: int, goal: int) -> str:
    """Trả hành động đưa bot về đích; tại đích thì đứng yên."""
    if position == goal:
        return "wait"
    return "right" if position < goal else "left"


def validate_turn(turn: int) -> int:
    """Chỉ chấp nhận lượt chơi dương (bắt đầu từ 1)."""
    if turn < 1:
        raise ValueError("turn must be positive")
    return turn
