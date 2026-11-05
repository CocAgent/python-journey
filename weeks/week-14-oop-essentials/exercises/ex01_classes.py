"""Bài 1: class Progress quản lý tiến độ hoàn thành."""


class Progress:
    """Lưu số lượng đã hoàn thành và tổng số công việc."""

    def __init__(self, completed: int, total: int) -> None:
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if completed < 0 or completed > total:
            raise ValueError("completed phải nằm trong khoảng từ 0 đến total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"
