"""Official solution for a small debugging regression."""


def distance(position: int, goal: int) -> int:
    if position < 0 or goal < 0:
        raise ValueError("positions must be non-negative")
    return abs(goal - position)
