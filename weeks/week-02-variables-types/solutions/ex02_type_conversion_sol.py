"""Official solution: explicit type conversion."""


def parse_whole_number(text: str) -> int:
    """Convert numeric text to an integer."""
    return int(text)


def calculate_bmi(weight: float, height: float) -> float:
    """Return BMI rounded to one decimal place."""
    return round(weight / height**2, 1)


def seconds_to_parts(total_seconds: int) -> tuple[int, int, int]:
    """Split seconds into hours, minutes and seconds."""
    hours = total_seconds // 3600
    minutes = total_seconds % 3600 // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds


if __name__ == "__main__":
    print(parse_whole_number("42"))
    print(calculate_bmi(70, 1.75))
    print(seconds_to_parts(3661))
