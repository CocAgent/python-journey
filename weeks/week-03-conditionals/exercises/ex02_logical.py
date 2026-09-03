"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"
if tuoi >= 18 and co_bang_lai and khong_say:
    print("Đủ điều kiện lái xe")
else:
    print("Không đủ điều kiện lái xe")

# TODO 2: Phân loại tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không tạo thành tam giác")

# TODO 3: Kiểm tra mật khẩu mạnh
pw = input("Nhập mật khẩu: ")
co_hoa = any(c.isupper() for c in pw)
co_thuong = any(c.islower() for c in pw)
co_so = any(c.isdigit() for c in pw)
if len(pw) >= 8 and co_hoa and co_thuong and co_so:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")

# TODO 4 (Thử thách): FizzBuzz
n = int(input("Nhập số: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
