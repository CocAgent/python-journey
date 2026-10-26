"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("Học Sinh", 18, "Python")
name, age, topic = profile

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left

print(x, y, profile, left, right)
