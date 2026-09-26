"""Round-trip a small CSV table."""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

rows = [{"bot": "student", "wins": "2"}, {"bot": "wait", "wins": "0"}]
with TemporaryDirectory() as directory:
    path = Path(directory) / "summary.csv"
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["bot", "wins"])
        writer.writeheader()
        writer.writerows(rows)
    with path.open(encoding="utf-8") as stream:
        print(list(csv.DictReader(stream)))
