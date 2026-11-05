class DienThoai:
    def __init__(self, ma_may, ten_may, hang_san_xuat, dung_luong_pin, gia_ban):
        if not isinstance(ma_may, str) or not ma_may.strip():
            raise ValueError("ma_may must not be empty")
        if not isinstance(ten_may, str) or not ten_may.strip():
            raise ValueError("ten_may must not be empty")
        if not isinstance(hang_san_xuat, str) or not hang_san_xuat.strip():
            raise ValueError("hang_san_xuat must not be empty")
        if dung_luong_pin <= 0:
            raise ValueError("dung_luong_pin must be greater than 0")
        if gia_ban < 0:
            raise ValueError("gia_ban must not be negative")

        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self):
        return (
            f"Ma may: {self.ma_may}\n"
            f"Ten may: {self.ten_may}\n"
            f"Hang san xuat: {self.hang_san_xuat}\n"
            f"Dung luong pin: {self.dung_luong_pin} mAh\n"
            f"Gia ban: {self.gia_ban:,} VND"
        )


if __name__ == "__main__":
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print(dt01.thongtindienthoai())
    print()
    print(dt02.thongtindienthoai())
