"""Bài 1: tự hoàn thành class Progress.

Gợi ý: xem lý do kiểm tra total trong examples/01_class_object.py.
Chưa làm bài thì các phương thức cố ý báo NotImplementedError.
"""


class Progress:
    """Quản lý completed/total và tính tỷ lệ phần trăm."""

    def __init__(self, completed: int, total: int) -> None:
        # TODO: total > 0; completed phải nằm trong [0, total].
        # TODO: lưu self.completed và self.total sau khi xác thực.
        raise NotImplementedError("TODO: khởi tạo Progress")

    def percentage(self) -> float:
        # TODO: trả completed / total * 100, không in hoặc sửa dữ liệu.
        raise NotImplementedError("TODO: tính phần trăm")

    def __str__(self) -> str:
        # TODO: trả chuỗi "Progress: 3/4 (75%)" cho Progress(3, 4).
        raise NotImplementedError("TODO: biểu diễn Progress")
