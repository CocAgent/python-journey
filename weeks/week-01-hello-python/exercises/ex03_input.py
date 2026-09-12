"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = input("ban ten la gi : ")
print(f"xin chao, {name}")
# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
age = int(input("ban bao nhieu tuoi : "))
print(f"ban sinh nam : {2026-age}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so1 = int(input("nhap so thu nhat : "))
so2 = int(input("nhap so thu hai : "))
print(f"tong cua {so1} va {so2} la : {so1+so2}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten = input("nhap ten : ")
tu = input("nhap tinh tu : ")
convat = input("nhap con vat : ")
so = int(input("nhap so : "))
print(f"{ten} co mot con {convat} rat {tu}")
print(f"Mỗi ngày nó ăn {so} bát cơm!")