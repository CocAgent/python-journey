"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print("--- 1. Indexing cơ bản ---")
print(f"Ký tự đầu: '{s[0]}'")
print(f"Ký tự cuối: '{s[-1]}'")
print(f"5 ký tự đầu: '{s[:5]}'")


# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
print("\n--- 2. Slicing chuỗi ---")
journey = s[7:]
dao_nguoc = s[::-1]
moi_ky_tu_thu_2 = s[::2]

print(f"a) Cắt 'Journey': '{journey}'")
print(f"b) Đảo ngược chuỗi: '{dao_nguoc}'")
print(f"c) Mỗi ký tự thứ 2: '{moi_ky_tu_thu_2}'")


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
print("\n--- 3. Tách thông tin CCCD ---")
cccd = input("Nhập CCCD (12 chữ số): ").strip()
if len(cccd) >= 5:
    ma_tinh = cccd[:2]
    gioi_tinh = cccd[2]
    nam_sinh = cccd[3:5]
    print(f"Mã tỉnh (2 số đầu): {ma_tinh}")
    print(f"Mã thế kỷ/giới tính (số thứ 3): {gioi_tinh}")
    print(f"2 số cuối năm sinh: {nam_sinh}")
else:
    print("Mã CCCD không hợp lệ (phải có ít nhất 5 chữ số)")


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
print("\n--- 4. Kiểm tra chuỗi đối xứng (Palindrome) ---")
chuoi_nhap = input("Nhập chuỗi cần kiểm tra: ")
chuoi_chuan_hoa = "".join(chuoi_nhap.lower().split())
is_palindrome = chuoi_chuan_hoa == chuoi_chuan_hoa[::-1]

print(f"Chuỗi '{chuoi_nhap}' có đối xứng không? {is_palindrome}")
