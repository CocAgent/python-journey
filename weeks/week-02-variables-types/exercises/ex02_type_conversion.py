"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_int = int(42) + 8
print(so_int)
# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_int = int(pi)
print(pi_int)
# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1,2]))
# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao = float(input('Nhập chiều cao (m):'))
can_nang = float(input('Nhập cân nặng (kg):'))
bmi = can_nang / (chieu_cao ** 2)
print('BMI của bạn là:', round(bmi,1))
print(f'BMI của bạn là: {bmi:.1f}')
# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
a = int(input('Nhập số giây:'))
gio = a // 3600
phut = (a % 3600) // 60
giay = a % 60
print(f'{gio} giờ {phut} phút {giay} giây')