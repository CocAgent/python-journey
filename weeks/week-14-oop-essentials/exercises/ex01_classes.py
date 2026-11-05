"""Exercise 01: class, object and methods."""


class Progress:
    """Track completed items out of a total."""

    def __init__(self, completed: int, total: int) -> None:
        if total <= 0:
            raise ValueError("total must be positive")
        if not 0 <= completed <= total:
            raise ValueError("completed must be between 0 and total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Return the completed percentage."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


def main() -> None:
    progress = Progress(completed=7, total=15)
    print(progress)
    print(f"Completed: {progress.percentage():.1f}%")


if __name__ == "__main__":
    main()
