"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print(s)
print("Kí tự đầu:", s[0])
print("Kí tự cuối:", s[-1])
print("5 kí tự đầu:", s[:5])

# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
print("Lấy Journey:", s[7:])
print("Đảo ngược:", s[::-1])
print("Lấy mỗi kí tự thứ 2:", s[::2])

# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
cccd = input("Nhập CCCD (12 chữ số): ")
ma_tinh = cccd[:3]
gioi_tinh = cccd[3]
nam_sinh = cccd[4:6]
print("Mã tỉnh:", ma_tinh)
print("Giới tính:", gioi_tinh)
print("Năm sinh:", nam_sinh)


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
chuoi = input("Nhập chuỗi: ")
if chuoi == chuoi[::-1]:
    print(f"{chuoi} là chuỗi đối xứng")
else:
    print(f"{chuoi} là chuỗi không đối xứng")