"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Bạn tên là gì? ")
print(f"Xin chào, {ten}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi = int(input("Bạn bao nhiêu tuổi? "))
nam_hien_tai = 2026
nam_sinh = nam_hien_tai - tuoi
print(f"Bạn sinh năm {nam_sinh}")
# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
s1 = int(input("Nhập số thứ nhất: "))
s2 = int(input("Nhập số thứ hai: "))
print((f"Tổng:{s1} + {s2} = {s1 + s2}"))

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten = input("Nhập tên của bạn: ")
tinh_tu = input("Nhập một tính từ: ")
con_vat = input("Nhập một con vật: ")
so = input("Nhập một số: ")
print(f"{ten} là một người {tinh_tu}. {ten} có một con {con_vat} và chúng sống hạnh phúc với {so} món ăn mỗi ngày.")
