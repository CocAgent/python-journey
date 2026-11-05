"""Bài 1: tự hoàn thành class Progress.

Gợi ý: xem lý do kiểm tra total trong examples/01_class_object.py.
"""


class Progress:
    """Quản lý completed/total và tính tỷ lệ phần trăm."""

    def __init__(self, completed: int, total: int) -> None:
        """Khởi tạo tiến độ với completed và total hợp lệ.

        Từ chối total <= 0 hoặc completed ngoài [0, total].
        """
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if not (0 <= completed <= total):
            raise ValueError("completed phải nằm trong khoảng [0, total]")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Trả completed / total * 100, không in hoặc sửa dữ liệu."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Trả chuỗi biểu diễn Progress, ví dụ: 'Progress: 3/4 (75%)'."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


if __name__ == "__main__":
    p = Progress(3, 4)
    print(p)
    print(f"Hoàn thành: {p.percentage()}%")
