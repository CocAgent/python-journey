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

        # Kiểm tra mã máy, tên máy và hãng sản xuất không được rỗng
        if not ma_may.strip():
            raise ValueError("Mã máy không được để trống")

        if not ten_may.strip():
            raise ValueError("Tên máy không được để trống")

        if not hang_san_xuat.strip():
            raise ValueError("Hãng sản xuất không được để trống")

        # Kiểm tra dung lượng pin phải lớn hơn 0
        if dung_luong_pin <= 0:
            raise ValueError("Dung lượng pin phải lớn hơn 0")

        # Kiểm tra giá bán không được âm
        if gia_ban < 0:
            raise ValueError("Giá bán không được nhỏ hơn 0")

        # Lưu 5 thuộc tính
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

    # Tạo đối tượng điện thoại thứ nhất
    DT01 = DienThoai(
        "DT01",
        "iPhone 16",
        "Apple",
        3561,
        22000000
    )

    # Tạo đối tượng điện thoại thứ hai
    DT02 = DienThoai(
        "DT02",
        "Samsung Galaxy S25",
        "Samsung",
        4000,
        20000000
    )

    # Hiển thị thông tin
    print("===== DIEN THOAI 1 =====")
    print(DT01.thongtindienthoai())

    print("\n===== DIEN THOAI 2 =====")
    print(DT02.thongtindienthoai())

