"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"

print("=== TODO 1 ===")
print(f"Ký tự đầu  : {s[0]}")       # 'P'
print(f"Ký tự cuối : {s[-1]}")      # 'y'  (dùng index âm)
print(f"5 ký tự đầu: {s[:5]}")      # 'Pytho'


# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s

print("\n=== TODO 2 ===")
print(f"a) Journey       : {s[7:]}")      # "Journey"
print(f"b) Đảo ngược     : {s[::-1]}")   # "yenruoJ nohtyP"
print(f"c) Mỗi ký tự thứ 2: {s[::2]}")   # "Pto ore"


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099

print("\n=== TODO 3 ===")
cccd = input("Nhập số CCCD (12 chữ số): ").strip()

ma_tinh = cccd[:3]       # 3 số đầu là mã tỉnh/thành phố
gioi_tinh = cccd[3]      # số thứ 4 là mã giới tính
nam_sinh = cccd[4:6]     # 2 số tiếp là 2 chữ số cuối của năm sinh

print(f"Mã tỉnh   : {ma_tinh}")
print(f"Giới tính : {gioi_tinh}  (0/2 = nam, 1/3 = nữ)")
print(f"Năm sinh  : 19{nam_sinh} hoặc 20{nam_sinh}")


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]

print("\n=== TODO 4 (Palindrome) ===")
chuoi = input("Nhập chuỗi cần kiểm tra: ").strip().lower()

if chuoi == chuoi[::-1]:
    print(f'"{chuoi}" → Palindrome ✅ (đọc xuôi ngược giống nhau)')
else:
    print(f'"{chuoi}" → Không phải palindrome ❌')
