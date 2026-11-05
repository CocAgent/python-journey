"""Lời giải tham khảo Lab 03: unpack, swap và tuple một phần tử."""

coordinate = (3, 7)
profile = ("An", 20, "Python")
left, right = "A", "B"

x, y = coordinate
name, age, topic = profile
left, right = right, left
one_item = ("Cóc",)

print(f"Tọa độ: x={x}, y={y}")
print(f"Học viên: {name}, {age} tuổi, học {topic}")
print(f"Đổi chỗ: {left}, {right}")
print(f"Tuple một phần tử: {one_item}")
print(f"Kiểu: {type(one_item).__name__}")
