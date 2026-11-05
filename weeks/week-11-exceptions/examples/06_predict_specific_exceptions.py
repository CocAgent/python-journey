"""Example 06: specific exceptions, missing file vs invalid contents.

No broad except; exceptions are handled only where meaningful.
"""

from pathlib import Path
from tempfile import TemporaryDirectory


def read_score(path: Path) -> int | None:
    """A missing/invalid score is an expected input problem."""
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    try:
        value = int(raw)
    except ValueError:
        return None
    if not 0 <= value <= 10:
        return None
    return value


def main() -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        print(f"Missing file -> {read_score(root / 'missing.txt')!r}")
        good = root / "good.txt"
        good.write_text("8", encoding="utf-8")
        print(f"Valid score -> {read_score(good)}")
        bad = root / "bad.txt"
        bad.write_text("eight", encoding="utf-8")
        print(f"Invalid text -> {read_score(bad)!r}")
        bad.write_text("11", encoding="utf-8")
        print(f"Out-of-range -> {read_score(bad)!r}")

    print("Unexpected programming bugs should not be silenced")


if __name__ == "__main__":
    main()
