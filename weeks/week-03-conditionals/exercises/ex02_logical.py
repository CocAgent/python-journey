"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True
print("=== TODO 1: Kiểm tra điều kiện lái xe ===")
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").strip().lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").strip().lower() == "y"

if tuoi >= 18 and co_bang_lai and khong_say:
    print("Đủ điều kiện lái xe an toàn!")
else:
    print("KHÔNG đủ điều kiện lái xe!")


# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
print("\n=== TODO 2: Phân loại tam giác ===")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Ba cạnh này KHÔNG tạo thành một tam giác hợp lệ.")


# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
print("\n=== TODO 3: Kiểm tra mật khẩu mạnh ===")
pw = input("Nhập mật khẩu cần kiểm tra: ")
du_do_dai = len(pw) >= 8
co_chu_hoa = any(c.isupper() for c in pw)
co_chu_thuong = any(c.islower() for c in pw)
co_chu_so = any(c.isdigit() for c in pw)

if du_do_dai and co_chu_hoa and co_chu_thuong and co_chu_so:
    print("Mật khẩu MẠNH!")
else:
    print("Mật khẩu CHƯA MẠNH. Yêu cầu: >= 8 ký tự, có chữ hoa, chữ thường và số.")


# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
print("\n=== TODO 4: FizzBuzz ===")
n = int(input("Nhập số nguyên n: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
