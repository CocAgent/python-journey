"""Lời giải Bài tập 02: Methods & đóng gói"""

class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du=0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
        self.lich_su = []

    def gui_tien(self, so_tien):
        if so_tien <= 0:
            print("Số tiền phải > 0!")
            return
        self.so_du += so_tien
        self.lich_su.append(f"+{so_tien:,} (Gửi)")
        print(f"Gửi {so_tien:,} thành công. Số dư: {self.so_du:,}")

    def rut_tien(self, so_tien):
        if so_tien <= 0:
            print("Số tiền phải > 0!")
            return
        if so_tien > self.so_du:
            print("Không đủ số dư!")
            return
        self.so_du -= so_tien
        self.lich_su.append(f"-{so_tien:,} (Rút)")
        print(f"Rút {so_tien:,} thành công. Số dư: {self.so_du:,}")

    def xem_lich_su(self):
        print(f"Lịch sử giao dịch ({self.chu_tai_khoan}):")
        for gd in self.lich_su:
            print(f"  {gd}")

    def __str__(self):
        return f"TK {self.chu_tai_khoan}: {self.so_du:,} VNĐ"

tk = TaiKhoanNganHang("Nguyễn An", 1000000)
tk.gui_tien(500000)
tk.rut_tien(200000)
print(tk)
tk.xem_lich_su()
