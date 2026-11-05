"""Bài 1: tự hoàn thành class Progress.

Gợi ý: xem lý do kiểm tra total trong examples/01_class_object.py.
Chưa làm bài thì các phương thức cố ý báo NotImplementedError.
"""


class Progress:
    def __init__(self, completed: int, total: int):
        # Kiểm tra dữ liệu trước khi tạo đối tượng
        if total <= 0 or not 0 <= completed <= total:
            raise ValueError("Tiến độ không hợp lệ")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():g}%)"


if __name__ == "__main__":
    p = Progress(3, 4)

    print(p.percentage())
    print(p)