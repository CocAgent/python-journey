"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = input("Nhập tên của bạn: ")
print("Xin chào,", name, "!")
# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
age = int(input("Nhập tuổi của bạn: "))
ns = 2026 - age
print("Năm sinh của bạn là:", ns)
# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
one = int(input("Nhập số thứ nhất: "))
two = int(input("Nhập số thứ hai: "))
sum = one + two
print("Tổng: ", one , "+", two, "=", sum)
# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
name = input("Nhập một cái tên: ")
adj = input("Nhập một tính từ: ")
animal = input("Nhập một con vật: ")
number = input("Nhập một con số: ")
print("Câu truyện của", name, "là một người rất", adj, "một hôm", name, "gặp", number, "con", animal, "đang đi dạo trước nhà. Thật là", adj, "làm sao!")