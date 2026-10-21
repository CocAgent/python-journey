"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    if position < 0 or goal < 0:
        raise ValueError("positions must be non-negative")
    return abs(goal - position)


if __name__ == "__main__":
    assert distance(1, 4) == 3
    assert distance(4, 1) == 3
    print(distance(1, 4))
