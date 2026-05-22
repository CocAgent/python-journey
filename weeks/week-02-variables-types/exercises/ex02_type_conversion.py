"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so = int(so_text) + 8
print(f"{so_text} + 8 = {so}")
print("-" * 30)


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
print(f"int({pi}) = {int(pi)}")
print("-" * 30)


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f'bool("") = {bool("")}')
print(f'bool("hello") = {bool("hello")}')
print(f"bool([]) = {bool([])}")
print(f"bool([1,2]) = {bool([1,2])}")
print("-" * 30)


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao_str = input("Nhập chiều cao của bạn (m): ")
can_nang_str = input("Nhập cân nặng của bạn (kg): ")

chieu_cao = float(chieu_cao_str)
can_nang = float(can_nang_str)

bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI của bạn là: {bmi:.1f}")
print("-" * 30)


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
tong_giay_str = input("Nhập tổng số giây: ")
tong_giay = int(tong_giay_str)

gio = tong_giay // 3600
giay_con_lai_sau_gio = tong_giay % 3600
phut = giay_con_lai_sau_gio // 60
giay = giay_con_lai_sau_gio % 60

print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
print("\nChúc mừng! Bạn đã hoàn thành bài tập về chuyển đổi kiểu dữ liệu!")
