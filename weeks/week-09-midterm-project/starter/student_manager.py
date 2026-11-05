"""Student Manager midterm track using nested list/dict data."""


def calculate_average(student: dict[str, object]) -> float:
    """Return the average of numeric scores, or 0 for missing/empty scores."""
    scores = student.get("scores", [])
    if not isinstance(scores, list) or not scores:
        return 0.0
    numeric_scores = [score for score in scores if isinstance(score, (int, float))]
    if not numeric_scores:
        return 0.0
    return sum(numeric_scores) / len(numeric_scores)


def classify_student(average: float) -> str:
    """Return an explainable classification from an average."""
    if average >= 8:
        return "Giỏi"
    if average >= 6.5:
        return "Khá"
    if average >= 5:
        return "Trung bình"
    return "Cần cố gắng"


def find_student(
    students: list[dict[str, object]], query: str
) -> dict[str, object] | None:
    """Return the first case-insensitive name match."""
    normalized_query = query.strip().casefold()
    if not normalized_query:
        return None
    for student in students:
        name = student.get("name")
        if isinstance(name, str) and name.casefold() == normalized_query:
            return student
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
    match = find_student(students, "bÌNH")
    print(f"Tìm học sinh: {match['name'] if match else 'Không tìm thấy'}")


if __name__ == "__main__":
    main()
