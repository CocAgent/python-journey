"""Lời giải tham chiếu bài tập lớp DienThoai (không phải bài nộp)."""


class DienThoai:
    """Một điện thoại với mã, tên, hãng, pin và giá bán."""

    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_san_xuat: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        if not ma_may.strip() or not ten_may.strip() or not hang_san_xuat.strip():
            raise ValueError("Mã, tên máy và hãng không được để trống")
        if dung_luong_pin <= 0:
            raise ValueError("Dung lượng pin phải là số dương")
        if gia_ban < 0:
            raise ValueError("Giá bán không được âm")
        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def thongtindienthoai(self) -> str:
        """Trả chuỗi có đủ năm thuộc tính để dễ in và dễ kiểm thử."""
        return (
            f"Mã máy: {self.ma_may}; Tên máy: {self.ten_may}; "
            f"Hãng: {self.hang_san_xuat}; "
            f"Pin: {self.dung_luong_pin} mAh; "
            f"Giá bán: {self.gia_ban} VND"
        )
