"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Bạn tên là gì? ")
print("xin chào,",ten)

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao nhiêu tuổi?"))
namsinh = 2026 - tuoi
print("Bạn sinh năm", namsinh)

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so1 = int(input("Nhập số thứ nhất:"))
so2 = int(input("Nhập số thứ hai:"))
tong = so1+so2
print("Tổng là:",tong)

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten = input("Nhập tên: ")
tinhtu = input("Nhập tính từ (vd:ngáo,cute,béo) :")
convat = input("Nhập con vật: ")
so = input("Nhập một con số :")
print("---Câu truyện cười không hài----")
print(f"Nhà {ten} có con {convat} trắng")
print(f"rất {tinhtu} và rất {tinhtu}")
print(f"còn thêm {so} cô vợ là em {convat} xám")