"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
Songuyen=int(so_text)
Songuyen=Songuyen+8
print(Songuyen)




# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_songuyen=int(pi)
print(pi_songuyen)


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("bool(0):", bool(0))          # False
print("bool(1):", bool(1))          # True
print('bool(""):', bool(""))        # False
print('bool("hello"):', bool("hello"))  # True
print("bool([]):", bool([]))        # False
print("bool([1,2]):", bool([1, 2])) # True

print("-" * 30)

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI của bạn: {bmi:.1f}")

print("-" * 30)


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
so_giay_nhap = int(input("Nhập số giây: "))
gio = so_giay_nhap // 3600
phut = (so_giay_nhap % 3600) // 60
giay = so_giay_nhap % 60
print(f"{gio} giờ {phut} phút {giay} giây")
