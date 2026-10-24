"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_nguyen = int(so_text)        # "42" (str) → 42 (int)
ket_qua = so_nguyen + 8         # 42 + 8 = 50
print("TODO 1:", ket_qua)       # 50


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_int = int(pi)                # float → int: cắt phần thập phân (không làm tròn)
print("TODO 2:", pi_int)        # 3


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("TODO 3:")
print("bool(0)      ->", bool(0))        # False  — so 0 la falsy
print("bool(1)      ->", bool(1))        # True   — so khac 0 la truthy
print('bool("")     ->', bool(""))       # False  — chuoi rong la falsy
print('bool("hello")->', bool("hello")) # True   — chuoi co noi dung la truthy
print("bool([])     ->", bool([]))       # False  — danh sach rong la falsy
print("bool([1,2])  ->", bool([1, 2]))   # True   — danh sach co phan tu la truthy


# TODO 4: Nhap chieu cao (m) va can nang (kg) tu nguoi dung
# Tinh BMI = can_nang / (chieu_cao ** 2)
# In ra BMI voi 1 chu so thap phan
chieu_cao = float(input("Nhap chieu cao (m): "))   # input() tra ve str -> can float()
can_nang = float(input("Nhap can nang (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"TODO 4: BMI cua ban la {bmi:.1f}")         # :.1f -> 1 chu so thap phan


# TODO 5 (Thu thach): Nhap so giay, chuyen sang gio:phut:giay
# Vi du: 3661 giay -> "1 gio 1 phut 1 giay"
tong_giay = int(input("Nhap so giay: "))
gio = tong_giay // 3600          # lay phan nguyen cua tong / 3600
con_lai = tong_giay % 3600       # so giay con lai sau khi bo gio
phut = con_lai // 60             # lay phan nguyen cua phan con lai / 60
giay = con_lai % 60              # so giay le cuoi cung
print(f"TODO 5: {gio} gio {phut} phut {giay} giay")
