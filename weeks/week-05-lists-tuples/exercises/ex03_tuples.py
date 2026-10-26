"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x = 0
y = 0
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("", 0, "")
name = "Sơn"
age = 19
topic = "Python"
profile: tuple[str, int, str] = (name, age, topic)
profile_name, profile_age, profile_topic = profile
# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left

print("Tọa độ:", x, y)
print("Hồ sơ:", profile)
print("Tách hồ sơ:", profile_name, profile_age, profile_topic)
print("Sau khi đổi chỗ:", left, right)