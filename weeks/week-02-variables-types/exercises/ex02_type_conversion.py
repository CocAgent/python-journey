"""Lời giải Bài tập 02: Chuyển đổi kiểu dữ liệu"""

# TODO 1
so_text = "42"
so = int(so_text) + 8
print(f"{so_text} + 8 = {so}")  # 50

# TODO 2
pi = 3.14159
print(f"int({pi}) = {int(pi)}")  # 3

# TODO 3
print(f"bool(0) = {bool(0)}")          # False
print(f"bool(1) = {bool(1)}")          # True
print(f'bool("") = {bool("")}')        # False
print(f'bool("hello") = {bool("hello")}')  # True
print(f"bool([]) = {bool([])}")        # False
print(f"bool([1,2]) = {bool([1,2])}")  # True

# TODO 4
chieu_cao = float(input("Chiều cao (m): "))
can_nang = float(input("Cân nặng (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI = {bmi:.1f}")

# TODO 5
tong_giay = int(input("Nhập số giây: "))
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
