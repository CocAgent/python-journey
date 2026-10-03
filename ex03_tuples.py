"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# 1. Unpack (mở gói) tuple coordinate vào 2 biến x và y
x, y = coordinate
print(f"Toạ độ sau khi unpack: x = {x}, y = {y}")

# 2. Đóng gói (pack) name, age, topic vào tuple profile, sau đó unpack ra
name = "An"
age = 20
topic = "Python"
profile: tuple[str, int, str] = (name, age, topic)   # Tuple Packing: gom 3 biến vào 1 tuple

# Unpack tuple profile thành các biến riêng biệt
user_name, user_age, user_topic = profile
print(f"Profile đã unpack: Tên = {user_name}, Tuổi = {user_age}, Chủ đề = {user_topic}")

# 3. Đổi chỗ (swap) left và right bằng unpacking mà không cần biến tạm
left = "A"
right = "B"
left, right = right, left     # Python tạo tuple (right, left) rồi unpack ngược lại vào (left, right)

print("\n--- KẾT QUẢ IN CUỐI CÙNG ---")
print("x:", x, "| y:", y)
print("profile:", profile)
print(f"left: {left} (ban đầu là A), right: {right} (ban đầu là B)")
print("\nIn theo mẫu bài tập ban đầu:")
print(x, y, profile, left, right)
