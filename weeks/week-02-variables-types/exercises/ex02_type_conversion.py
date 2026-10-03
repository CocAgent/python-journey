"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"

so_nguyen = int(so_text) + 8
print("Ket qua:", so_nguyen)

# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159

pi_int = int(pi)
print("pi sau khi chuyen sang int:", pi_int)

# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])

print("bool(0):", bool(0))              # False (số 0 là False)
print("bool(1):", bool(1))              # True (số khác 0 là True)
print('bool(""):', bool(""))            # False (chuỗi rỗng là False)
print('bool("hello"):', bool("hello"))  # True (chuỗi có ký tự là True)
print("bool([]):", bool([]))            # False (danh sách rỗng là False)
print("bool([1, 2]):", bool([1, 2]))    # True (danh sách có phần tử là True)

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùngi
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân

chieu_cao = float(input("Nhap chieu cao (m): "))
can_nang = float(input("Nhap can nang (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI cua ban: {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"

so_giay = int(input("Nhap so giay: "))
gio = so_giay // 3600
phut = (so_giay % 3600) // 60
giay = so_giay % 60
print(f"{so_giay} giay -> {gio} gio {phut} phut {giay} giay")