"""Official solution: variables and types."""


def build_profile(
    name: str, age: int, average: float, is_learning: bool
) -> dict[str, object]:
    """Return four named values in one simple profile."""
    return {
        "name": name,
        "age": age,
        "average": average,
        "is_learning": is_learning,
    }


if __name__ == "__main__":
    profile = build_profile("An", 18, 8.5, True)
    for key, value in profile.items():
        print(f"{key}={value}, type={type(value).__name__}")
