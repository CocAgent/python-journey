"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("Nguyễn Tấn Dũng", 19, "Python Journey")
name, age, topic = profile
print(f"Hồ sơ đã unpack: Họ tên={name}, Tuổi={age}, Chủ đề={topic}")

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
print(f"Trước khi swap: left={left}, right={right}")
left, right = right, left
print(f"Sau khi swap: left={left}, right={right}")

print("Kết quả in ra:", x, y, profile, left, right)
