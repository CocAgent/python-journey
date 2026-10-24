"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
ket_qua = 2024 + 1000
print(f"2024 + 1000 = {ket_qua}")


# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
so_tien = 150_000
gia_ca_phe = 35_000
so_ly = 3
tien_con_lai = so_tien - (gia_ca_phe * so_ly)
print(f"Số tiền còn lại: {tien_con_lai:,} VNĐ")


# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
pi = 3.14159
ban_kinh = 7
dien_tich = pi * (ban_kinh ** 2)
print(f"Diện tích hình tròn (r = {ban_kinh}): {dien_tich:.2f}")


# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
tong_keo = 100
so_nguoi = 7
moi_nguoi = tong_keo // so_nguoi
so_keo_du = tong_keo % so_nguoi
print(f"Mỗi người được: {moi_nguoi} viên kẹo")
print(f"Còn dư: {so_keo_du} viên kẹo")


# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
do_c = 37
do_f = do_c * 9 / 5 + 32
print(f"{do_c}°C = {do_f}°F")
