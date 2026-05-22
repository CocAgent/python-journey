"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_2 = int(so_text) + 8
print(f"{so_text} + 8 = {so_2}")  

# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
int_pi = int(pi)
print(f"int({pi}) = {int_pi}")


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
bool_0 = bool(0)
bool_1 = bool(1)
bool_empty_str = bool("")
bool_hello = bool("hello")
bool_empty_list = bool([])
bool_list = bool([1,2])

print(f"bool(0) = {bool_0}")
print(f"bool(1) = {bool_1}")
print(f"bool('') = {bool_empty_str}")
print(f"bool('hello') = {bool_hello}")
print(f"bool([]) = {bool_empty_list}")
print(f"bool([1,2]) = {bool_list}")

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
cc= float(input("Chiều cao (m): "))
cn= float(input("Cân nặng (kg): "))
bmi = cn / (cc ** 2)
print(f"BMI = {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
giay = int(input("Nhập số giây: "))
gio = giay // 3600
phut = (giay % 3600) // 60
giay_con_lai = giay % 60
print(f"{giay} giây → {gio} giờ {phut} phút {giay_con_lai} giây")