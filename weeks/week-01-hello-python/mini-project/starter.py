"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")

# Bước 2: Tính độ rộng khung
width = len(ten) + 20
# TODO: Tính width dựa trên len(ten)

# Bước 3: In khung trên
print("╔" + "═" * (width-2) + "╗")
# TODO: In dòng trên bằng ╔═══╗

# Bước 4: In nội dung
print("║" + "Xin chào".center(width-2) +"║")
print("║ " + ten.center(width-4) + " ║")
print("║" + "🐍 Python 🐍".center(width-4) +"║")
# TODO: In tên trong khung, căn giữa

# Bước 5: In khung dưới
print("╚" + "═" * (width-2) + "╝")
# TODO: In dòng dưới bằng ╚═══╝

# Gợi ý: Dùng str.center(width) để căn giữa


