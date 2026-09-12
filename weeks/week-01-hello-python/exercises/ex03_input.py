"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

# TODO 2: Hỏi tuổi người dùng, tính và in năm sin
# Gợi ý: Nhớ chuyển input sang int!
age = int(input("Nhập tuổi của bạn: "))
print("Năm sinh của bạn là:", 2026 - age)

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
print("Tổng:", so1, "+", so2, "=", so1 + so2)

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten_nv = input("Nhập tên: ")
tinh_tu = input("Nhập tính từ: ")
con_vat = input("Nhập con vật: ")
so = input("Nhập một con số: ")
print(ten_nv, "nuôi một", con_vat, "rất", tinh_tu, "và ăn hết", so, "bát cơm mỗi ngày!")