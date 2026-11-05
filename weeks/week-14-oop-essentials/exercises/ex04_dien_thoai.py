"""Bài 4: tạo lớp DienThoai, hai đối tượng và hiển thị thông tin.

Không thay thế NotImplementedError bằng pass: bài chưa hoàn thành phải
được báo lỗi khi chạy kiểm thử.
"""


class DienThoai:
    """Lớp quản lý thông tin điện thoại di động."""

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
            raise ValueError("Dung lượng pin phải là số nguyên dương lớn hơn 0")
        if gia_ban < 0:
            raise ValueError("Giá bán không được âm")

        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self) -> str:
        """Trả về chuỗi chứa đầy đủ 5 thông tin của điện thoại."""
        return (
            f"Mã: {self.ma_may} | Tên: {self.ten_may} | Hãng: {self.hang_san_xuat} | "
            f"Pin: {self.dung_luong_pin} mAh | Giá: {self.gia_ban} VND"
        )


if __name__ == "__main__":
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000)
    print(dt01.thongtindienthoai())
    print(dt02.thongtindienthoai())

