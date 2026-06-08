"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so = int(so_text) + 8
print(f"int({so_text}) + 8 = {so}")

# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_int = int(pi)
print(f"int({pi}) = {pi_int}")

# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f'bool("") = {bool("")}')
print(f'bool("hello") = {bool("hello")}')
print(f"bool([]) = {bool([])}")
print(f"bool([1,2]) = {bool([1,2])}")

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao = float(input("Nhập chiều cao của bạn (m, ví dụ 1.70): "))
can_nang = float(input("Nhập cân nặng của bạn (kg, ví dụ 65.5): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI của bạn là: {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
tong_giay = int(input("Nhập tổng số giây: "))
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
