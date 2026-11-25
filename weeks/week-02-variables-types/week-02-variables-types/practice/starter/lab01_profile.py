"""Bài tương tự 01 — biến, type và chuyển tuổi từ text sang int.

Hãy đọc PRACTICE-GUIDE.md và đoán kết quả trước khi sửa TODO.
"""

name = "An"
age_text = "18"  # str, chưa phải int
is_learning = True

# TODO 1: chuyển age_text sang int và lưu vào age.
age = int(age_text)

# TODO 2: in chính xác:
# Tên: An
# Tuổi năm sau: 19
# Kiểu tuổi: int
# Đang học: True
print(f"Tên: {name}")
print(f"Tuổi năm sau: {age + 1}")
print(f"Kiểu tuổi: {type(age).__name__}")
print(f"Đang học: {is_learning}")
