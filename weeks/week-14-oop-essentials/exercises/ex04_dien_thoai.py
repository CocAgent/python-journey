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
        # TODO: từ chối mã/tên/hãng rỗng; dung_luong_pin <= 0; gia_ban < 0.
        # TODO: lưu đủ năm thuộc tính với self.
        if not ma_may.strip():
            raise ValueError("Mã máy không được để trống")
        if not ten_may.strip():
            raise ValueError("Tên máy không được để trống")
        if not hang_san_xuat.strip():
            raise ValueError("Hãng sản xuất không được để trống")
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
        # TODO: trả chuỗi có đủ 5 trường; lệnh print nằm bên ngoài class.
        gia_ban_text = f"{self.gia_ban:,}".replace(",", ".")
        return (
            f"Mã máy: {self.ma_may}\n"
            f"Tên máy: {self.ten_may}\n"
            f"Hãng sản xuất: {self.hang_san_xuat}\n"
            f"Dung lượng pin: {self.dung_luong_pin} mAh\n"
            f"Giá bán: {gia_ban_text} VNĐ"
        )


if __name__ == "__main__":
    # TODO: tạo DT01 và DT02 theo đề bài rồi gọi print(...).
    DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print("===== THÔNG TIN ĐIỆN THOẠI 1 =====")
    print(DT01.thongtindienthoai())

    print("\n===== THÔNG TIN ĐIỆN THOẠI 2 =====")
    print(DT02.thongtindienthoai())
