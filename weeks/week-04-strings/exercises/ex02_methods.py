"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email_clean = email.strip().lower()
print(f"Email chuẩn hóa: {email_clean}")


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print(f"a) Title Case: {sentence.title()}")
print(f"b) Số lần chữ 'o': {sentence.count('o')}")
print(f"c) Thay thế: {sentence.replace('python', 'PYTHON')}")


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
full_name = input("Nhập họ tên đầy đủ: ").strip()
parts = full_name.split()
if parts:
    ho = parts[0]
    ten = parts[-1]
    print(f"Họ: {ho}, Tên: {ten}")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
filename = input("Nhập tên file: ").strip()
is_valid = filename.endswith((".py", ".txt", ".csv"))
print(f"Tên file hợp lệ: {is_valid}")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
plain_text = input("Nhập chuỗi cần mã hóa Caesar: ")
shift = int(input("Nhập số bước dịch (shift): "))

encrypted = []
for char in plain_text:
    if char.isalpha():
        base = ord('a') if char.islower() else ord('A')
        new_char = chr((ord(char) - base + shift) % 26 + base)
        encrypted.append(new_char)
    else:
        encrypted.append(char)

print(f"Chuỗi sau mã hóa: {''.join(encrypted)}")
