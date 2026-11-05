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
        # Không chấp nhận các chuỗi rỗng hoặc chỉ chứa khoảng trắng.
        if not all(
            isinstance(value, str) and value.strip()
            for value in (ma_may, ten_may, hang_san_xuat)
        ):
            raise ValueError("Mã máy, tên máy và hãng sản xuất không được rỗng")

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
        """Trả về chuỗi chứa đầy đủ năm thuộc tính."""
        return (
            f"Mã máy: {self.ma_may} | "
            f"Tên máy: {self.ten_may} | "
            f"Hãng sản xuất: {self.hang_san_xuat} | "
            f"Dung lượng pin: {self.dung_luong_pin} mAh | "
            f"Giá bán: {self.gia_ban:,} VND"
        )


if __name__ == "__main__":
    dien_thoai_1 = DienThoai(
        "DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000
    )
    dien_thoai_2 = DienThoai(
        "DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000
    )

    print(dien_thoai_1.thongtindienthoai())
    print(dien_thoai_2.thongtindienthoai())
