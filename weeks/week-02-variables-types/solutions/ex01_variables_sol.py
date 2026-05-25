"""Lời giải Bài tập 02: Chuyển đổi kiểu dữ liệu"""

# TODO 1
so_text = "75"

so = int(so_text) + 25

print(f"{so_text} + 25 = {so}")  # 100


# TODO 2
pi = 9.8765

print(f"int({pi}) = {int(pi)}")  # 9


# TODO 3
print(f"bool(0) = {bool(0)}")               # False
print(f"bool(5) = {bool(5)}")               # True

print(f'bool("") = {bool("")}')             # False
print(f'bool("Python") = {bool("Python")}') # True

print(f"bool([]) = {bool([])}")             # False
print(f"bool([10, 20]) = {bool([10, 20])}") # True


# TODO 4
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print(f"Chỉ số BMI = {bmi:.2f}")


# TODO 5
tong_giay = int(input("Nhập tổng số giây: "))

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
