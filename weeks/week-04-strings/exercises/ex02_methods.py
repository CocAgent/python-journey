"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "

normalized_email = email.strip().lower()
print(normalized_email)

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
# a) Chuyển thành Title Case
title_case = sentence.title()
print("Title Case:", title_case)

# b) Đếm số lần chữ "o" xuất hiện
count_o = sentence.count('o')
print("Số lần chữ 'o':", count_o)

# c) Thay "python" thành "PYTHON"
replaced_sentence = sentence.replace("python", "PYTHON")
print("Thay thế:", replaced_sentence)

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
full_name = input("Nhập họ tên đầy đủ: ")
name_parts = full_name.split()
if len(name_parts) >= 2:
    last_name = name_parts[0]
    first_name = name_parts[-1]
    print(f"Họ: {last_name}, Tên: {first_name}")
else:
    print("Vui lòng nhập họ tên đầy đủ.")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
file_name = input("Nhập tên file: ")
valid_extensions = (".py", ".txt", ".csv")
if file_name.endswith(valid_extensions):
    print(f"Tên file '{file_name}' hợp lệ.")
else:
    print(f"Tên file '{file_name}' không hợp lệ.")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
input_str = input("Nhập chuỗi để mã hóa: ")
shift_str = input("Nhập số bước dịch (shift): ")

# Kiểm tra và chuyển đổi shift thành số nguyên
try:
    shift = int(shift_str)
except ValueError:
    print("Vui lòng nhập số hợp lệ cho shift.")
    exit()

encrypted_str = ""
for char in input_str:
    if 'a' <= char <= 'z':
        # Xử lý chữ thường
        shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        # Xử lý chữ hoa
        shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    else:
        # Giữ nguyên các ký tự khác (số, khoảng trắng, ký tự đặc biệt)
        shifted_char = char
    encrypted_str += shifted_char

print("Chuỗi đã mã hóa:", encrypted_str)
