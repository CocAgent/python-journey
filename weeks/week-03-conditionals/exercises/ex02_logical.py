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
    print("Đủ điều kiện lái xe")
else:
    print("Không đủ điều kiện lái xe")


# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))

# Điều kiện tam giác: độ dài > 0 và tổng 2 cạnh bất kỳ > cạnh còn lại
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Không hợp lệ: Không tạo thành tam giác")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
else:
    print("Tam giác thường")


# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
pw = input("Nhập mật khẩu: ")

dai_hop_le = len(pw) >= 8
co_chu_hoa = any(c.isupper() for c in pw)
co_chu_thuong = any(c.islower() for c in pw)
co_chu_so = any(c.isdigit() for c in pw)

if dai_hop_le and co_chu_hoa and co_chu_thuong and co_chu_so:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")


# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
n = int(input("Nhập số n: "))

if n % 3 == 0 and n % 5 == 0:  # Chia hết cho cả 3 và 5 (tức n % 15 == 0)
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
