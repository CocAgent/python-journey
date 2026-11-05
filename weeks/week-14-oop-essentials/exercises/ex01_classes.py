# Bài 1: Class, object và method

class Progress:
    def __init__(self, completed, total):
        if total <= 0:
            raise ValueError("Tổng số phải lớn hơn 0")
        if completed < 0 or completed > total:
            raise ValueError("Tiến độ không hợp lệ")

        self.completed = completed
        self.total = total

    def percentage(self):
        return self.completed / self.total * 100

    def __str__(self):
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


# Tạo object và sử dụng
tien_do = Progress(3, 4)
print("Phần trăm:", tien_do.percentage())
print(tien_do)
