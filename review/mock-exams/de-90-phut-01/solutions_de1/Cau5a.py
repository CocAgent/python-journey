"""Cau5a — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

class DienThoai:
    """Điện thoại giả lập cho bài OOP căn bản, không dùng dữ liệu sản xuất."""

    def __init__(
        self,
        MaMay: str,
        TenMay: str,
        HangSanXuat: str,
        DungLuongPin: int,
        GiaBan: int,
    ) -> None:
        if any(
            not isinstance(value, str) or not value.strip()
            for value in (MaMay, TenMay, HangSanXuat)
        ):
            raise ValueError("Chuỗi thông tin máy không hợp lệ")
        if type(DungLuongPin) is not int or DungLuongPin <= 0:
            raise ValueError("Dung lượng pin không hợp lệ")
        if type(GiaBan) is not int or GiaBan < 0:
            raise ValueError("Giá bán không hợp lệ")
        self.MaMay = MaMay.strip()
        self.TenMay = TenMay.strip()
        self.HangSanXuat = HangSanXuat.strip()
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self) -> str:
        """Định dạng thống nhất để caller có thể in hoặc lưu."""
        return (
            f"{self.MaMay} | {self.TenMay} | {self.HangSanXuat}"
            f" | {self.DungLuongPin} mAh | {self.GiaBan} VND"
        )
