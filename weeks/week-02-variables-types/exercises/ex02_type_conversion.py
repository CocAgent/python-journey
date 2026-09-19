"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_int = int(so_text)
ket_qua_1 = so_int + 8
print(f"TODO 1: {so_int} + 8 = {ket_qua_1}")


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_int = int(pi)
print(f"TODO 2: int({pi}) = {pi_int}")


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("TODO 3:")
print("bool(0) ->", bool(0))
print("bool(1) ->", bool(1))
print('bool("") ->', bool(""))
print('bool("hello") ->', bool("hello"))
print("bool([]) ->", bool([]))
print("bool([1, 2]) ->", bool([1, 2]))


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("\nTODO 4: Tính chỉ số BMI")
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI của bạn là: {bmi:.1f}")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("\nTODO 5: Đổi số giây sang giờ:phút:giây")
so_giay = int(input("Nhập số giây: "))
gio = so_giay // 3600
phut = (so_giay % 3600) // 60
giay = so_giay % 60
print(f"{so_giay} giây -> {gio} giờ {phut} phút {giay} giây")
