"""Show a fixed function and its regression assertion."""


def final_position(start: int, steps: int) -> int:
    return start + steps


failing_input = (1, 2)
assert final_position(*failing_input) == 3
print("regression=PASS")
