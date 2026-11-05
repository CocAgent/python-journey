"""Bài 1: tự hoàn thành class Progress."""


class Progress:
    """Quản lý completed/total và tính tỷ lệ phần trăm."""

    def __init__(self, completed: int, total: int) -> None:
        # Xác thực dữ liệu trước khi lưu để object luôn hợp lệ.
        if total <= 0 or not 0 <= completed <= total:
            raise ValueError("Tiến độ phải nằm trong khoảng 0 đến total")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Trả về phần trăm hoàn thành."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Trả về chuỗi mô tả object, không tự in ra màn hình."""
        return (
            f"Progress: {self.completed}/{self.total} "
            f"({self.percentage():.0f}%)"
        )
