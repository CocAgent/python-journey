"""Exercise 01: expected bad input."""

raw_turn = "not-a-number"

try:
    turn = int(raw_turn)
except ValueError:
    print(f"Invalid turn {raw_turn!r}: expected an integer.")
else:
    print(f"Turn: {turn}")
