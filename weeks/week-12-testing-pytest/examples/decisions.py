"""Small behavior to test."""


def choose_step(position: int, goal: int) -> str:
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
