"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")

# Bước 2: Tính độ rộng khung
# Tính width dựa trên len(ten), đảm bảo khung tối thiểu rộng 20 ký tự
width = max(len(ten) + 8, 20)

# Bước 3: In khung trên
print("╔" + "═" * width + "╗")

# Bước 4: In nội dung
print("║" + "Xin chào".center(width) + "║")
print("║" + ten.upper().center(width) + "║")
print("║" + "🐍 Python 🐍".center(width) + "║")

# Bước 5: In khung dưới
print("╚" + "═" * width + "╝")
