"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# ============================================================
# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
# ============================================================
print("=== TODO 1: Tính toán cơ bản ===")  # In tiêu đề ra màn hình

# input() = hỏi người dùng gõ vào một giá trị
# float() = chuyển chữ người dùng gõ thành số thực (có thể có dấu phẩy)
# Vì input() luôn trả về CHỮ, nên phải bọc bằng float() để tính toán được
a = float(input("Nhập số thứ nhất: "))   # Hỏi số 1, lưu vào biến a
b = float(input("Nhập số thứ hai: "))    # Hỏi số 2, lưu vào biến b

# f"..." là f-string: cho phép nhúng biến trực tiếp vào chuỗi bằng {}
# Ví dụ: nếu a=10, b=3 thì in ra "Tổng: 10 + 3 = 13"
print(f"Tổng:   {a} + {b} = {a + b}")       # Phép cộng
print(f"Hiệu:   {a} - {b} = {a - b}")       # Phép trừ
print(f"Tích:   {a} × {b} = {a * b}")       # Phép nhân (* là dấu nhân)

# Kiểm tra b có bằng 0 không trước khi chia
# Vì toán học không cho phép chia cho 0, Python cũng sẽ bị lỗi nếu b = 0
if b != 0:                                               # Nếu b KHÁC 0
    print(f"Thương: {a} ÷ {b} = {a / b:.2f}")           # :.2f = làm tròn 2 số thập phân
else:                                                    # Nếu b = 0
    print("Thương: Không thể chia cho 0!")               # Thông báo lỗi thân thiện


# ============================================================
# TODO 2: Nhập bán kính hình tròn, tính và in diện tích, chu vi
# ============================================================
print("\n=== TODO 2: Hình tròn ===")  # \n = xuống dòng trống trước khi in

pi = 3.14159  # Lưu hằng số π (pi) vào biến, dùng xuyên suốt bài

# Nhập bán kính từ người dùng, chuyển sang số thực bằng float()
r = float(input("Nhập bán kính hình tròn (r): "))

# Tính diện tích: công thức = π × r²
# r ** 2 nghĩa là r bình phương (r mũ 2), ví dụ 5**2 = 25
dien_tich = pi * r ** 2

# Tính chu vi: công thức = 2 × π × r
chu_vi = 2 * pi * r

# In kết quả, :.2f = hiển thị 2 chữ số thập phân
print(f"Diện tích = π × {r}² = {dien_tich:.2f}")
print(f"Chu vi    = 2 × π × {r} = {chu_vi:.2f}")


# ============================================================
# TODO 3: Nhập giá gốc và % giảm giá, tính giá sau khi giảm
# ============================================================
print("\n=== TODO 3: Tính giảm giá ===")

# Nhập giá gốc từ người dùng (ví dụ: 500000)
gia_goc = float(input("Nhập giá gốc (VNĐ): "))

# Nhập % giảm giá (ví dụ: gõ 20 nghĩa là giảm 20%)
phan_tram_giam = float(input("Nhập % giảm giá: "))

# Tính số tiền được giảm: lấy giá gốc × phần trăm ÷ 100
# Ví dụ: 500000 × 20 ÷ 100 = 100000
so_tien_giam = gia_goc * phan_tram_giam / 100

# Giá sau giảm = Giá gốc - Số tiền giảm
gia_sau_giam = gia_goc - so_tien_giam

# :,.0f = in số có dấu phẩy ngàn, không có thập phân
# Ví dụ: 500000 → "500,000"   |   1234567 → "1,234,567"
print(f"Giá gốc:       {gia_goc:,.0f} VNĐ")
print(f"Giảm {phan_tram_giam}%:      -{so_tien_giam:,.0f} VNĐ")
print(f"Giá sau giảm:  {gia_sau_giam:,.0f} VNĐ")


# ============================================================
# TODO 4 (Thử thách): Máy đổi tiền VNĐ → USD
# ============================================================
print("\n=== TODO 4: Đổi tiền VNĐ → USD ===")

# Nhập số tiền VNĐ muốn đổi (ví dụ: 1000000)
so_tien_vnd = float(input("Nhập số tiền VNĐ: "))

# Nhập tỷ giá hôm nay (ví dụ: 25000 nghĩa là 1 USD = 25,000 VNĐ)
ty_gia = float(input("Nhập tỷ giá (1 USD = ? VNĐ): "))

# Đổi sang USD: lấy số VNĐ ÷ tỷ giá
# Ví dụ: 1,000,000 ÷ 25,000 = 40 USD
so_usd = so_tien_vnd / ty_gia

# :.2f = làm tròn USD đến 2 chữ số thập phân (vì tiền USD hay dùng xu)
print(f"{so_tien_vnd:,.0f} VNĐ = {so_usd:.2f} USD (tỷ giá {ty_gia:,.0f} VNĐ/USD)")
