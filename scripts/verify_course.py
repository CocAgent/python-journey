"""Verify stable repository invariants for Python Journey V2."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_WEEK_NUMBERS = list(range(1, 16))
REQUIRED_ROOT_FILES = (
    "AGENTS.md",
    "CONTRIBUTING.md",
    "FINAL_PROJECT.md",
    "PROGRESS.md",
    "README.md",
    "SETUP.md",
    "STYLE_GUIDE.md",
    "SYLLABUS.md",
)
CONTENT_PATHS = (
    "README.md",
    "SYLLABUS.md",
    "SETUP.md",
    "STYLE_GUIDE.md",
    "CONTRIBUTING.md",
    "PROGRESS.md",
    "weeks",
    "assets",
    "cheatsheets",
    "templates",
)
CONTAMINATION_PATTERNS = (
    re.compile(r"g\+\+\s+-std=Python", re.IGNORECASE),
    re.compile(r"required\s+linked\s+list", re.IGNORECASE),
    re.compile(r"required\s+BST", re.IGNORECASE),
    re.compile(r"required\s+Graph", re.IGNORECASE),
    re.compile(r"required\s+Heap", re.IGNORECASE),
    re.compile(r"\.h\s+declaration", re.IGNORECASE),
    re.compile(r"struct\s+Book", re.IGNORECASE),
)


def syllabus_week_numbers(path: Path) -> list[int]:
    """Return week numbers from Markdown week headings."""
    numbers: list[int] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = line.lstrip("#").strip()
        if not heading.startswith("Tuần "):
            continue
        token = heading.removeprefix("Tuần ").split(maxsplit=1)[0]
        if token.isdigit():
            numbers.append(int(token))
    return numbers


def week_directory_numbers(path: Path) -> list[int]:
    """Return numeric prefixes from direct week directories."""
    numbers: list[int] = []
    for child in sorted(path.iterdir()):
        if not child.is_dir() or not child.name.startswith("week-"):
            continue
        parts = child.name.split("-", maxsplit=2)
        if len(parts) >= 2 and parts[1].isdigit():
            numbers.append(int(parts[1]))
    return numbers


def iter_content_files() -> list[Path]:
    """Return readable course content files, excluding capstone ownership."""
    files: list[Path] = []
    for relative in CONTENT_PATHS:
        path = ROOT / relative
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(candidate for candidate in path.rglob("*") if candidate.is_file())
    return files


def contamination_findings() -> list[str]:
    """Find foreign-language course requirements outside FINAL_PROJECT.md."""
    findings: list[str] = []
    for path in iter_content_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in CONTAMINATION_PATTERNS:
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)}: {pattern.pattern}")
    return findings


def verify() -> list[str]:
    """Return all invariant violations found in the repository."""
    errors: list[str] = []

    missing = [name for name in REQUIRED_ROOT_FILES if not (ROOT / name).is_file()]
    if missing:
        errors.append(f"Missing required root files: {', '.join(missing)}")

    weeks_path = ROOT / "weeks"
    if not weeks_path.is_dir():
        errors.append("Missing weeks directory")
    else:
        actual_weeks = week_directory_numbers(weeks_path)
        if actual_weeks != EXPECTED_WEEK_NUMBERS:
            errors.append(f"Week directories are {actual_weeks}, expected 1 through 15")

    syllabus_path = ROOT / "SYLLABUS.md"
    if syllabus_path.is_file():
        actual_syllabus = syllabus_week_numbers(syllabus_path)
        if actual_syllabus != EXPECTED_WEEK_NUMBERS:
            errors.append(f"Syllabus weeks are {actual_syllabus}, expected 1 through 15")

    final_project = ROOT / "FINAL_PROJECT.md"
    if final_project.is_file() and not final_project.read_text(encoding="utf-8").strip():
        errors.append("FINAL_PROJECT.md is empty")

    week_15_readmes = list((ROOT / "weeks").glob("week-15-*/README.md"))
    if len(week_15_readmes) != 1:
        errors.append("Expected exactly one Week 15 README")

    errors.extend(f"Course contamination: {finding}" for finding in contamination_findings())
    return errors


def main() -> int:
    """Print a concise health report and return a process status."""
    errors = verify()
    if errors:
        print("Python Journey course verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Python Journey course verification: PASS")
    print("- required root documents: present")
    print("- week directories: 15")
    print("- syllabus week headings: 15")
    print("- capstone ownership: present")
    print("- P0 content contamination: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
