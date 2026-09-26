"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print(email.strip().lower())  # → user@example.com


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print(sentence.title())                        # → Hello World Python Programming
print(sentence.count("o"))                     # → 5
print(sentence.replace("python", "PYTHON"))    # → hello world PYTHON programming


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ và tên: ")
parts = ho_ten.split()
print(f"Họ: {parts[0]}, Tên: {parts[-1]}")

# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
filename = input("Nhập tên file: ")
if filename.endswith((".py", ".txt", ".csv")):
    print(f'"{filename}" hợp lệ → True')
else:
    print(f'"{filename}" không hợp lệ → False')


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
text = input("Chuỗi cần mã hóa: ")
shift = int(input("Số bước dịch: "))
result = []
for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    else:
        result.append(ch)
print("".join(result))
