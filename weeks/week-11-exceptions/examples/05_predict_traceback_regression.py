"""Example 05: traceback type/message, minimal failing input, small fix."""

import traceback


def buggy_distance(start: int, goal: int) -> int:
    """Intentional bug: forget abs()."""
    return goal - start


def distance(start: int, goal: int) -> int:
    """Fix: distance should be nonnegative."""
    return abs(goal - start)


def main() -> None:
    failing_input = (4, 1)
    print(f"Bug reproduced: {buggy_distance(*failing_input)} != 3")
    print(f"Fixed result: {distance(*failing_input)}")
    assert distance(*failing_input) == 3
    assert distance(1, 4) == 3
    print("Regression: PASS")

    try:
        int("bad")
    except ValueError as error:
        frames = traceback.extract_tb(error.__traceback__)
        print(f"Traceback exception type: {type(error).__name__}")
        print(f"Failing operation: {frames[-1].line}")
        print("Read traceback bottom-up, then locate the failing operation")


if __name__ == "__main__":
    main()
