"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"

# In ra ký tự đầu
print(s[0])

# In ra ký tự cuối (dùng index âm)
print(s[-1])

# In ra 5 ký tự đầu
print(s[:5])

# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s


# a) Lấy "Journey" từ s
print("a) Journey:", s[7:])

# b) Đảo ngược chuỗi s
print("b) Đảo ngược:", s[::-1])

# c) Lấy mỗi ký tự thứ 2 từ s
print("c) Mỗi ký tự thứ 2:", s[::2])


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
cccd = "001099012345"
tinh = cccd[:2]
gioi_tinh = cccd[2]
nam_sinh = cccd[3:5]  # hoặc cccd[3:6] nếu muốn ra "099" như ví dụ
print(f"Tỉnh: {tinh}, Giới tính: {gioi_tinh}, Năm sinh: {nam_sinh}")


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
# Nhập chuỗi
input_str = input("Nhập chuỗi để kiểm tra đối xứng: ")

# Kiểm tra có phải palindrome không
is_palindrome = input_str == input_str[::-1]

# In kết quả
print(f"Chuỗi '{input_str}' có phải là palindrome không? {is_palindrome}")
