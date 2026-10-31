"""Predict: relative paths, UTF-8, and missing files. Offline and sandboxed."""

from pathlib import Path
from tempfile import TemporaryDirectory


def main() -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        target = root / "notes" / "lesson.txt"
        print(f"Relative to terminal? {Path('notes/lesson.txt').is_absolute()}")
        print(f"Exists before save: {target.exists()}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("Chào Python\nDòng hai\n", encoding="utf-8")
        print(f"Read back: {target.read_text(encoding='utf-8').splitlines()}")
        print(f"Exists after save: {target.exists()}")
        missing = root / "missing.txt"
        try:
            missing.read_text(encoding="utf-8")
        except FileNotFoundError:
            print("Missing file: FileNotFoundError (expected)")
        print(f"Missing file exists: {missing.exists()}")


if __name__ == "__main__":
    main()
