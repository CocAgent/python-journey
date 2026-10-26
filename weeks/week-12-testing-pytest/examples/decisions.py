"""Hàm quyết định hướng di chuyển để minh họa kiểm thử."""


def choose_step(position: int, goal: int) -> str:
    """Đi về đích; đứng yên nếu đã tới đúng vị trí."""
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
