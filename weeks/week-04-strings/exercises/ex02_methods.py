"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email_chuan_hoa = email.strip().lower()
print("Email chuẩn hóa:", email_chuan_hoa)


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print("a) Title Case:", sentence.title())
print("b) Số lần xuất hiện 'o':", sentence.count("o"))
print("c) Thay 'python' thành 'PYTHON':", sentence.replace("python", "PYTHON"))


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ tên đầy đủ: ")
cac_tu = ho_ten.strip().split()
if cac_tu:
    ho = cac_tu[0]
    ten = cac_tu[-1]
    print(f'Họ: "{ho}", Tên: "{ten}"')


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
ten_file = input("Nhập tên file: ")
la_hop_le = ten_file.endswith((".py", ".txt", ".csv"))
print(f"Tên file '{ten_file}' hợp lệ (.py, .txt, .csv): {la_hop_le}")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
van_ban = input("Nhập chuỗi cần mã hóa: ")
shift = int(input("Nhập số bước dịch (shift): "))

ket_qua = []
for ky_tu in van_ban:
    if ky_tu.isalpha():
        goc = ord("a") if ky_tu.islower() else ord("A")
        ky_tu_moi = chr((ord(ky_tu) - goc + shift) % 26 + goc)
        ket_qua.append(ky_tu_moi)
    else:
        ket_qua.append(ky_tu)

chuoi_ma_hoa = "".join(ket_qua)
print("Chuỗi sau khi mã hóa Caesar:", chuoi_ma_hoa)

