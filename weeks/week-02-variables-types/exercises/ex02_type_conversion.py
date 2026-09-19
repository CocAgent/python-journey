"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_nguyen = int(so_text)   # Chuyển chuỗi "42" → số nguyên 42
ket_qua = so_nguyen + 8    # 42 + 8 = 50
print("TODO 1:", ket_qua)  # In ra: 50


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_nguyen = int(pi)           # int() cắt bỏ phần thập phân → 3
print("TODO 2:", pi_nguyen)   # In ra: 3


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("TODO 3:")
print("bool(0)       =", bool(0))        # False  → 0 là "rỗng"
print("bool(1)       =", bool(1))        # True   → khác 0
print('bool("")      =', bool(""))       # False  → chuỗi rỗng
print('bool("hello") =', bool("hello"))  # True   → chuỗi có nội dung
print("bool([])      =", bool([]))       # False  → danh sách rỗng
print("bool([1,2])   =", bool([1, 2]))   # True   → danh sách có phần tử


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("TODO 4:")
chieu_cao = float(input("Chieu cao (m), vi du 1.70: "))
can_nang = float(input("Can nang (kg), vi du 65: "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI của bạn là: {bmi:.1f}")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("TODO 5:")
tong_giay = int(input("Nhap so giay, vi du 3661: "))
gio = tong_giay // 3600          # Lấy số giờ
con_lai = tong_giay % 3600       # Số giây còn lại sau khi trừ giờ
phut = con_lai // 60             # Lấy số phút
giay = con_lai % 60              # Số giây còn lại
print(f"{gio} giờ {phut} phút {giay} giây")
