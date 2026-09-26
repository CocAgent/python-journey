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
    print('Du dieu kien lai xe')
else:
    print('Khong du dieu kien lai xe')
# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
a = int(input('Nhap canh a:'))
b = int(input('Nhap canh b:'))
c = int(input('Nhap canh c:'))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Tam giac deu')
    elif a == b or a == c or b == c:
        print('Tam giac can')
    else:
        print('Tam giac thuong')
else:
    print('Giac ngo khong phai tam giac')
# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
pw = input('Nhap mat khau:')
Do_dai_pw = len(pw) >= 8
Co_chu_hoa = any(c.isupper() for c in pw)
Co_chu_thuong = any(c.islower() for c in pw)
Co_So = any(c.isdigit() for c in pw)
if Do_dai_pw and Co_chu_hoa and Co_chu_thuong and Co_So:
    print('Mat khau manh')
else:
    print('Mat khau yeu')
# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
n = int(input('Nhap n:'))
if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)