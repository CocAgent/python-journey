"""Logic ra quyết định. Hàm này không biết CLI, HTTP hay VuaCóc production."""


def choose_action(position: int, goal: int) -> str:
    """Trả về hành động tiến về goal từ position trong ví dụ course-local."""
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
