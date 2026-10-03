"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# 1. unpack coordinate into x and y.
x, y = coordinate  # x = 3, y = 7

# 2. pack name, age and topic into one profile tuple, then unpack it.
name = "Anh"
age = 20
topic = "Python"

profile: tuple[str, int, str] = (name, age, topic)  # Packing
p_name, p_age, p_topic = profile                     # Unpacking

# 3. swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left  # Swap: left = "B", right = "A"

print("x, y:", x, y)
print("Profile tuple:", profile)
print("Unpacked profile:", p_name, p_age, p_topic)
print("Sau khi swap (left, right):", left, right)
