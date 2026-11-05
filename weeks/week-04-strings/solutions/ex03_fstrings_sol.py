"""Official solutions for f-string formatting."""


def student_summary(name: str, age: int, average: float) -> str:
    return f"Học sinh {name}, {age} tuổi, điểm TB: {average:.2f}"


def product_row(name: str, price: int) -> str:
    return f"{name:<20}{price:>10,}"


def progress_bar(percent: int) -> str:
    filled = percent // 5
    bar = "█" * filled + "░" * (20 - filled)
    return f"[{bar}] {percent}%"
