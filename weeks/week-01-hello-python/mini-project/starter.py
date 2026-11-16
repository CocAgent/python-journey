"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")

# Bước 2: Tính độ rộng khung
thong_diep = f"Xin chào {ten}!"
width = max(len(thong_diep) + 4, 20)

# Bước 3: In khung trên
print("╔" + "═" * width + "╗")

# Bước 4: In nội dung
# In thông điệp chứa tên người dùng trong khung, căn giữa bằng .center()
print("║" + thong_diep.center(width) + "║")

# Bước 5: In khung dưới
print("╚" + "═" * width + "╝")
