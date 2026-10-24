"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print(f"Ký tự đầu:    {s[0]}")       # 'P'
print(f"Ký tự cuối:   {s[-1]}")      # 'y' — dùng index âm
print(f"5 ký tự đầu:  {s[:5]}")      # 'Pytho'


# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s
a = s[7:]           # "Journey" bắt đầu từ index 7
b = s[::-1]         # đảo ngược: bước -1 đi từ cuối về đầu
c = s[::2]          # mỗi ký tự thứ 2 (step = 2)
print(f"a) Journey:         {a}")
print(f"b) Đảo ngược:       {b}")
print(f"c) Mỗi ký tự thứ 2: {c}")


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
cccd = input("Nhập số CCCD (12 chữ số): ").strip()
ma_tinh = cccd[:2]          # 2 ký tự đầu
gioi_tinh = cccd[2]         # ký tự thứ 3 (index 2)
nam_sinh = cccd[3:5]        # 2 ký tự tiếp theo (index 3-4)
print(f"Mã tỉnh:    {ma_tinh}")
print(f"Giới tính:  {gioi_tinh}")
print(f"Năm sinh:   {nam_sinh}")


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
chuoi = input("Nhập chuỗi kiểm tra palindrome: ").strip().lower()
# Bỏ khoảng trắng để kiểm tra câu như "Never odd or even"
chuan_hoa = "".join(chuoi.split())
if chuan_hoa == chuan_hoa[::-1]:
    print(f'"{chuoi}" là chuỗi đối xứng (palindrome) ✅')
else:
    print(f'"{chuoi}" không phải chuỗi đối xứng ❌')
