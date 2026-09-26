"""Structural readiness check for a learner capstone submission.

Canonical requirements and the only rubric live in FINAL_PROJECT.md. This check
reports mechanical evidence — files present, tests collectable, no bare except —
so a learner can self-audit before handoff. It does not grade design quality and
it never replaces human review.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from pathlib import Path

MIN_TESTS = 5
MIN_FUNCTIONS = 4
README_SECTIONS = ("setup", "usage", "test")


def python_files(root: Path) -> list[Path]:
    """Return project Python files, skipping virtualenvs and caches."""
    skip = {".venv", "venv", "env", "__pycache__", ".git", "build", "dist"}
    return [
        path
        for path in sorted(root.rglob("*.py"))
        if not skip.intersection(path.parts)
    ]


def parse(path: Path) -> ast.Module | None:
    """Return the parsed module, or None when the file cannot be parsed."""
    try:
        return ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return None


def check_documents(root: Path) -> list[str]:
    """Report missing required documents and README sections."""
    problems: list[str] = []
    readme = root / "README.md"
    if not readme.is_file():
        problems.append("thiếu README.md")
    else:
        text = readme.read_text(encoding="utf-8", errors="replace").lower()
        missing = [name for name in README_SECTIONS if name not in text]
        if missing:
            problems.append(f"README.md chưa nhắc tới: {', '.join(missing)}")
    if not (root / "AI_USAGE.md").is_file():
        problems.append("thiếu AI_USAGE.md")
    return problems


def check_decomposition(files: list[Path]) -> list[str]:
    """Report too few functions across the project."""
    total = 0
    for path in files:
        tree = parse(path)
        if tree is None:
            continue
        total += sum(
            isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef)
            for node in ast.walk(tree)
        )
    if total < MIN_FUNCTIONS:
        return [f"chỉ tìm thấy {total} hàm, cần >= {MIN_FUNCTIONS}"]
    return []


def check_bare_except(files: list[Path]) -> list[str]:
    """Report every bare except clause, which the course forbids."""
    problems: list[str] = []
    for path in files:
        tree = parse(path)
        if tree is None:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                problems.append(f"bare except tại {path.name}:{node.lineno}")
    return problems


def check_tests(root: Path, files: list[Path]) -> list[str]:
    """Report a shortfall of test functions and any collection failure."""
    problems: list[str] = []
    test_functions = 0
    test_files = [path for path in files if path.name.startswith("test_")]
    for path in test_files:
        tree = parse(path)
        if tree is None:
            continue
        test_functions += sum(
            isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef)
            and node.name.startswith("test_")
            for node in ast.walk(tree)
        )
    if test_functions < MIN_TESTS:
        problems.append(f"chỉ tìm thấy {test_functions} test, cần >= {MIN_TESTS}")

    if test_files:
        collected = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", "-q"],
            cwd=root,
            capture_output=True,
            text=True,
        )
        if collected.returncode != 0:
            problems.append("pytest không collect được test (xem lỗi import/syntax)")
    return problems


def main() -> int:
    """Audit a capstone directory and return a process exit code."""
    # Console mặc định trên Windows không in được tiếng Việt.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "project",
        type=Path,
        help="đường dẫn tới thư mục capstone của bạn",
    )
    args = parser.parse_args()

    root = args.project.resolve()
    if not root.is_dir():
        print(f"Week 15 capstone readiness: FAIL — không tìm thấy thư mục {root}")
        return 1

    files = python_files(root)
    problems = [
        *check_documents(root),
        *check_decomposition(files),
        *check_bare_except(files),
        *check_tests(root, files),
    ]

    if problems:
        print("Week 15 capstone readiness: FAIL")
        for problem in problems:
            print(f"- {problem}")
        print("\nTham chiếu rubric chính thức: FINAL_PROJECT.md")
        return 1

    print("Week 15 capstone readiness: PASS")
    print("Mechanical evidence đủ. Rubric và review do người chấm quyết định.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
