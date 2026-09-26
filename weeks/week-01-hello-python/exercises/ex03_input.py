"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name=input("\nHãy nhập tên của bạn: ")
print(f"Xin chào, {name}!\n")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
from datetime import date
tuoi=int(input("Năm nay bạn bao nhiêu tuổi: "))
print(f"Năm sinh của bạn là: {date.today().year-tuoi}\n")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
a=int(input("Nhập số thứ nhất: "))
b=int(input("Nhập số thứ hai: "))
print(f"Tổng: {a} + {b} = {a+b}\n")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten=input("Nhập một cái tên: ")
tinhtu=input("Nhập một tính từ miêu tả ngoại hình hoặc tính cách: ")
convat=input("Nhập một loài vật: ")
so=int(input("Nhập một con số: "))
print("\n" + "="*50)
print("CÂU CHUYỆN HÀI HƯỚC\n")
print(f"Một ngày nọ, {ten} đang đi dạo thì bắt gặp một con {convat} trông cực kỳ {tinhtu}.")
print(f"Con {convat} bỗng nhiên biết nói tiếng người và đòi {ten} chia cho nó {so} viên kẹo.")
print(f"Vì quá hoảng sợ, {ten} đã cõng luôn con {convat} trên lưng và chạy với vận tốc gấp {so} lần bình thường=)))\n")