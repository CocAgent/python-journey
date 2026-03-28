"""
Bài tập 02: Nhiều loại Exception 🎯
=====================================
Mục tiêu: Xử lý nhiều lỗi, dùng else và finally
"""

# TODO 1: Viết chương trình đọc file và chia số
# try:
#     Đọc file chứa 2 số → chia số 1 cho số 2
# except FileNotFoundError: ...
# except ValueError: ...
# except ZeroDivisionError: ...
# else: in kết quả
# finally: in "Hoàn tất"


# TODO 2: Viết hàm get_value(data, key, index)
# data = {"scores": [85, 92, 78]}
# get_value(data, "scores", 1) → 92
# Xử lý: KeyError, IndexError, TypeError


# TODO 3: Nhập liệu an toàn (lặp đến khi đúng)
# Viết hàm get_float(prompt) hỏi người dùng nhập float
# Lặp lại nếu nhập sai, trả về khi nhập đúng


# TODO 4 (Thử thách): Decorator xử lý lỗi
# Viết decorator @safe_call in lỗi thay vì crash
