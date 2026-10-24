"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    """Return the non-negative distance from position to goal."""
    return goal - position


assert distance(1, 4) == 3
print(distance(1, 4))
