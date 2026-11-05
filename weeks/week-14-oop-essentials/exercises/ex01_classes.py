class Progress:
    def __init__(self, completed, total):
        if total <= 0:
            raise ValueError("total must be greater than 0")
        if completed < 0 or completed > total:
            raise ValueError("completed must be between 0 and total")

        self.completed = completed
        self.total = total

    def percentage(self):
        return self.completed / self.total * 100

    def __str__(self):
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"
