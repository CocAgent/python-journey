"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Bạn tên là gì? ").strip()
print(f"Xin chào, {ten}!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao nhiêu tuổi? "))
nam_hien_tai = 2026
nam_sinh = nam_hien_tai - tuoi
print(f"Bạn sinh khoảng năm {nam_sinh}")


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_1 = int(input("Nhập số thứ nhất: "))
so_2 = int(input("Nhập số thứ hai: "))
tong = so_1 + so_2
print(f"Tổng: {so_1} + {so_2} = {tong}")


# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten_nv = input("Nhập tên: ").strip()
tinh_tu = input("Nhập tính từ: ").strip()
con_vat = input("Nhập con vật: ").strip()
so_luong = input("Nhập một số: ").strip()

print(f"\n--- Câu chuyện của bạn ---")
print(f"{ten_nv} có một con {con_vat} rất {tinh_tu}.")
print(f"Mỗi ngày nó ăn {so_luong} bát cơm!")
