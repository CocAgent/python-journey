"""Bài 4: lớp DienThoai và hai đối tượng điện thoại độc lập."""


class DienThoai:
    """Mô tả điện thoại bằng mã, tên, hãng, pin và giá bán."""

    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_san_xuat: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        if not ma_may.strip() or not ten_may.strip() or not hang_san_xuat.strip():
            raise ValueError("Mã máy, tên máy và hãng sản xuất không được để trống")
        if dung_luong_pin <= 0:
            raise ValueError("Dung lượng pin phải lớn hơn 0")
        if gia_ban < 0:
            raise ValueError("Giá bán không được âm")
        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self) -> str:
        """Trả về thông tin dạng chuỗi, không tự in ra màn hình."""
        return (
            f"Mã máy: {self.ma_may}; Tên máy: {self.ten_may}; "
            f"Hãng sản xuất: {self.hang_san_xuat}; "
            f"Dung lượng pin: {self.dung_luong_pin} mAh; "
            f"Giá bán: {self.gia_ban} VND"
        )


if __name__ == "__main__":
    dien_thoai_1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    dien_thoai_2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000)
    print(dien_thoai_1.thongtindienthoai())
    print(dien_thoai_2.thongtindienthoai())
