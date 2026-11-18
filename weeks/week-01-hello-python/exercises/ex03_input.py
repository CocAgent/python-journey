"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = input("Bạn tên là gì? ")
print(f"Xin chào, {name}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
age = int(input("Bạn bao nhiêu tuổi? "))
birth_year = 2026 - age
print(f"Bạn sinh năm khoảng: {birth_year}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
print(f"Tổng: {num1} + {num2} = {num1 + num2}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
story_name = input("Nhập tên: ")
story_adj = input("Nhập tính từ: ")
story_animal = input("Nhập con vật: ")
story_num = input("Nhập một số: ")

print("\n--- Câu chuyện vui ---")
print(f"{story_name} có một con {story_animal} rất {story_adj}.")
print(f"Mỗi ngày nó ăn {story_num} bát cơm!")
