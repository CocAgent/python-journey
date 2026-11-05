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
        gia_ban: int
    ):

        # Kiểm tra chuỗi rỗng
        if (
            not ma_may.strip()
            or not ten_may.strip()
            or not hang_san_xuat.strip()
        ):
            raise ValueError("Thông tin điện thoại không được để trống")

        # Kiểm tra pin và giá
        if dung_luong_pin <= 0 or gia_ban < 0:
            raise ValueError("Pin hoặc giá bán không hợp lệ")

        # Lưu thông tin
        self.ma_may = ma_may.strip()
        self.ten_may = ten_may.strip()
        self.hang_san_xuat = hang_san_xuat.strip()
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self) -> str:
        return (
            f"Mã máy: {self.ma_may}\n"
            f"Tên máy: {self.ten_may}\n"
            f"Hãng sản xuất: {self.hang_san_xuat}\n"
            f"Dung lượng pin: {self.dung_luong_pin} mAh\n"
            f"Giá bán: {self.gia_ban} VND"
        )


if __name__ == "__main__":

    iphone = DienThoai(
        "DT01",
        "iPhone 15 Pro",
        "Apple",
        3274,
        28_990_000
    )

    samsung = DienThoai(
        "DT02",
        "Galaxy S24 Ultra",
        "Samsung",
        5000,
        29_990_000
    )

    print("THÔNG TIN ĐIỆN THOẠI 1")
    print(iphone.thongtindienthoai())

    print("\nTHÔNG TIN ĐIỆN THOẠI 2")
    print(samsung.thongtindienthoai())