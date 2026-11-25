"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Tên của bạn: ")
print(f"Xin chào, {ten}!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Tuổi của bạn: "))
nam_hien_tai = int(input("Năm hiện tại: "))
print(f"Năm sinh ước tính: {nam_hien_tai - tuoi}")


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_thu_nhat = float(input("Nhập số thứ nhất: "))
so_thu_hai = float(input("Nhập số thứ hai: "))
print(f"Tổng: {so_thu_nhat:g} + {so_thu_hai:g} = {so_thu_nhat + so_thu_hai:g}")


# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten_nhan_vat = input("Tên nhân vật: ")
tinh_tu = input("Một tính từ: ")
con_vat = input("Một con vật: ")
so_luong = int(input("Một số nguyên: "))
print(f"{ten_nhan_vat} gặp {so_luong} con {con_vat} rất {tinh_tu} trên đường học Python.")
