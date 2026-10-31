"""Mechanical readiness audit for a learner capstone.

FINAL_PROJECT.md owns requirements and the only rubric. This script checks
mechanical evidence only. It does not grade design quality, feature quality or
code understanding, and it intentionally does not impose function/class quotas.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from pathlib import Path

MIN_TESTS = 5

README_REQUIREMENTS: dict[str, tuple[str, ...]] = {
    "problem/scope": ("vấn đề", "phạm vi", "problem", "scope"),
    "features": ("chức năng", "feature"),
    "run/setup": ("cài đặt", "setup", "usage", "chạy", "run"),
    "tests": ("test", "kiểm thử"),
    "design/structure": ("thiết kế", "design", "cấu trúc", "structure"),
}


def python_files(root: Path) -> list[Path]:
    """Return project Python files, skipping environments and generated dirs."""
    skip = {
        ".venv",
        "venv",
        "env",
        "__pycache__",
        ".git",
        ".pytest_cache",
        ".ruff_cache",
        "build",
        "dist",
    }
    return [
        path
        for path in sorted(root.rglob("*.py"))
        if not skip.intersection(path.parts)
    ]


def parse_python(path: Path) -> tuple[ast.Module | None, str | None]:
    """Parse one Python file and preserve a readable syntax/encoding error."""
    try:
        text = path.read_text(encoding="utf-8")
        return ast.parse(text), None
    except (SyntaxError, UnicodeDecodeError) as error:
        return None, str(error)


def check_documents(root: Path) -> list[str]:
    """Report missing core documents and README evidence areas."""
    problems: list[str] = []
    readme = root / "README.md"

    if not readme.is_file():
        problems.append("thiếu README.md")
    else:
        text = readme.read_text(encoding="utf-8", errors="replace").lower()
        for label, aliases in README_REQUIREMENTS.items():
            if not any(alias in text for alias in aliases):
                problems.append(f"README.md chưa có evidence cho: {label}")

    ai_usage = root / "AI_USAGE.md"
    if not ai_usage.is_file():
        problems.append("thiếu AI_USAGE.md")
    elif not ai_usage.read_text(encoding="utf-8", errors="replace").strip():
        problems.append("AI_USAGE.md đang rỗng")

    return problems


def check_source_and_syntax(files: list[Path]) -> list[str]:
    """Require Python source and report every file that cannot be parsed."""
    if not files:
        return ["không tìm thấy Python source (*.py)"]

    problems: list[str] = []
    for path in files:
        _tree, error = parse_python(path)
        if error is not None:
            problems.append(f"syntax/encoding lỗi tại {path}: {error}")
    return problems


def check_bare_except(files: list[Path]) -> list[str]:
    """Report bare except clauses forbidden by the canonical capstone spec."""
    problems: list[str] = []
    for path in files:
        tree, error = parse_python(path)
        if tree is None or error is not None:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                problems.append(f"bare except tại {path}:{node.lineno}")
    return problems


def test_files_and_count(files: list[Path]) -> tuple[list[Path], int]:
    """Return test modules and the number of test functions."""
    test_files = [
        path
        for path in files
        if path.name.startswith("test_") or path.name.endswith("_test.py")
    ]
    count = 0

    for path in test_files:
        tree, error = parse_python(path)
        if tree is None or error is not None:
            continue
        count += sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name.startswith("test_")
            for node in ast.walk(tree)
        )

    return test_files, count


def run_pytest(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    """Run pytest in the learner project."""
    return subprocess.run(
        [sys.executable, "-m", "pytest", *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )


def check_tests(root: Path, files: list[Path], run_tests: bool) -> list[str]:
    """Check test count, collection, and optionally execute the test suite."""
    problems: list[str] = []
    test_files, test_functions = test_files_and_count(files)

    if test_functions < MIN_TESTS:
        problems.append(f"chỉ tìm thấy {test_functions} test, cần >= {MIN_TESTS}")

    if not test_files:
        return problems

    collected = run_pytest(root, ["--collect-only", "-q"])
    if collected.returncode != 0:
        problems.append("pytest không collect được test (xem lỗi import/syntax)")
        return problems

    if run_tests:
        executed = run_pytest(root, ["-q"])
        if executed.returncode != 0:
            problems.append("pytest chạy nhưng test suite chưa PASS")

    return problems


def main() -> int:
    """Audit a capstone directory and return a process exit code."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "project",
        type=Path,
        help="đường dẫn tới thư mục capstone của bạn",
    )
    parser.add_argument(
        "--run-tests",
        action="store_true",
        help="chạy pytest thật; chỉ dùng với project/code bạn tin cậy",
    )
    args = parser.parse_args()

    root = args.project.resolve()
    if not root.is_dir():
        print(f"Week 15 capstone readiness: FAIL — không tìm thấy thư mục {root}")
        return 1

    files = python_files(root)
    problems = [
        *check_documents(root),
        *check_source_and_syntax(files),
        *check_bare_except(files),
        *check_tests(root, files, args.run_tests),
    ]

    if problems:
        print("Week 15 capstone readiness: FAIL")
        for problem in problems:
            print(f"- {problem}")
        print("\nTham chiếu rubric chính thức: FINAL_PROJECT.md")
        return 1

    print("Week 15 capstone readiness: PASS")
    if args.run_tests:
        print("Mechanical evidence đủ và test suite PASS.")
    else:
        print("Mechanical evidence đủ; dùng --run-tests để chạy test suite.")
    print("Rubric và review chất lượng vẫn do FINAL_PROJECT.md/người chấm quyết định.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
