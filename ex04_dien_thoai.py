"""Bài 4: tạo lớp DienThoai, hai đối tượng và hiển thị thông tin.

Không thay thế NotImplementedError bằng pass: bài chưa hoàn thành phải
được báo lỗi khi chạy kiểm thử.
"""


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
            raise ValueError("Mã máy không được rỗng")
        if not ten_may.strip():
            raise ValueError("Tên máy không được rỗng")
        if not hang_san_xuat.strip():
            raise ValueError("Hãng sản xuất không được rỗng")
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
        return (
            f"Mã: {self.ma_may}, Tên: {self.ten_may}, Hãng: {self.hang_san_xuat}, "
            f"Pin: {self.dung_luong_pin} mAh, Giá: {self.gia_ban} VND"
        )


if __name__ == "__main__":
    iphone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    samsung = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000)
    print(iphone.thongtindienthoai())
    print(samsung.thongtindienthoai())