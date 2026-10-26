"""Exercise 01: class, object and methods."""


class Progress:
    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


def main() -> None:
    progress = Progress(3, 4)

    print(progress)
    print(f"Phần trăm hoàn thành: {progress.percentage():.0f}%")


if __name__ == "__main__":
    main()
