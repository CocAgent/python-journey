"""Write and read UTF-8 text with pathlib."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "evidence.txt"
    path.write_text("Python Journey", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
