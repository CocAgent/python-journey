"""Official solution for the Week 04 regex mini-lab."""

import re


def extract_codes(text: str) -> list[str]:
    return re.findall(r"PJ-\d{3}", text)


def first_number(text: str) -> str | None:
    match = re.search(r"\d+", text)
    return match.group() if match else None


def is_week_code(candidate: str) -> bool:
    return re.fullmatch(r"W\d{2}", candidate) is not None
