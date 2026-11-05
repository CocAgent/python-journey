"""Bài 1: class Progress quản lý tiến độ hoàn thành."""


class Progress:
    """Quản lý completed/total và tính tỷ lệ phần trăm."""

    def __init__(self, completed: int, total: int) -> None:
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if not 0 <= completed <= total:
            raise ValueError("completed phải nằm trong khoảng [0, total]")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Trả về phần trăm hoàn thành, không làm thay đổi trạng thái."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Hiển thị tiến độ gọn, không in trực tiếp."""
        return (
            f"Progress: {self.completed}/{self.total} "
            f"({self.percentage():g}%)"
        )
