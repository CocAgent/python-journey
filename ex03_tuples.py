"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
# Unpacking (giải nén tuple): Gán lần lượt từng giá trị của tuple cho các biến x, y
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
name = "An"
age = 20
topic = "Python"

# 1. Packing (đóng gói): Gom các biến riêng lẻ vào một tuple `profile`
profile: tuple[str, int, str] = (name, age, topic)

# 2. Unpacking (giải nén): Tách các giá trị từ tuple ra lại các biến riêng rẽ
unpacked_name, unpacked_age, unpacked_topic = profile
print(f"Unpacked profile: name={unpacked_name}, age={unpacked_age}, topic={unpacked_topic}")

# TODO: swap left and right using unpacking.
# Hoán đổi giá trị 2 biến trong Python mà không cần dùng biến trung gian (biến tạm)
left = "A"
right = "B"
left, right = right, left

print(x, y, profile, left, right)