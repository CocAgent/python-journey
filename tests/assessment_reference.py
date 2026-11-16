"""Mẫu kiểm tra kết quả cho giáo trình; KHÔNG phải hệ thống chấm thi.

Các ví dụ chỉ sử dụng chương trình mẫu đáng tin cậy do maintainer tự tạo.
Không chạy bài nộp của sinh viên hoặc script lấy từ Drive trong GitHub Actions.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path


@dataclass(frozen=True)
class RunResult:
    """Tách rõ stdout, stderr, mã thoát và trạng thái quá thời gian."""

    returncode: int | None
    stdout: str
    stderr: str
    timed_out: bool = False


def output_matches(result: RunResult, expected_lines: tuple[str, ...]) -> bool:
    """Chỉ nhận đúng toàn bộ dòng và quá trình kết thúc thành công.

    Không dùng phép tìm chuỗi con: "1" không được coi là khớp "100".
    Chỉ bỏ khoảng trắng cuối dòng và ký tự xuống dòng kết thúc output.
    """
    if not expected_lines:
        raise ValueError("expected_lines must not be empty")
    if result.timed_out or result.returncode != 0:
        return False
    actual = tuple(line.rstrip() for line in result.stdout.splitlines())
    expected = tuple(line.rstrip() for line in expected_lines)
    return actual == expected


def question_score(passed_cases: tuple[bool, ...]) -> Decimal:
    """Mỗi câu có tối đa 2 điểm; chia đều theo số case có minh chứng.

    Đây là minh họa CHÍNH SÁCH chấm 5 câu x 2 điểm từ đề tổng hợp.
    Không mặc định áp dụng cho bài thi thực tế khi chưa duyệt rubric riêng.
    """
    if not passed_cases:
        raise ValueError("A question must contain at least one test case")
    if any(type(passed) is not bool for passed in passed_cases):
        raise TypeError("Every test outcome must be a boolean")
    passed_count = sum(passed_cases)
    return (
        Decimal("2") * Decimal(passed_count) / Decimal(len(passed_cases))
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def illustrative_exam_score(questions: tuple[tuple[bool, ...], ...]) -> Decimal:
    """Đúng 5 câu, mỗi câu 2 điểm: tổng không vượt 10."""
    if len(questions) != 5:
        raise ValueError("Exactly five questions are required")
    return sum((question_score(cases) for cases in questions), Decimal("0"))


def run_trusted_example(
    script: Path, *, stdin: str = "", timeout_seconds: float = 2.0
) -> RunResult:
    """Chạy CHỈ mã ví dụ đã được review, không phải sandbox an toàn.

    -I chỉ cô lập đường dẫn/module Python, KHÔNG cấm đọc tệp hoặc gọi mạng.
    Chỉ gọi hàm này với mã kiểm thử tự tạo trong môi trường CI tin cậy.
    """
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")
    if not script.is_file():
        raise FileNotFoundError(script)
    try:
        result = subprocess.run(
            [sys.executable, "-I", "-B", str(script.resolve())],
            cwd=script.parent,
            input=stdin,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or b""
        stderr = exc.stderr or b""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        return RunResult(None, stdout, stderr, timed_out=True)
    return RunResult(result.returncode, result.stdout, result.stderr)
