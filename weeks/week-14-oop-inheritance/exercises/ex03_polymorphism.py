"""
Bài tập 03: Đa hình (Polymorphism) 🎭
========================================
Mục tiêu: Hiểu và áp dụng đa hình
"""

# TODO 1: Đa hình qua method chung
# Tạo list: [HinhTron(5), HinhChuNhat(4, 6), HinhTamGiac(3, 4, 5)]
# Dùng for loop gọi tinh_dien_tich() trên mỗi hình
# → Cùng method name, kết quả khác nhau = đa hình!


# TODO 2: Đa hình với "hợp đồng"
# Class ThanhToan (cha): phuong_thuc(), xu_ly(so_tien)
# Class TienMat: xu_ly() → "Nhận tiền mặt..."
# Class TheNganHang: xu_ly() → "Trừ thẻ..."
# Class ViDienTu: xu_ly() → "Chuyển qua ví..."
# Viết hàm thanh_toan(don_hang, phuong_thuc) hoạt động với bất kỳ loại nào


# TODO 3: Duck typing
# Bất cứ object nào có method .speak() đều gọi được
# Không cần kế thừa chung — chỉ cần "có method giống nhau"


# TODO 4 (Thử thách): Hệ thống nhân viên
# NhanVien → FullTime, PartTime, Intern
# Mỗi loại tính lương khác nhau
# Viết hàm tong_luong(danh_sach_nhan_vien) dùng đa hình
