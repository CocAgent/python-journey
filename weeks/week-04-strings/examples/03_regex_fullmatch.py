"""Validate one deliberately simplified teaching code."""

import re

pattern = r"W\d{2}"

for candidate in ("W04", "W4", "week04"):
    valid = re.fullmatch(pattern, candidate) is not None
    print(f"{candidate}: {valid}")

print("SIMPLIFIED COURSE PATTERN — NOT A UNIVERSAL STANDARD")
