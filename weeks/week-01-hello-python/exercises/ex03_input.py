"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten  = input("Bạn tên là gì? ")
print("xin chào,",ten)

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao nhiêu tuổi? "))
namsinh = 2026 - tuoi
print("BẠn sinh năm:",namsinh)

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:li
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
tong = so1 + so2
print(f"Tổng hai số là: {so1} + {so2} = {tong}")
# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
tenn = input("Hãy nhập 1 cái tên:")
tinhtu = input("Hãy chọn tính từ (ngố, dễ thương, béo): ")
convat = input("Hãy chọn một con vật (chó, mèo, cú): ")
so = input("Hãy chọn 1 con số: ")
print("\n---CÂU CHUYỆN VUI CỦA BẠN---")
print(f"{tenn} là con {convat} rất {tinhtu}.")
print(f"Mỗi ngày nó ăn hết {so} cám heo")