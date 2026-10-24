"""Exercise 03: reproduce and fix a defect.

The distance between two non-negative positions is the absolute difference.
Negative positions violate the function's contract and must raise ValueError.
"""


def distance(position: int, goal: int) -> int:
    """Return the absolute distance between two non-negative positions."""
    if position < 0 or goal < 0:
        raise ValueError("positions must be non-negative")
    return abs(goal - position)


def main() -> None:
    # Regression checks for both directions and identical positions.
    assert distance(1, 4) == 3
    assert distance(4, 1) == 3
    assert distance(2, 2) == 0

    for position, goal in ((-1, 4), (1, -4)):
        try:
            distance(position, goal)
        except ValueError as error:
            assert "non-negative" in str(error)
        else:
            raise AssertionError(
                f"negative position was accepted: {position=}, {goal=}"
            )

    print("Distance:", distance(1, 4))
    print("Exercise 03 checks: PASS")


if __name__ == "__main__":
    main()
