"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

path = Path("match_summary.csv")
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]
# TODO: write header and rows with csv.DictWriter.
# TODO: load rows with csv.DictReader and print them.
print(csv.__name__, path, rows)
