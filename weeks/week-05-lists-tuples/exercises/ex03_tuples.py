"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("An", 20, "Python")
user_name, user_age, user_topic = profile

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left

print("x, y:", x, y)
print("profile:", profile)
print("unpacked profile:", user_name, user_age, user_topic)
print("left, right sau khi swap:", left, right)
