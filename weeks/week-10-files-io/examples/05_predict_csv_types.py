"""Predict CSV readback types; validate before arithmetic. All temp files."""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory


def main() -> None:
    with TemporaryDirectory() as directory:
        path = Path(directory) / "scores.csv"
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=["name", "score"])
            writer.writeheader()
            writer.writerows([
                {"name": "An", "score": 8},
                {"name": "Bình", "score": 9},
            ])
        with path.open("r", newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        print(f"CSV rows: {rows}")
        print(f"Score type after CSV: {type(rows[0]['score']).__name__}")
        converted = [int(row["score"]) for row in rows]
        print(f"Score sum after int: {sum(converted)}")

        # A malformed row must not silently become a valid score.
        bad_csv = Path(directory) / "bad.csv"
        bad_csv.write_text("name,score\nAn,not-a-number\n", encoding="utf-8")
        with bad_csv.open("r", newline="", encoding="utf-8") as stream:
            invalid = list(csv.DictReader(stream))
        try:
            int(invalid[0]["score"])
        except ValueError:
            print("Invalid CSV score: ValueError (expected)")


if __name__ == "__main__":
    main()
