"""Câu 5a — Sinh viên tự hoàn thiện lớp DienThoai.

Khai báo class DienThoai, __init__ lưu 5 thuộc tính, kiểm chuỗi không rỗng; dung lượng pin là int dương, giá bán int không âm. Phương thức thongtindienthoai() trả chuỗi thông tin theo mẫu. Sai -> ValueError.
Dùng class, __init__(self,...), gán self.*, tạo method trả f-string, không print.
"""


class DienThoai:
    """Lớp sinh viên cần hoàn thiện."""

    def __init__(
        self,
        MaMay: str,
        TenMay: str,
        HangSanXuat: str,
        DungLuongPin: int,
        GiaBan: int,
    ) -> None:
        # TODO: validate input, lưu năm thuộc tính lên self.
        raise NotImplementedError("Hoàn thành Cau5a.__init__")

    def thongtindienthoai(self) -> str:
        # TODO: return "MaMay | TenMay | HangSanXuat | DungLuongPin mAh | GiaBan VND"
        raise NotImplementedError("Hoàn thành thongtindienthoai")
