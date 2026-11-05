"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")

# Bước 2: Tính độ rộng khung
# Cộng 16 để chừa đủ chỗ cho emoji và căn giữa đẹp mắt
width = len(ten) + 15

# Bước 3: In khung trên
print("╔" + "═" * width + "╗")

# Bước 4: In nội dung
ten_emoji = "✨ " + ten + " ✨"
print("║" + ten_emoji.center(width) + "║")
print("║" + "🐍 Python 🐍".center(width) + "║")

# Bước 5: In khung dưới
print("╚" + "═" * width + "╝")



# Gợi ý: Dùng str.center(width) để căn giữa
