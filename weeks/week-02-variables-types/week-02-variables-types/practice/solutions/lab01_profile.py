"""Lời giải tham khảo 01 — type() không tự thay đổi kiểu dữ liệu."""

name = "An"
age_text = "18"
is_learning = True

age = int(age_text)
print(f"Tên: {name}")
print(f"Tuổi năm sau: {age + 1}")
print(f"Kiểu tuổi: {type(age).__name__}")
print(f"Đang học: {is_learning}")
