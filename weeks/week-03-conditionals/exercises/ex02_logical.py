"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True    
# Viết if kiểm tra và in kết quả
tuoi = int(input("Nhap tuoi: "))
co_bang_lai = input("co bang lai (true/false): ")
khong_say = input("khong say (true/false): ")
if tuoi >= 18 and co_bang_lai == "true" and khong_say == "true":
    print("Du dieu kien lai xe")
else:
    print("Khong du dieu kien lai xe")

# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
canh_a = float(input("Nhap canh a: "))
canh_b = float(input("Nhap canh b: "))
canh_c = float(input("Nhap canh c: "))

if canh_a + canh_b > canh_c and canh_a + canh_c > canh_b and canh_b + canh_c > canh_a:
    if canh_a == canh_b == canh_c:
        print("Tam giac deu")
    elif canh_a == canh_b or canh_a == canh_c or canh_b == canh_c:
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")

# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
mat_khau = input("Nhap mat khau: ")
if len(mat_khau) >= 8 and any(c.isupper() for c in mat_khau) and any(c.islower() for c in mat_khau) and any(c.isdigit() for c in mat_khau):
    print("mat khau manh")
else:
    print("Mat khau yeu")

# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
nhap_n = int(input("Nhap so n: "))
if nhap_n % 3 == 0 and nhap_n % 5 == 0:
    print("FizzBuzz")
elif nhap_n % 3 == 0:
    print("Fizz")
elif nhap_n % 5 == 0:
    print("Buzz")
else:
    print(nhap_n)