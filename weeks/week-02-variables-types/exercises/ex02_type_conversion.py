"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
ket_qua = int(so_text) + 8
print(f"Ket qua: {ket_qua}")


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_nguyen = int(pi)
print(f"int(pi) = {pi_nguyen}")


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1, 2]))


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao = float(input("Chieu cao (m): ").strip().replace(",", "."))
can_nang = float(input("Can nang (kg): ").strip().replace(",", "."))
# Người dùng hay gõ 175 (cm) thay vì 1.75 (m) -> tự đổi sang mét
if chieu_cao > 3:
    chieu_cao = chieu_cao / 100
if chieu_cao <= 0 or can_nang <= 0:
    print("Chieu cao va can nang phai lon hon 0")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"BMI: {bmi:.1f}")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
tong_giay = int(input("Tong so giay: ").strip())
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giay -> {gio} gio {phut} phut {giay} giay")
