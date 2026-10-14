"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Nhập tên của bạn: ")
print(f"Xin chào, {ten}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao nhiêu tuổi? "))
nam_sinh = 2024 - tuoi
print(f"Bạn sinh năm khoảng {nam_sinh}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))
tong = so_1 + so_2
print(f"Tổng: {so_1} + {so_2} = {tong}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten_mad = input("Nhập một cái tên: ")
tinh_tu = input("Nhập một tính từ: ")
con_vat = input("Nhập một con vật: ")
so_luong = input("Nhập một con số: ")

print(f"\n--- Câu chuyện Mad Libs ---")
print(f"Ngày xửa ngày xưa, có một chú {con_vat} tên là {ten_mad}.")
print(f"Chú ta trông rất {tinh_tu} và có đến tận {so_luong} cái chân!")
