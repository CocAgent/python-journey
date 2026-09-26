"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print("--- TODO 1: Indexing cơ bản ---")
print(f"Chuỗi ban đầu: '{s}'")
print(f"Ký tự đầu: '{s[0]}'")
print(f"Ký tự cuối (dùng index âm): '{s[-1]}'")
print(f"5 ký tự đầu: '{s[:5]}'")


# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
print("\n--- TODO 2: Slicing nâng cao ---")
journey = s[7:]
s_dao_nguoc = s[::-1]
ky_tu_cach = s[::2]

print(f'a) Lấy "Journey": "{journey}"')
print(f'b) Đảo ngược chuỗi: "{s_dao_nguoc}"')
print(f'c) Mỗi ký tự thứ 2: "{ky_tu_cach}"')


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
print("\n--- TODO 3: Phân tích số CCCD ---")
cccd = input("Nhập CCCD (12 chữ số): ").strip()
if len(cccd) == 12:
    ma_tinh = cccd[:2]
    gioi_tinh = cccd[2]
    nam_sinh = cccd[3:5]  # 2 số tiếp theo theo mô tả đề bài
    print(f"Tỉnh: {ma_tinh}, Giới tính: {gioi_tinh}, Năm sinh: {nam_sinh}")
else:
    print("Lưu ý: Bạn cần nhập chuỗi có đúng 12 chữ số!")


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
print("\n--- TODO 4: Kiểm tra chuỗi đối xứng (Palindrome) ---")
chuoi_nhap = input("Nhập chuỗi cần kiểm tra: ")
# Chuẩn hóa: loại bỏ khoảng trắng thừa và chuyển về chữ thường
chuoi_chuan_hoa = "".join(chuoi_nhap.lower().split())
la_palindrome = (chuoi_chuan_hoa == chuoi_chuan_hoa[::-1])
print(f'Chuỗi "{chuoi_nhap}" đối xứng (Palindrome): {la_palindrome}')
