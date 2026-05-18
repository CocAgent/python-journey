"""
Bài tập 02: Methods & đóng gói 🔒
====================================
Mục tiêu: Instance methods, property, encapsulation
"""

# TODO 1: Tạo class TaiKhoanNganHang
# - __init__(self, chu_tai_khoan, so_du=0)
# - gui_tien(self, so_tien) — kiểm tra số tiền > 0
# - rut_tien(self, so_tien) — kiểm tra đủ số dư
# - xem_so_du(self)
# - __str__(self)


# TODO 2: Thêm lịch sử giao dịch
# - Mỗi lần gửi/rút → thêm vào list lich_su
# - Thêm method xem_lich_su(self) in ra lịch sử


# TODO 3: Tạo class SanPham
# - __init__(self, ten, gia, so_luong)
# - ban(self, sl) → giảm số lượng, kiểm tra còn hàng
# - nhap(self, sl) → tăng số lượng
# - tong_gia_tri(self) → giá × số lượng


# TODO 4 (Thử thách): Tạo class GioHang
# - them(self, san_pham, so_luong)
# - xoa(self, ten_san_pham)
# - tinh_tong(self) → tổng tiền
# - hien_thi(self) → in giỏ hàng
