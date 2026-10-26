"""Exercise 01: class, object and methods."""


class Progress:
    """Track completed work against a positive total."""

    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")
        if completed < 0 or completed > total:
            raise ValueError("completed must be between 0 and total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Return the percentage of work completed."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Return a readable progress summary."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


if __name__ == "__main__":
    progress = Progress(3, 4)
    print(progress)
