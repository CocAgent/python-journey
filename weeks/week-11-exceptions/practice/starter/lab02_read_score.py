"""Lab 02: isolate file I/O vs number parse errors (no broad except)."""

from pathlib import Path


def read_score(path: Path) -> int | None:
    """Missing file / invalid content -> None; valid int 0..10 -> int.

    Keep other errors visible (e.g. path is the wrong object type).
    """
    # TODO: try path.read_text(encoding="utf-8"), except FileNotFoundError.
    # TODO: try int(text), except ValueError.
    # TODO: validate score 0..10, otherwise None.
    raise NotImplementedError("Hoàn thiện read_score")


if __name__ == "__main__":
    print("Chạy self-check; không tạo file bên ngoài TemporaryDirectory.")
