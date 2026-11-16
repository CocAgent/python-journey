"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Xin chào bạn tên là gì thế?: ")
print(f"Xin chào, {ten}!")
print()

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao thiêu tuổi thế?: "))
year = 2026
print("Năm sinh của bạn là:", year - tuoi)
print()

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print(f"Tổng: {a} + {b} = {a + b}")
print()

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten = input("Nhập một cái tên: ")
tinhtu = input("Nhập một tính từ: ")
convat = input("Nhập tên một con vật: ")
so = input("Nhập một con số: ")
print(f"Hôm qua, {ten} đang đi dạo trong công viên thì bất ngờ gặp một con {convat} cực kỳ {tinhtu}.")
print(f"Nó nhìn {ten} chằm chằm rồi bất ngờ nhảy lên {so} cái và bỏ chạy mất!")