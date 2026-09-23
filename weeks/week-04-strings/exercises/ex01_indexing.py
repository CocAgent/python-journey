"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print("Ký tự đầu:", s[0])
print("Ký tự cuối:", s[-1])
print("5 ký tự đầu:", s[:5])

# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
print("Lấy 'Journey':", s[7:14])
print("Đảo ngược chuỗi:", s[::-1])
print("Mỗi ký tự thứ 2:", s[::2])


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
CCCD = input("Nhập CCCD (12 chữ số): ")
if len(CCCD) == 12 and CCCD.isdigit():
    ma_tinh = CCCD[:2]
    gioi_tinh = CCCD[2]
    nam_sinh = CCCD[3:6]
    print("Mã tỉnh:", ma_tinh)
    print("Giới tính:", gioi_tinh)
    print("Năm sinh:", nam_sinh)
else:
    print("CCCD không hợp lệ.")

# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
s = input("Nhập chuỗi: ")
if s == s[::-1]:
    print("Chuỗi đối xứng.")
else:
    print("Chuỗi không đối xứng.")