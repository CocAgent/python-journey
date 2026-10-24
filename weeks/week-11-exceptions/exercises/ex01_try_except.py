"""Exercise 01: handle expected bad input with try/except."""

raw_turn = "not-a-number"

try:
    # int() raises ValueError when the text is not a valid integer.
    turn = int(raw_turn)
except ValueError:
    # Catch only the error we expect from invalid user input.
    print(f"Invalid turn {raw_turn!r}: please enter a whole number.")
else:
    # This block runs only when conversion succeeds.
    print(f"Turn: {turn}")
