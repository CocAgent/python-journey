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
from datetime import datetime
current_year = datetime.now().year
age_input = input("Nhập tuổi của bạn: ")
try:
    age = int(age_input)
except ValueError:
    age = 0
birth_year = current_year - age
print(f"Năm sinh của bạn là {birth_year}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
print(f"Tổng: {num1} + {num2} = {num1 + num2}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
person_name = input("Nhập tên: ")
adjective = input("Nhập tính từ: ")
animal = input("Nhập con vật: ")
number = input("Nhập số: ")
print(f"{person_name} có một con {animal} {adjective} và {number} viên kẹo.")
