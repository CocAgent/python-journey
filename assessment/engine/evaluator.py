"""Week 01 observable behaviour and light AST evidence (not plagiarism detection)."""

from __future__ import annotations

import ast
import math
import re
from dataclasses import dataclass

from .runner import RunResult


@dataclass(frozen=True)
class Evaluation:
    passed: bool
    reason: str


def _operator_present(tree: ast.AST, *operators: type[ast.operator]) -> bool:
    return any(isinstance(node.op, operators) for node in ast.walk(tree) if isinstance(node, ast.BinOp))


def _number_lines(stdout: str) -> list[list[float]]:
    result = []
    for line in stdout.splitlines():
        # Remove thousand separators, while retaining decimals.
        line = re.sub(r"(?<=\d),(?=\d{3}(?:\D|$))", "", line)
        result.append([float(s) for s in re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])", line)])
    return result


def _contains_number(lines: list[list[float]], expected: float) -> bool:
    return any(math.isclose(number, expected, abs_tol=0.011, rel_tol=0) for row in lines for number in row)


def _print_statements(tree: ast.AST) -> bool:
    return any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "print"
        for node in ast.walk(tree)
    )


def evaluate(check_id: str, stdout: str, tree: ast.AST) -> Evaluation:
    """Dispatch criterion IDs to a typed, reusable evaluator registry."""
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    numbers = _number_lines(stdout)
    if not _print_statements(tree):
        return Evaluation(False, "Chưa phát hiện lệnh print() thực thi được.")

    if check_id == "W01.HELLO":
        valid = "Hello, World!" in lines
    elif check_id == "W01.NAME":
        text_lines = [
            line for line in lines
            if line != "Hello, World!" and not re.fullmatch(r"[ *]+", line)
        ]
        valid = len(text_lines) >= 4 and bool(re.search(r"[A-Za-zÀ-ỹ]", text_lines[0]))
    elif check_id == "W01.INTERESTS":
        text_lines = [
            line for line in lines
            if line != "Hello, World!" and not re.fullmatch(r"[ *]+", line)
        ]
        valid = len(text_lines) >= 4 and len(set(text_lines[1:4])) == 3
    elif check_id == "W01.RECTANGLE":
        valid = any(lines[i:i + 4] == ["*****", "*   *", "*   *", "*****"] for i in range(max(0, len(lines) - 3)))
    elif check_id == "W01.SUM":
        valid = _contains_number(numbers, 3024) and _operator_present(tree, ast.Add)
    elif check_id == "W01.BALANCE":
        valid = _contains_number(numbers, 45000) and _operator_present(tree, ast.Sub) and _operator_present(tree, ast.Mult)
    elif check_id == "W01.AREA":
        valid = _contains_number(numbers, 153.94) and _operator_present(tree, ast.Pow) and _operator_present(tree, ast.Mult)
    elif check_id == "W01.QUOTIENT":
        valid = _contains_number(numbers, 14) and _operator_present(tree, ast.FloorDiv)
    elif check_id == "W01.REMAINDER":
        valid = _contains_number(numbers, 2) and _operator_present(tree, ast.Mod)
    elif check_id in {"W01.FRAME", "W01.MESSAGE"}:
        frames = []
        for i in range(len(lines) - 2):
            top, middle, bottom = lines[i:i + 3]
            if re.fullmatch(r"\+-{2,}\+", top) and bottom == top:
                frames.append((top, middle))
        if check_id == "W01.FRAME":
            valid = any(len(top) == len(mid) and mid.startswith("|") and mid.endswith("|") for top, mid in frames)
        else:
            valid = any(
                len(top) == len(mid) and mid.startswith("|")
                and mid.endswith("|") and bool(re.search(r"Xin chào", mid, re.IGNORECASE))
                for top, mid in frames
            )
    else:
        raise ValueError(f"Mã tiêu chí chưa được hỗ trợ: {check_id}")
    return Evaluation(bool(valid), "Đạt tiêu chí." if valid else "Chưa đáp ứng yêu cầu đầu ra hoặc cấu trúc mã.")


def check_file(check_id: str, code: str, result: RunResult) -> Evaluation:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return Evaluation(False, "Lỗi cú pháp Python: kiểm tra SyntaxError.")
    if result.error == "TIMEOUT":
        return Evaluation(False, "Chương trình quá thời gian chạy. Hãy kiểm tra vòng lặp hoặc input().")
    if result.error:
        return Evaluation(False, "Không thể chạy chương trình trên máy cục bộ.")
    if result.returncode != 0:
        return Evaluation(False, "Chương trình phát sinh lỗi chạy; xem traceback trên máy.")
    return evaluate(check_id, result.stdout, tree)
