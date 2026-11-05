"""Bài 1: class Progress quản lý tiến độ hoàn thành."""


class Progress:
    """Lưu số lượng đã hoàn thành và tổng số lượng cần hoàn thành."""

    def __init__(self, completed: int, total: int) -> None:
        # Xác thực trước khi gán để object không bao giờ chứa tiến độ sai.
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if not 0 <= completed <= total:
            raise ValueError("completed phải nằm trong khoảng 0 đến total")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Trả về phần trăm hoàn thành."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Trả về thông tin ngắn gọn; không tự in ra màn hình."""
        percentage = self.percentage()
        return f"Progress: {self.completed}/{self.total} ({percentage:g}%)"


if __name__ == "__main__":
    progress = Progress(3, 4)
    print(progress)
