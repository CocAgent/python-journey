"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print(f"email chuan hoa: {email.strip().lower()}")

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print(f"title case: {sentence.title()}")
print(f"so lan xuat hien cua 'o': {sentence.count('o')}")
print(f"thay 'python' thanh 'PYTHON': {sentence.replace('python', 'PYTHON')}")

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_tenh = input("Nhap ho ten day du: ")
ho = ho_tenh.split()[0]
ten = ho_tenh.split()[-1]
print(f"Ho: {ho}, Ten: {ten}")

# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()

filename = input("Nhap ten file: ")
if filename.endswith((".py", ".txt", ".csv")):
    print("Ten file hop le")
else:
    print("Ten file khong hop le")

# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
string = input("Nhap chuoi: ")
shift = int(input("Nhap so buoc dich: "))

result = ""
for char in string:
    if char.isalpha():
        base = ord('a') if char.islower() else ord('A')
        result += chr((ord(char) - base + shift) % 26 + base)
    else:
        result += char

print(f"Chuoi ma hoa: {result}")
