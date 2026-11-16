"""Ví dụ 1: gom dữ liệu tiến độ và phương thức liên quan trong class."""


class Progress:
    def __init__(self, completed: int, total: int) -> None:
        # Kiểm tra trước khi gán để object luôn ở trạng thái hợp lệ.
        if total <= 0 or not 0 <= completed <= total:
            raise ValueError("Tiến độ phải nằm trong khoảng 0 đến total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Tính tỷ lệ hoàn thành, không thay đổi object."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Chuỗi dùng khi print(object), không tự in ra màn hình."""
        return f"Progress: {self.completed}/{self.total}"


if __name__ == "__main__":
    progress = Progress(3, 4)
    print(progress.percentage())  # 75.0
    print(progress)  # Progress: 3/4
