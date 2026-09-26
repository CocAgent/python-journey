"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
clean_email = email.strip().lower()
print("Email chuẩn hóa:", clean_email)


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
title_case = sentence.title()
count_o = sentence.count("o")
replaced = sentence.replace("python", "PYTHON")

print("a) Title Case:", title_case)
print("b) Số lần xuất hiện của 'o':", count_o)
print("c) Thay thế 'python':", replaced)


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ tên đầy đủ: ")
cac_tu = ho_ten.split()
if cac_tu:
    ho = cac_tu[0]
    ten = cac_tu[-1]
    print(f'Họ: "{ho}", Tên: "{ten}"')


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
ten_file = input("Nhập tên file: ")
hop_le = ten_file.endswith((".py", ".txt", ".csv"))
print(f"File '{ten_file}' hợp lệ (.py, .txt, .csv): {hop_le}")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
van_ban = input("Nhập chuỗi cần mã hóa Caesar: ")
shift = int(input("Nhập số bước dịch (shift): "))

ket_qua_caesar = []
for ky_tu in van_ban:
    if ky_tu.isalpha():
        goc = ord("a") if ky_tu.islower() else ord("A")
        ky_tu_moi = chr((ord(ky_tu) - goc + shift) % 26 + goc)
        ket_qua_caesar.append(ky_tu_moi)
    else:
        ket_qua_caesar.append(ky_tu)

print("Chuỗi sau mã hóa Caesar:", "".join(ket_qua_caesar))
