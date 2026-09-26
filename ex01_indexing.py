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
journey = s[7:]
dao_nguoc = s[::-1]
moi_ky_tu_thu_2 = s[::2]

print("a) Lấy 'Journey':", journey)
print("b) Đảo ngược chuỗi:", dao_nguoc)
print("c) Lấy mỗi ký tự thứ 2:", moi_ky_tu_thu_2)


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 09
cccd = input("Nhập CCCD (12 chữ số): ")
ma_tinh = cccd[:2]
gioi_tinh = cccd[2]
nam_sinh = cccd[3:5]

print(f"Tỉnh: {ma_tinh}, Giới tính: {gioi_tinh}, Năm sinh: {nam_sinh}")


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
chuoi = input("Nhập chuỗi kiểm tra đối xứng: ")
chuoi_chuan_hoa = "".join(chuoi.lower().split())
is_palindrome = chuoi_chuan_hoa == chuoi_chuan_hoa[::-1]

print(f"'{chuoi}' đối xứng (palindrome): {is_palindrome}")
