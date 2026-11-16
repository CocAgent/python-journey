"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Nhap ten cua ban: ")
print("Xin chao,",ten,"!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
print("Ban bao nhieu tuoi?")
tuoi = int(input("Nhap tuoi cua ban: "))
namsinh = 2026 - tuoi
print(namsinh)

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
print("Nhap hai so")
sothunhat = int(input("Nhap so thu nhat: "))
sothuhai = int(input("Nhap so thu hai: "))
tong = sothunhat + sothuhai
print("Tong la:",tong)


# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
tengi = input("Nhap ten bat ki: ")
tinhtu = input("Nhap tinh tu bat ki: ")
convat = input("Nhap con vat bat ki: ")
so = int(input("Nhap so bat ki: "))
print("O mot thanh pho no, co mot nguoi ten la",tengi,",",
      tengi,"la mot nguoi",tinhtu,". Khi dang di tren duong toi nha ban be thi",
      tengi,"bat gap con",convat,", o day co khoang",so,"con dang nhin",tengi)
