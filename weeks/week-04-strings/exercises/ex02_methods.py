"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print("--- TODO 1: Chuẩn hóa email ---")
email_chuan_hoa = email.strip().lower()
print(f'Email gốc: "{email}"')
print(f'Email chuẩn hóa: "{email_chuan_hoa}"')


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print("\n--- TODO 2: Xử lý chuỗi với string methods ---")
# a) Title case
sentence_title = sentence.title()
# b) Đếm ký tự 'o'
so_chu_o = sentence.count("o")
# c) Thay thế từ
sentence_upper_python = sentence.replace("python", "PYTHON")

print(f'a) Title Case: "{sentence_title}"')
print(f'b) Số lần xuất hiện của "o": {so_chu_o}')
print(f'c) Thay "python" thành "PYTHON": "{sentence_upper_python}"')


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
print("\n--- TODO 3: Tách họ và tên ---")
ho_ten = input("Nhập họ và tên đầy đủ: ").strip()
cac_tu = ho_ten.split()
if len(cac_tu) >= 2:
    ho = cac_tu[0]
    ten = cac_tu[-1]
    print(f'Họ: "{ho}", Tên: "{ten}"')
elif len(cac_tu) == 1:
    print(f'Chỉ có tên: "{cac_tu[0]}"')
else:
    print("Bạn chưa nhập họ tên!")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
print("\n--- TODO 4: Kiểm tra tên file hợp lệ ---")
ten_file = input("Nhập tên file: ").strip()
duoi_hop_le = (".py", ".txt", ".csv")
hop_le = ten_file.endswith(duoi_hop_le)
print(f'Tên file "{ten_file}" có đuôi hợp lệ (.py, .txt, .csv): {hop_le}')


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
print("\n--- TODO 5: Mã hóa Caesar ---")
van_ban = input("Nhập chuỗi cần mã hóa: ")
shift_input = input("Nhập số bước dịch (shift): ").strip()
shift = int(shift_input) if shift_input.lstrip("-").isdigit() else 3

ket_qua = []
for ky_tu in van_ban:
    if "a" <= ky_tu <= "z":
        # Dịch trong khoảng chữ thường 'a' -> 'z'
        ma_moi = chr((ord(ky_tu) - ord("a") + shift) % 26 + ord("a"))
        ket_qua.append(ma_moi)
    elif "A" <= ky_tu <= "Z":
        # Dịch trong khoảng chữ hoa 'A' -> 'Z'
        ma_moi = chr((ord(ky_tu) - ord("A") + shift) % 26 + ord("A"))
        ket_qua.append(ma_moi)
    else:
        # Ký tự khoảng trắng, số, dấu câu giữ nguyên
        ket_qua.append(ky_tu)

chuoi_ma_hoa = "".join(ket_qua)
print(f'Chuỗi sau khi mã hóa Caesar (shift={shift}): "{chuoi_ma_hoa}"')
