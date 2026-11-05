"""Lời giải bài 1: class Progress."""


class Progress:
    """Quản lý số việc đã hoàn thành trên tổng số việc."""

    def __init__(self, completed: int, total: int) -> None:
        # Kiểm tra total trước để phép chia luôn an toàn.
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if not 0 <= completed <= total:
            raise ValueError("completed phải nằm trong khoảng [0, total]")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Trả tỷ lệ hoàn thành theo phần trăm."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Trả chuỗi hiển thị gọn; :g bỏ .0 khi là số nguyên."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():g}%)"
