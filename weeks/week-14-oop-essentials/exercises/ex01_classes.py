"""Exercise 01: Classes and objects."""


class Progress:
    def __init__(self, completed: int, total: int) -> None:
        if total <= 0 or not 0 <= completed <= total:
            raise ValueError("Invalid progress")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


if __name__ == "__main__":
    progress = Progress(3, 4)
    print(progress)
    print(progress.percentage())
