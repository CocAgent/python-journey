"""Starter for the Student Manager alternative midterm track."""


def calculate_average(student: dict[str, object]) -> float:
    """Return the average of the student's scores."""
    # TODO: read the nested scores list and handle an empty list.
    return 0.0


def classify_student(average: float) -> str:
    """Return an explainable classification from an average."""
    # TODO: define a small set of ordered thresholds.
    return "Chưa xếp loại"


def find_student(
    students: list[dict[str, object]], query: str
) -> dict[str, object] | None:
    """Return the first case-insensitive name match."""
    # TODO: iterate through caller-owned data; avoid a global students list.
    return None


def main() -> None:
    """Run the starter with nested sample data."""
    students = [
        {"name": "An", "scores": [8.0, 9.0, 7.0]},
        {"name": "Bình", "scores": [7.0, 6.0, 8.0]},
    ]
    for student in students:
        average = calculate_average(student)
        print(f"{student['name']}: {average:.1f} — {classify_student(average)}")


if __name__ == "__main__":
    main()
