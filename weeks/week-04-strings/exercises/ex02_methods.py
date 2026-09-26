"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print("--- 1. Chuẩn hóa email ---")
email_chuan_hoa = email.strip().lower()
print(f"Email gốc: '{email}'")
print(f"Email sau chuẩn hóa: '{email_chuan_hoa}'")


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print("\n--- 2. Thao tác với câu ---")
sentence_title = sentence.title()
so_lan_o = sentence.count("o")
sentence_replaced = sentence.replace("python", "PYTHON")

print(f"a) Title Case: '{sentence_title}'")
print(f"b) Số lần xuất hiện của chữ 'o': {so_lan_o}")
print(f"c) Thay 'python' thành 'PYTHON': '{sentence_replaced}'")


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
print("\n--- 3. Tách họ và tên ---")
ho_ten = input("Nhập họ tên đầy đủ: ").strip()
parts = ho_ten.split()
if parts:
    ho = parts[0]
    ten = parts[-1]
    print(f"Họ: {ho}")
    print(f"Tên: {ten}")
else:
    print("Chưa nhập họ tên hợp lệ")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
print("\n--- 4. Kiểm tra định dạng file ---")
ten_file = input("Nhập tên file (kèm phần mở rộng): ").strip()
is_valid_ext = ten_file.endswith((".py", ".txt", ".csv"))
if is_valid_ext:
    print(f"Tệp '{ten_file}' HỢP LỆ (thuộc định dạng .py, .txt, .csv)")
else:
    print(f"Tệp '{ten_file}' KHÔNG HỢP LỆ (chỉ chấp nhận .py, .txt, .csv)")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
print("\n--- 5. Mã hóa Caesar ---")
van_ban = input("Nhập văn bản cần mã hóa: ")
shift = int(input("Nhập số bước dịch (shift): "))

ket_qua = []
for ky_tu in van_ban:
    if ky_tu.isupper():
        # Ký tự in hoa: A-Z
        moi = chr((ord(ky_tu) - ord('A') + shift) % 26 + ord('A'))
        ket_qua.append(moi)
    elif ky_tu.islower():
        # Ký tự in thường: a-z
        moi = chr((ord(ky_tu) - ord('a') + shift) % 26 + ord('a'))
        ket_qua.append(moi)
    else:
        # Giữ nguyên khoảng trắng và ký tự đặc biệt
        ket_qua.append(ky_tu)

van_ban_ma_hoa = "".join(ket_qua)
print(f"Văn bản sau mã hóa Caesar: {van_ban_ma_hoa}")
