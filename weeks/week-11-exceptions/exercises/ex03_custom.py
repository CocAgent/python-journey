"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    if position < 0 or goal < 0:
        raise ValueError("positions must be non-negative")
    return abs(goal - position)


assert distance(1, 4) == 3
print(distance(1, 4))
