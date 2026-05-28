"""Lời giải Bài tập 02: Toán tử logic"""

# TODO 1
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"
if tuoi >= 18 and co_bang_lai and khong_say:
    print("Được phép lái xe!")
else:
    print("Không đủ điều kiện lái xe.")

# TODO 2
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")

# TODO 3
pw = input("Nhập mật khẩu: ")
du_dai = len(pw) >= 8
co_hoa = any(c.isupper() for c in pw)
co_thuong = any(c.islower() for c in pw)
co_so = any(c.isdigit() for c in pw)
if du_dai and co_hoa and co_thuong and co_so:
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu! Cần: >=8 ký tự, chữ hoa, chữ thường, số")

# TODO 4
n = int(input("Nhập số: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
