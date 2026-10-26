"""Exercise 01: class, object and methods."""


class Progress:
    def __init__(self, completed: int, total: int) -> None:
        self.completed = completed
        self.total = total

    def percentage(self) -> int:
        if self.total == 0:
            return 0
        return self.completed * 100 // self.total

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage()}%)"


def main() -> None:
    progress = Progress(3, 4)
    print(progress)
    print(progress.percentage())


if __name__ == "__main__":
    main()
