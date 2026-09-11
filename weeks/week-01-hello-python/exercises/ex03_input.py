"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Tên của bạn là gì? ")
print(f"Xin chào, {ten}!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao nhiêu tuổi? "))
nam_sinh = 2026 - tuoi
print(f"Bạn sinh năm {nam_sinh}.")


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_thu_nhat = int(input("Nhập số thứ nhất: "))
so_thu_hai = int(input("Nhập số thứ hai: "))
tong = so_thu_nhat + so_thu_hai
print(f"Tổng: {so_thu_nhat} + {so_thu_hai} = {tong}")


# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten_nhan_vat = input("Nhập một cái tên: ")
tinh_tu = input("Nhập một tính từ: ")
con_vat = input("Nhập tên một con vật: ")
so_luong = input("Nhập một số: ")
print(
	f"{ten_nhan_vat} gặp một {con_vat} {tinh_tu} và cùng nhau nhảy {so_luong} lần."
)
