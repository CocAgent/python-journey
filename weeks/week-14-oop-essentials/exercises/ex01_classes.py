"""Bài 1: tự hoàn thành class Progress.

Gợi ý: xem lý do kiểm tra total trong examples/01_class_object.py.
Chưa làm bài thì các phương thức cố ý báo NotImplementedError.
"""


class Progress:
    """Quản lý completed/total và tính tỷ lệ phần trăm."""

    def __init__(self, completed: int, total: int) -> None:
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if not 0 <= completed <= total:
            raise ValueError("completed phải nằm trong đoạn [0, total]")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"
