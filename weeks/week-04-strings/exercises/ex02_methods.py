"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email_chuan = email.strip().lower()     # strip() bỏ khoảng trắng đầu/cuối, lower() chuyển thường
print(f"Email chuẩn hóa: {email_chuan}")


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
a = sentence.title()                    # Title Case: viết hoa chữ đầu mỗi từ
b = sentence.count("o")                # đếm số lần ký tự "o" xuất hiện
c = sentence.replace("python", "PYTHON")  # thay thế chuỗi con
print(f"a) Title Case:  {a}")
print(f"b) Số lần 'o':  {b}")
print(f"c) Thay python: {c}")


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ tên đầy đủ: ").strip()
phan = ho_ten.split()       # tách thành list các từ theo khoảng trắng
ho = phan[0]                # từ đầu tiên là họ
ten = phan[-1]              # từ cuối cùng là tên (kể cả tên đệm)
print(f"Họ:  {ho}")
print(f"Tên: {ten}")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
ten_file = input("Nhập tên file: ").strip()
# endswith() có thể nhận tuple — chỉ cần một đuôi khớp là True
if ten_file.endswith((".py", ".txt", ".csv")):
    print(f'"{ten_file}" là file hợp lệ (.py / .txt / .csv) ✅')
else:
    print(f'"{ten_file}" không phải file hợp lệ ❌')


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
van_ban = input("Nhập chuỗi để mã hóa Caesar: ")
shift = int(input("Nhập số bước dịch: "))

ket_qua = []
for ky_tu in van_ban:
    if ky_tu.isalpha():
        # Xác định điểm gốc: 'A' (65) cho chữ hoa, 'a' (97) cho chữ thường
        goc = ord("A") if ky_tu.isupper() else ord("a")
        # Dịch ký tự và quay vòng trong bảng chữ cái (26 chữ) bằng %
        ky_tu_moi = chr((ord(ky_tu) - goc + shift) % 26 + goc)
        ket_qua.append(ky_tu_moi)
    else:
        ket_qua.append(ky_tu)   # giữ nguyên ký tự không phải chữ cái

print(f"Kết quả mã hóa: {''.join(ket_qua)}")
