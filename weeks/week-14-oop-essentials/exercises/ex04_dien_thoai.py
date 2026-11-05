"""Bài 4: Lớp DienThoai và hai đối tượng mẫu."""


class DienThoai:
    def __init__(self, ma_may, ten_may, hang_san_xuat, dung_luong_pin, gia_ban):
        if not ma_may.strip() or not ten_may.strip() or not hang_san_xuat.strip():
            raise ValueError("Mã, tên và hãng sản xuất không được để trống")
        if dung_luong_pin <= 0:
            raise ValueError("Dung lượng pin phải lớn hơn 0")
        if gia_ban < 0:
            raise ValueError("Giá bán không được âm")

        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self):
        return (
            f"Mã máy: {self.ma_may}\n"
            f"Tên máy: {self.ten_may}\n"
            f"Hãng sản xuất: {self.hang_san_xuat}\n"
            f"Dung lượng pin: {self.dung_luong_pin} mAh\n"
            f"Giá bán: {self.gia_ban:,} VND"
        )


if __name__ == "__main__":
    iphone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    samsung = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print(iphone.thongtindienthoai())
    print()
    print(samsung.thongtindienthoai())
