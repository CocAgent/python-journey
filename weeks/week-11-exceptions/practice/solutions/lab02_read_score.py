"""Reference: file existence, numeric parsing, and range are separate."""


from pathlib import Path


def read_score(path: Path) -> int | None:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None

    try:
        value = int(text)
    except ValueError:
        return None

    if not 0 <= value <= 10:
        return None
    return value


if __name__ == "__main__":
    print("Use the self-check (isolated temporary files).")
