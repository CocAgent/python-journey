"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True
print("--- 1. Kiểm tra đủ điều kiện lái xe ---")
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"
# Viết if kiểm tra và in kết quả
if tuoi >= 18 and co_bang_lai and khong_say:
    print("=> Kết quả: ĐỦ điều kiện lái xe")
else:
    print("=> Kết quả: KHÔNG đủ điều kiện lái xe")


# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
print("\n--- 2. Phân loại tam giác ---")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Điều kiện tồn tại tam giác: 3 cạnh > 0 và tổng 2 cạnh bất kỳ > cạnh còn lại
la_tam_giac = a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

if not la_tam_giac:
    print("Ba cạnh KHÔNG tạo thành tam giác")
elif a == b == c:
    print("Loại tam giác: Tam giác ĐỀU")
elif a == b or b == c or a == c:
    print("Loại tam giác: Tam giác CÂN")
else:
    print("Loại tam giác: Tam giác THƯỜNG")


# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
print("\n--- 3. Kiểm tra mật khẩu mạnh ---")
pw = input("Nhập mật khẩu cần kiểm tra: ")

du_dai = len(pw) >= 8
co_chu_hoa = any(c.isupper() for c in pw)
co_chu_thuong = any(c.islower() for c in pw)
co_chu_so = any(c.isdigit() for c in pw)

if du_dai and co_chu_hoa and co_chu_thuong and co_chu_so:
    print("Độ bảo mật: Mật khẩu MẠNH")
else:
    print("Độ bảo mật: Mật khẩu YẾU")
    if not du_dai:
        print(" - Cần có ít nhất 8 ký tự")
    if not co_chu_hoa:
        print(" - Cần có ít nhất 1 chữ in hoa")
    if not co_chu_thuong:
        print(" - Cần có ít nhất 1 chữ thường")
    if not co_chu_so:
        print(" - Cần có ít nhất 1 chữ số")


# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
print("\n--- 4. Trò chơi FizzBuzz ---")
n = int(input("Nhập số nguyên n: "))

if n % 3 == 0 and n % 5 == 0:
    print("Kết quả: FizzBuzz")
elif n % 3 == 0:
    print("Kết quả: Fizz")
elif n % 5 == 0:
    print("Kết quả: Buzz")
else:
    print(f"Kết quả: {n}")
