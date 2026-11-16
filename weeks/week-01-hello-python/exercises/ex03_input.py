"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = input("Bạn tên là gì? ")
print("Xin chào,", name, "!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
age = int(input("Bạn bao nhiêu tuổi? "))
birth_year = 2026 - age
print("Bạn sinh khoảng năm:", birth_year)

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
number1 = int(input("Nhập số thứ nhất: "))
number2 = int(input("Nhập số thứ hai: "))

total = number1 + number2

print("Tổng:", number1, "+", number2, "=", total)

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
print("\n--- CÂU CHUYỆN VUI ---")

story_name = input("Nhập tên một người: ")
adjective = input("Nhập một tính từ: ")
animal = input("Nhập tên một con vật: ")
number = input("Nhập một con số: ")

print("\nHôm nay,", story_name, "gặp một con", animal,
      adjective, "và nó đã nhảy", number, "lần!")
