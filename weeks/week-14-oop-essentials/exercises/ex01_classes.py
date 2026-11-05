"""Bài 1: tự hoàn thành class Progress.

Gợi ý: xem lý do kiểm tra total trong examples/01_class_object.py.
Chưa làm bài thì các phương thức cố ý báo NotImplementedError.
"""


class Progress:
    """Quản lý completed/total và tính tỷ lệ phần trăm."""

    def __init__(self, completed: int, total: int) -> None:
        if total <= 0:
            raise ValueError("Tổng số việc (total) phải lớn hơn 0")
        if not 0 <= completed <= total:
            raise ValueError("Số việc hoàn thành (completed) phải nằm trong khoảng từ 0 đến total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Tính và trả về phần trăm hoàn thành, không sửa đổi dữ liệu."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Biểu diễn chuỗi thân thiện cho Progress."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"

