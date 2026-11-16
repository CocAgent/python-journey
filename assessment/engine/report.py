"""Structured formative reporting; manual and official scores are intentionally absent."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .evaluator import check_file
from .runner import run_python

ENGINE_VERSION = "AG01-v1.0"


def _safe_file(base: Path, relative: str) -> Path:
    candidate = (base / relative).resolve()
    if not candidate.is_relative_to(base.resolve()):
        raise ValueError("Đường dẫn bài nộp nằm ngoài thư mục cho phép.")
    return candidate


def load_rubric(rubric_path: Path) -> dict:
    rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
    if rubric.get("schema_version") != "1.0" or rubric.get("week_id") != "W01":
        raise ValueError("Rubric chưa tương thích với AG01.")
    if rubric.get("auto_max_points") != 5 or rubric.get("manual_max_points") != 5:
        raise ValueError("Rubric Week 01 phải giữ 5 điểm tự động + 5 điểm duyệt.")
    criteria = [criterion for task in rubric["tasks"] for criterion in task["criteria"]]
    if len({c["id"] for c in criteria}) != len(criteria):
        raise ValueError("Mã tiêu chí bị trùng.")
    if len(criteria) != 11 or sum(c["points"] for c in criteria) != 5:
        raise ValueError("Thiếu tiêu chí hoặc tổng điểm không hợp lệ.")
    return rubric


def grade_week01(base: Path, rubric_path: Path, *, reference: bool = False) -> dict:
    rubric = load_rubric(rubric_path)
    tasks = []
    passed_count = 0
    scores = []
    for task in rubric["tasks"]:
        path = _safe_file(base, task["path"])
        code = path.read_text(encoding="utf-8") if path.is_file() else ""
        run = run_python(path) if path.is_file() else None
        checks = []
        for criterion in task["criteria"]:
            if run is None:
                reason, passed = "Thiếu tệp bài làm.", False
            else:
                verdict = check_file(criterion["id"], code, run)
                passed, reason = verdict.passed, verdict.reason
            earned = criterion["points"] if passed else 0
            passed_count += int(passed)
            scores.append(earned)
            checks.append({
                "id": criterion["id"],
                "skill": criterion["skill"],
                "label": criterion["label"],
                "passed": passed,
                "earned": earned,
                "maximum": criterion["points"],
                "reason": reason,
                "hint": None if passed else criterion["hint"],
            })
        tasks.append({
            "id": task["id"], "path": task["path"],
            "source_sha256": hashlib.sha256(code.encode("utf-8")).hexdigest() if path.is_file() else None,
            "checks": checks,
        })
    return {
        "engine_version": ENGINE_VERSION,
        "assessment_type": "formative_self_check",
        "mode": "reference" if reference else "student",
        "week_id": rubric["week_id"],
        "rubric_sha256": hashlib.sha256(rubric_path.read_bytes()).hexdigest(),
        "auto_score": round(sum(scores), 2),
        "auto_max_points": rubric["auto_max_points"],
        "manual_score": None,
        "manual_max_points": rubric["manual_max_points"],
        "official_score": None,
        "passed_criteria": passed_count,
        "total_criteria": len(scores),
        "tasks": tasks,
        "limitations": [
            "Điểm máy chỉ phản ánh tiêu chí công khai; không xác nhận tác giả.",
            "Kết quả chấm mẫu không phải điểm sinh viên.",
            "Mã Python không tin cậy phải được chạy trong sandbox thực sự.",
        ],
    }
