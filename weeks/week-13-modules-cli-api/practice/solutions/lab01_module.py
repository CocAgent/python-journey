"""Lab 1 solution: import, return, main guard."""

from practice.study_core import status_for_score


def describe_score(score: int | float) -> str:
    """Không in trong core: người gọi quyết định in ra đâu."""
    return f"Điểm {score:g}: {status_for_score(score)}"


def main() -> None:
    print(describe_score(7.5))


if __name__ == "__main__":
    main()
