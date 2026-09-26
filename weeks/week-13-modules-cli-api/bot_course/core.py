"""Network-free bot decision core."""


def choose_action(position: int, goal: int) -> str:
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
