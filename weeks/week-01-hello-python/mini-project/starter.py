"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")

# Bước 2: Tính độ rộng khung
# TODO: Tính width dựa trên len(ten)
width = len(ten) + 4

# Bước 3: In khung trên
# TODO: In dòng trên bằng ╔═══╗
print("╔" + "═" * width + "╗")


# Bước 4: In nội dung
# TODO: In tên trong khung, căn giữa
print("║" + ten.center(width) + "║")


# Bước 5: In khung dưới
# TODO: In dòng dưới bằng ╚═══╝
print("╚" + "═" * width + "╝")


# Gợi ý: Dùng str.center(width) để căn giữa


