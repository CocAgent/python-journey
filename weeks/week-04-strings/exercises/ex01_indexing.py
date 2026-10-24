"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print("Ky tu dau:", s[0])
print("Ký tự cuối:", s[-1])
print("5 ký tự đầu:", s[:5])



# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
s = "Journey"
print(s[:7])
print(s[::-1])
print(s[::2])

# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099

cccd =input("Nhập CCCD: ").strip()
print("Tỉnh:", cccd[:2])
print("Giới tính:", cccd[2])
print("Năm sinh:", cccd[3:5])



# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
chuoi = input("Nhập chuỗi: ").strip()
if chuoi == chuoi[::-1]:
    print("Chuỗi đối xứng")
else:
    print("Chuỗi không đối xứng")
