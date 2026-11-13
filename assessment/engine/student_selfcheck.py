"""Run learner-owned *local* self-check commands; NOT an isolation sandbox."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from .student_registry import REPO_ROOT, StudentCheck


def selfcheck(
    spec: StudentCheck,
    *,
    project: Path | None = None,
    run_tests: bool = False,
    timeout_seconds: int = 180,
) -> tuple[int, dict[str, object]]:
    """Run only a registry-defined command on a learner's trusted checkout.

    Existing course scripts can import/run learner code. No CI/server should
    call this against third-party submissions without a real sandbox.
    """
    if spec.argv is None:
        raise ValueError("Tuần này dùng rubric dự án, chưa có self-check chung.")
    if spec.week == "15" and project is None:
        raise ValueError("Week 15 yêu cầu --project /duong/dan/du-an-cua-em.")
    if spec.week != "15" and project is not None:
        raise ValueError("--project chỉ dành cho Week 15.")
    if spec.week != "15" and run_tests:
        raise ValueError("--run-tests chỉ dành cho Week 15.")

    command = [sys.executable, "-B", *spec.argv]
    if project is not None:
        command.append(str(project.resolve()))
        if run_tests:
            command.append("--run-tests")
    cwd = (REPO_ROOT / spec.cwd).resolve()
    environment = {
        key: value
        for key, value in os.environ.items()
        if key in {"PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "LANG", "LC_ALL"}
    }
    environment["PYTHONNOUSERSITE"] = "1"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"

    try:
        process = subprocess.run(
            command,
            cwd=cwd,
            env=environment,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
            check=False,
        )
        returncode = process.returncode
        stdout = process.stdout[-12000:]
        stderr = process.stderr[-4000:]
        status = "PASS" if returncode == 0 else "RETRY"
    except subprocess.TimeoutExpired:
        returncode, stdout, stderr, status = 124, "", "Quá thời gian tự kiểm.", "RETRY"
    except OSError:
        returncode, stdout, stderr, status = 2, "", "Không chạy được Python checker.", "ERROR"

    result: dict[str, object] = {
        "schema_version": "1.0",
        "assessment_type": "formative_student_selfcheck",
        "mode": "student",
        "week_id": f"W{spec.week}",
        "scope": spec.scope,
        "status": status,
        "checker_exit_code": returncode,
        "checker_stdout": stdout,
        "checker_stderr": stderr,
        "auto_score": None,
        "official_score": None,
        "manual_review_required": True,
        "limitations": [
            "PASS chỉ xác nhận phạm vi checker công khai, không chấm toàn tuần.",
            "Không dùng PASS reference làm kết quả sinh viên.",
            "Đầu ra có thể chứa dữ liệu từ bài làm; báo cáo chỉ lưu tại máy.",
            "Subprocess và timeout không phải security sandbox.",
        ],
    }
    return (0 if returncode == 0 else 1), result


def write_report(report: dict[str, object], target: Path) -> None:
    """Output is private/local by default; overwrite only explicit target."""
    destination = target.resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
