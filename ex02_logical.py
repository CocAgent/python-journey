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

if tuoi >=18 and co_bang_lai and khong_say:
    print("du dieu kien lai xe")
else:
    print("khong du dieu kien lai xe")

# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?

a = float(input("nhap canh a: "))
b = float(input("nhap canh b: "))
c = float(input("nhap canh c: "))

if (a +b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("tam giac deu")
    elif a == b or b == c or a == c:
        print("tam giac can")
    else:
        print("tam giac thuong")
else:
    print("khong phai la tam giac")

# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)

pw = input("nhap mat khau: ")

dai_du = len(pw) >= 8
co_hoa = any(c.isupper() for c in pw)
co_thuong = any(c.islower() for c in pw)
co_so = any(c.isdigit() for c in pw)

if dai_du and co_hoa and co_thuong and co_so:
    print("mat khau manh")
else:
    print("mat khau yeu")

# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó

n = int(input("nhap so n: "))

if n % 3 == 0 and n % 5 == 0:
    print("fizzbuzz")
elif n % 3 == 0:
    print("fizz")
elif n % 5 == 0:
    print("buzz")
else:
    print(n)
