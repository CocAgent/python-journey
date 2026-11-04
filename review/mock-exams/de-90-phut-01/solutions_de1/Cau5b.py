"""Cau5b — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

from Cau5a import DienThoai


def tao_danh_sach_dien_thoai() -> list[DienThoai]:
    return [
        DienThoai("DT01", "Thiết bị A", "Hãng A", 4500, 12_000_000),
        DienThoai("DT02", "Thiết bị B", "Hãng B", 5000, 15_000_000),
    ]
