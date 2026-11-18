"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhap ten cua ban: ")

# Bước 2: Tính độ rộng khung
message = f"Xin chao {ten}!"
width = len(message) + 2

# Bước 3: In khung trên
print("+" + "-" * width + "+")

# Bước 4: In nội dung
print("| " + message + " |")

# Bước 5: In khung dưới
print("+" + "-" * width + "+")
