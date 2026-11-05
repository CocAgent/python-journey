"""Bài 4: tạo lớp DienThoai, hai đối tượng và hiển thị thông tin."""


class DienThoai:
    """Mô tả một điện thoại với dữ liệu riêng của từng object."""

    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_san_xuat: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        if not all(
            value.strip()
            for value in (ma_may, ten_may, hang_san_xuat)
        ):
            raise ValueError("Mã máy, tên máy và hãng không được để trống")
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
        """Trả chuỗi đủ năm trường để caller tự quyết định cách hiển thị."""
        return (
            f"{self.ma_may} | {self.ten_may} | {self.hang_san_xuat} | "
            f"{self.dung_luong_pin} mAh | {self.gia_ban} VND"
        )


if __name__ == "__main__":
    iphone = DienThoai(
        "DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000
    )
    samsung = DienThoai(
        "DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000
    )
    print(iphone.thongtindienthoai())
    print(samsung.thongtindienthoai())
