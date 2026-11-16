"""Ví dụ 06 — Tuple, unpacking, hoán đổi, và khác list.

Không gán lại tuple[0] vì sẽ gây TypeError; thử sửa danh sách thay vì tuple.
"""

position = (3, 7)
x, y = position
print(f"Tọa độ: x={x}, y={y}")

profile = ("An", 20, "Python")
name, age, topic = profile
print(f"Học viên: {name}, {age} tuổi, học {topic}")

left, right = "A", "B"
left, right = right, left
print(f"Sau đổi chỗ: {left}, {right}")

one_item = ("Cóc",)  # Dấu phẩy làm nó thành tuple một phần tử.
not_tuple = ("Cóc")  # Chỉ có str, không phải tuple.
print(f"Kiểu một phần tử có dấu phẩy: {type(one_item).__name__}")
print(f"Không có dấu phẩy: {type(not_tuple).__name__}")

# position[0] = 9  # TypeError: tuple không hỗ trợ gán phần tử.
# Nếu có đủ 2 giá trị thì mới unpack được thành x, y.
candidate = (8,)
if len(candidate) == 2:
    x, y = candidate
    print(x, y)
else:
    print("Không unpack: cần chính xác hai giá trị")
