"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_int = int(so_text)
ket_qua = so_int + 8
print(f"TODO 1: {so_int} + 8 = {ket_qua}")


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_int = int(pi)
print(f"TODO 2: int({pi}) = {pi_int} (int() cắt bỏ phần thập phân, không làm tròn)")


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("TODO 3: Kiểm tra bool():")
gia_tri_kiem_tra = [0, 1, "", "hello", [], [1, 2]]
for gia_tri in gia_tri_kiem_tra:
    print(f"  bool({gia_tri!r}) = {bool(gia_tri)}")


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("\nTODO 4: Tính BMI")
chieu_cao = float(input("Nhập chiều cao (m, ví dụ 1.75): "))
can_nang = float(input("Nhập cân nặng (kg, ví dụ 70): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI: {bmi:.1f}")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("\nTODO 5: Đổi số giây sang giờ:phút:giây")
tong_so_giay = int(input("Nhập số giây (ví dụ 3661): "))
gio = tong_so_giay // 3600
phut = (tong_so_giay % 3600) // 60
giay = tong_so_giay % 60
print(f"{tong_so_giay} giây → {gio} giờ {phut} phút {giay} giây")
