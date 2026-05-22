"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng


# Bước 2: Tính độ rộng khung
# TODO: Tính width dựa trên len(ten)


# Bước 3: In khung trên
# TODO: In dòng trên bằng ╔═══╗

# Bước 4: In nội dung
# TODO: In tên trong khung, căn giữa

# Bước 5: In khung dưới
# TODO: In dòng dưới bằng ╚═══╝

# Gợi ý: Dùng str.center(width) để căn giữa
ten = input("Nhập tên của bạn: ")
line1 = "Xin chào"
line2 = f"{ten}!"
line3 = "🐍 Python 🐍"

width = max(len(line1), len(line2), len(line3)) + 10
# Bước 1: Hỏi tên người dùng


# Bước 2: Tính độ rộng khung


# Bước 3: In khung trên


# Bước 4: In nội dung


# Bước 5: In khung dưới


print("╔" + "═" * width + "╗")
print(f"║{line1.center(width)}║")
print(f"║{line2.center(width)}║")
print(f"║{line3.center(width)}║")
print("╚" + "═" * width + "╝")