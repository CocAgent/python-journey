
"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
print("TODO 1: Chuyen chuoi thanh so nguyen")

so_text = "42"
so = int(so_text)
print("Ket qua:", so + 8)
print()


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
print("TODO 2: Chuyen so thuc thanh so nguyen")

pi = 3.14159
print("Gia tri ban dau:", pi)
print("Sau khi chuyen:", int(pi))
print()


# TODO 3: Kiểm tra bool() của các giá trị sau
# bool(0), bool(1), bool(""), bool("hello")
# bool([]), bool([1,2])
print("TODO 3: Kiem tra gia tri Boolean")

print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("hello"):', bool("hello"))
print("bool([]):", bool([]))
print("bool([1, 2]):", bool([1, 2]))
print()


# TODO 4: Nhập chiều cao (m) và cân nặng (kg)
# BMI = cân_nặng / (chiều_cao ** 2)
# In BMI với 1 chữ số thập phân
print("TODO 4: Tinh chi so BMI")

chieucao = float(input("Nhap chieu cao (m): "))
cannang = float(input("Nhap can nang (kg): "))

bmi = cannang / (chieucao ** 2)

print(f"Chi so BMI cua ban la: {bmi:.1f}")
print()


# TODO 5 (Thử thách): Chuyển giây sang giờ:phút:giây
print("TODO 5: Chuyen doi thoi gian")

tonggiay = int(input("Nhap so giay: "))

gio = tonggiay // 3600
phut = (tonggiay % 3600) // 60
giay = tonggiay % 60

print(f"{gio} gio {phut} phut {giay} giay")
