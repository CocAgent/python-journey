"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print(f"ky tu dau: {s[0]}")
print(f"ky tu cuoi: {s[-1]}")
print(f"5 ky tu dau: {s[:5]}")

# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
print(f"lay 'journey': {s[7:]}")
print(f"dao nguoc chuoi: {s[-1::-1]}")
print(f"lay moi ky tu thu 2: {s[1:12:2]}")

# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
cccd = input("Nhap CCCD (12 chu so): ")
ma_tinh = cccd[:2]
gioi_tinh = cccd[2]
nam_sinh = cccd[3:5]
print(f"Tinh: {ma_tinh}, Gioi tinh: {gioi_tinh}, Nam sinh: {nam_sinh}")

# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
chuoi = input("nhap chuoi: ")
if chuoi == chuoi[::-1]:
    print("chuoi doi xung")
else:
    print("chuoi khong doi xung")
