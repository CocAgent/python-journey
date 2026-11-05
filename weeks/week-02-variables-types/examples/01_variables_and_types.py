"""Observe four beginner Python value types."""

name = "An"
age = 18
height = 1.68
is_learning = True

values = (name, age, height, is_learning)
for value in values:
    print(f"value={value}, type={type(value).__name__}")
