"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"
# Viết if kiểm tra và in kết quả
if tuoi >= 18 and co_bang_lai and khong_say:
    print("Đủ điều kiện lái xe\n")
else:
    if tuoi < 18:
        print("Chưa đủ điều kiện lái xe (cần đủ 18 tuổi)\n")
    elif not co_bang_lai:
        print("Chưa đủ điều kiện lái xe (cần có bằng lái)\n")
    else:
        print("Chưa đủ điều kiện lái xe (cần tỉnh táo)\n")

# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("đây là tam giác đều\n")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân\n")
    else:
        print("Đây là tam giác thường\n")
else:
    print("Không tạo thành tam giác\n")

# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
pw = input("Nhập mật khẩu: ")
du_dai = len(pw) >= 8
co_hoa = any(c.isupper() for c in pw)
co_thuong = any(c.islower() for c in pw)
co_so = any(c.isdigit() for c in pw)

if du_dai and co_hoa and co_thuong and co_so:
    print("Mật khẩu mạnh\n")
else:
    print("Mật khẩu yếu")
    if not du_dai:
        print("- Cần ít nhất 8 kí tự")
    if not co_hoa:
        print("- Cần có chữ in hoa")
    if not co_thuong:
        print("- Cần có chữ in thường")
    if not co_so:
        print("- Cần có số")
print("\n")
# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
n = int(input("Nhập số n: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)