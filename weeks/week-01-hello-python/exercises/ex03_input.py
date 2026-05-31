"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# ============================================================
# TODO 1: Hỏi tên người dùng và in lời chào
# ============================================================

# input()
# dùng để nhập dữ liệu từ bàn phím

# dữ liệu nhập vào luôn là chuỗi (str)

ten = input("Nhập tên của bạn: ")

# f-string
# dùng để chèn biến vào chuỗi

print(f"Xin chào, {ten}!")


# ============================================================
# TODO 2: Hỏi tuổi người dùng, tính năm sinh
# ============================================================

# int()
# đổi dữ liệu từ chuỗi sang số nguyên

tuoi = int(input("Nhập tuổi của bạn: "))

# tạo biến lưu năm hiện tại

nam_hien_tai = 2026

# tính năm sinh

nam_sinh = nam_hien_tai - tuoi

print(f"Bạn sinh năm {nam_sinh}")


# ============================================================
# TODO 3: Nhập 2 số và tính tổng
# ============================================================

so1 = int(input("Nhập số thứ nhất: "))

so2 = int(input("Nhập số thứ hai: "))

# dấu +
# phép cộng

tong = so1 + so2

print(f"Tổng: {so1} + {so2} = {tong}")


# ============================================================
# TODO 4: Mad Libs mini
# ============================================================

# Mad Libs:
# người dùng nhập dữ liệu
# Python ghép lại thành câu chuyện

ten = input("Nhập một cái tên: ")

tinh_tu = input("Nhập một tính từ: ")

con_vat = input("Nhập tên một con vật: ")

# không cần int()
# vì chỉ dùng để in

so = input("Nhập một con số: ")

# \n
# xuống dòng

print("\n--- Câu chuyện vui ---")

print(f"Một ngày nọ, {ten} gặp một con {con_vat} rất {tinh_tu}.")

print(f"Cả hai cùng chạy {so} vòng quanh công viên và cười rất vui!")
