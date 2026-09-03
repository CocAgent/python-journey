"""A class that owns one clear responsibility."""


class Progress:
    def __init__(self, completed: int, total: int):
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100


progress = Progress(3, 4)
print(progress.percentage())
