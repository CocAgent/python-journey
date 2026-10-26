"""Lời giải bài 02: Methods, giao dịch, sản phẩm và giỏ hàng."""


class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du=0):
        if so_du < 0:
            raise ValueError("Số dư ban đầu không được âm.")
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
        self.lich_su = []

    def gui_tien(self, so_tien):
        if so_tien <= 0:
            return False
        self.so_du += so_tien
        self.lich_su.append(f"Gửi +{so_tien:,.0f} VNĐ")
        return True

    def rut_tien(self, so_tien):
        if so_tien <= 0 or so_tien > self.so_du:
            return False
        self.so_du -= so_tien
        self.lich_su.append(f"Rút -{so_tien:,.0f} VNĐ")
        return True

    def xem_so_du(self):
        return self.so_du

    def xem_lich_su(self):
        return self.lich_su.copy()

    def __str__(self):
        return f"TK {self.chu_tai_khoan}: {self.so_du:,.0f} VNĐ"


class SanPham:
    def __init__(self, ten, gia, so_luong):
        if gia < 0 or so_luong < 0:
            raise ValueError("Giá và số lượng không được âm.")
        self.ten = ten
        self.gia = gia
        self.so_luong = so_luong

    def ban(self, sl):
        if sl <= 0 or sl > self.so_luong:
            return False
        self.so_luong -= sl
        return True

    def nhap(self, sl):
        if sl <= 0:
            return False
        self.so_luong += sl
        return True

    def tong_gia_tri(self):
        return self.gia * self.so_luong


class GioHang:
    def __init__(self):
        self.mat_hang = {}

    def them(self, san_pham, so_luong):
        if so_luong <= 0:
            return False
        ten = san_pham.ten
        da_chon = self.mat_hang.get(ten, {}).get("so_luong", 0)
        if da_chon + so_luong > san_pham.so_luong:
            return False
        self.mat_hang[ten] = {
            "san_pham": san_pham,
            "so_luong": da_chon + so_luong,
        }
        return True

    def xoa(self, ten_san_pham):
        return self.mat_hang.pop(ten_san_pham, None) is not None

    def tinh_tong(self):
        return sum(
            item["san_pham"].gia * item["so_luong"]
            for item in self.mat_hang.values()
        )

    def hien_thi(self):
        if not self.mat_hang:
            print("Giỏ hàng đang trống.")
            return
        for ten, item in self.mat_hang.items():
            thanh_tien = item["san_pham"].gia * item["so_luong"]
            print(f"{ten} x {item['so_luong']}: {thanh_tien:,.0f} VNĐ")
        print(f"Tổng cộng: {self.tinh_tong():,.0f} VNĐ")


def main():
    tk = TaiKhoanNganHang("Nguyễn An", 1_000_000)
    tk.gui_tien(500_000)
    tk.rut_tien(200_000)
    print(tk)
    print("Lịch sử:", *tk.xem_lich_su(), sep="\n- ")

    tra_sua = SanPham("Trà sữa", 30_000, 10)
    banh = SanPham("Bánh ngọt", 20_000, 5)
    gio_hang = GioHang()
    gio_hang.them(tra_sua, 2)
    gio_hang.them(banh, 1)
    gio_hang.hien_thi()


if __name__ == "__main__":
    main()
