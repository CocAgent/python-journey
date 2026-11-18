"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
name = input("Nhập tên của bạn: ")
print(f"Xin chào, {name}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
age = int(input("Nhập tuổi của bạn: "))
current_year = 2026
birth_year = current_year - age
print(f"Bạn sinh năm {birth_year}.")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
print(f"{num1} + {num2} = {num1 + num2}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
name = input("Tên của bạn: ")
adjective = input("Tính từ: ")
animal = input("Con vật: ")
number = input("Số: ")
print(f"Ngày hôm nay, {name} đã gặp một con {animal} {adjective} và nó có {number} màu.")
# Ví dụ: "Xin chào, Minh!"


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42


# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
