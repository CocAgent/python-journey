"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
name = "An"
age = 20
topic = "Python"
profile: tuple[str, int, str] = (name, age, topic)
name_unpacked, age_unpacked, topic_unpacked = profile

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left

print(x, y, profile, left, right)
