"""Ví dụ 4: tạo hai đối tượng điện thoại từ cùng một class."""


class DienThoai:
    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_san_xuat: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        # Từ chối pin hoặc giá vô lý trước khi tạo đối tượng.
        if dung_luong_pin <= 0 or gia_ban < 0:
            raise ValueError("Dung lượng pin hoặc giá bán không hợp lệ")
        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self) -> str:
        """Trả về chuỗi để người gọi có thể in hoặc kiểm thử."""
        return (
            f"{self.ma_may} | {self.ten_may} | {self.hang_san_xuat} | "
            f"{self.dung_luong_pin} mAh | {self.gia_ban} VND"
        )


if __name__ == "__main__":
    iphone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    samsung = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000)
    print(iphone.thongtindienthoai())
    print(samsung.thongtindienthoai())
