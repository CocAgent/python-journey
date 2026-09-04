"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print("Email chuẩn hóa:", email.strip().lower())

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print("a) Title Case:", sentence.title())
print("b) Số lần 'o':", sentence.count("o"))
print("c) Thay 'python' thành 'PYTHON':", sentence.replace("python", "PYTHON"))

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ tên đầy đủ: ")
parts = ho_ten.split()
ho = parts[0]
ten = parts[-1]
print("Họ:", ho)
print("Tên:", ten)


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
ten_file = input("Nhập tên file: ")
if ten_file.endswith((".py", ".txt", ".csv")):
    print("Tên file hợp lệ.")
else:
    print("Tên file không hợp lệ. Phải kết thúc bằng .py, .txt, hoặc .csv.")

# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
text = input("Nhập chuỗi: ").lower()
shift = int(input("Bước dịch: "))
result = ""
for ch in text:
    if ch.isalpha():
        new_code = (ord(ch) - ord("a") + shift) % 26 + ord("a")
        result += chr(new_code)
    else:
        result += ch
print(f"Mã hóa: {result}")

