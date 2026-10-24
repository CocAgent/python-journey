"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
name = "An"
age = 20
topic = "Python"
profile: tuple[str, int, str] = (name, age, topic)
unpacked_name, unpacked_age, unpacked_topic = profile

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left

print(f"Point: x={x}, y={y}")
print(f"Profile tuple: {profile}")
print(f"Unpacked profile: name={unpacked_name}, age={unpacked_age}, topic={unpacked_topic}")
print(f"Swapped: left={left}, right={right}")
print(x, y, profile, left, right)
