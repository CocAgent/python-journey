"""Bài 4: tạo lớp DienThoai, hai đối tượng và hiển thị thông tin."""


class DienThoai:
    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_san_xuat: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        if not ma_may.strip():
            raise ValueError("Mã máy không được để trống")
        if not ten_may.strip():
            raise ValueError("Tên máy không được để trống")
        if not hang_san_xuat.strip():
            raise ValueError("Hãng sản xuất không được để trống")
        if dung_luong_pin <= 0:
            raise ValueError("Dung lượng pin phải lớn hơn 0")
        if gia_ban < 0:
            raise ValueError("Giá bán không được nhỏ hơn 0")
        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self) -> str:
        return (
            f"Ma may: {self.ma_may}\n"
            f"Ten may: {self.ten_may}\n"
            f"Hang san xuat: {self.hang_san_xuat}\n"
            f"Dung luong pin: {self.dung_luong_pin} mAh\n"
            f"Gia ban: {self.gia_ban:,} VND"
        )


if __name__ == "__main__":
    DT01 = DienThoai("DT01", "iPhone 16", "Apple", 3561, 22000000)
    DT02 = DienThoai("DT02", "Samsung Galaxy S25", "Samsung", 4000, 20000000)
    print("===== DIEN THOAI 1 =====")
    print(DT01.thongtindienthoai())
    print("\n===== DIEN THOAI 2 =====")
    print(DT02.thongtindienthoai())
