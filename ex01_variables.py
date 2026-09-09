"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
diem_tb = float(input("Nhập điểm trung bình: "))
dang_hoc = bool(input("Nhập trạng thái học (1: đang học, 0: không học): "))

print(f"Tên: {ten}, Kiểu: {type(ten)}")
print(f"Tuổi: {tuoi}, Kiểu: {type(tuoi)}")
print(f"Điểm trung bình: {diem_tb}, Kiểu: {type(diem_tb)}")
print(f"Đang học: {dang_hoc}, Kiểu: {type(dang_hoc)}")

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b 
# Gợi ý: Python cho phép a, b = b, aa=10
a=10
b=20
a,b=b,a,a==10
print(f"print sau hoan doi:a={a},b={b}")

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x=100
x+=10
print(f"x sau +=:{x}")
x-=5
print(f"x sau -=:{x}")
x*=2
print(f"x sau *=:{x}")
x//=3
print(f"x sau //=:{x}")

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
input_ho+=input("nhap ho:")
input_ten=input("nhap ten:")
input_tuoi=int(input("nhap tuoi:"))
print(f"Ho ten: {input_ho} {input_ten}, {input_tuoi} tuổi")
"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
input_8=int ("42")+8

# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_as_int = int(pi)

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
chieu_cao=float(input("Nhap chieu cao(m): "))
can_nang=float(input("Nhap can nang(kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chi so BMI cua ban la: {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
input_seconds=int(input("nhap so giay: "))
hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60
seconds = input_seconds % 60
print(f"{hours} giờ {minutes} phút {seconds} giây")
"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
input_num1=float(input("nhap so thu nhat: "))
input_num2=float(input("nhap so thu hai: "))

print(f"Tong: {input_num1 + input_num2}")
print(f"Hieu: {input_num1 - input_num2}")
print(f"Tich: {input_num1 * input_num2}")
print(f"Thuong: {input_num1 / input_num2}")

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
radius = float(input("Nhập bán kính hình tròn: "))
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Diện tích: {area}")
print(f"Chu vi: {circumference}")

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
original_price = float(input("Nhập giá gốc: "))
discount_percentage = float(input("Nhập phần trăm giảm giá: "))
discount_amount = original_price * discount_percentage / 100
final_price = original_price - discount_amount
print(f"Giá sau khi giảm: {final_price}")

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnd_amount = float(input("Nhập số tiền VNĐ: "))
exchange_rate = float(input("Nhập tỷ giá USD/VNĐ: "))
usd_amount = vnd_amount / exchange_rate
print(f"Số USD tương ứng: {usd_amount:.2f}")