"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print(email.strip().lower())  
print(email.strip().lower())    

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print(sentence.title())
print(sentence.count("o"))
print(sentence.replace("python", "PYTHON"))

print(sentence.title())
print(sentence.count("o"))
print(sentence.replace("python", "PYTHON"))




# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing

ho_ten = input("Nhập họ tên: ").strip()
cac_tu = ho_ten.split()
print("Họ:", cac_tu[0])
print("Tên:", cac_tu[-1])



# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()

filename = input("Nhập tên file: ").strip()
if filename.endswith((".py", ".txt", ".csv")):
    print("Tên file hợp lệ")
else:
    print("Tên file không hợp lệ")



# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
