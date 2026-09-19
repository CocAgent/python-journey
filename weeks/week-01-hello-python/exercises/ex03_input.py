"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = input("Nhập tên của bạn: ")
print(f"Xin chào, {name}!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!

age = int(input("Bạn bao nhiêu tuổi? "))
birth_year = 2026 - age
print("Năm sinh của bạn là:", birth_year)


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

total = num1 + num2

print(f"Tổng: {num1} + {num2} = {total}")



# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
name = input("Nhập tên: ")
adjective = input("Nhập một tính từ: ")
animal = input("Nhập một con vật: ")
number = int(input("Nhập một số: "))

print(f"\nHôm nay, {name} gặp một con {animal} rất {adjective}.")
print(f"Điều bất ngờ là con {animal} có tận {number} chiếc bánh!")
print(f"{name} bật cười và cùng con {animal} mở tiệc.")
