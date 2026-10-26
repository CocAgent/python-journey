"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email = email.strip().lower()
print(email)

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
sentence = sentence.title()
print(sentence)
print(sentence.count("o"))
print(sentence.replace("python", "PYTHON"))

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
full_name = input("Nhập họ tên đầy đủ: ")
first_name = full_name.split()[0]
last_name = full_name.split()[-1]
print("Họ:", first_name)
print("Tên:", last_name)

# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
file_name = input("Nhập tên file: ")
if file_name.endswith((".py", ".txt", ".csv")):
    print("Tên file hợp lệ")
else:
    print("Tên file không hợp lệ")

# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Xác định offset dựa trên chữ hoa hay thường
            offset = ord('A') if char.isupper() else ord('a')
            # Dịch ký tự và đảm bảo vòng quanh bảng chữ cái
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char  # Giữ nguyên ký tự không phải chữ cái
    return result