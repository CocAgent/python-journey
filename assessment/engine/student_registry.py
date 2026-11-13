"""Registry of *existing* learner-owned checkers; never grade reference solutions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class StudentCheck:
    week: str
    directory: str
    focus: str
    scope: str
    argv: tuple[str, ...] | None
    cwd: str = "."
    extra: str = ""


def _practice(week: str, directory: str, focus: str) -> StudentCheck:
    return StudentCheck(
        week=week,
        directory=directory,
        focus=focus,
        scope="practice/starter/ — bài luyện bổ sung, KHÔNG chấm toàn bộ exercises/.",
        argv=(f"weeks/{directory}/practice/checks/check_practice.py", "--starter"),
        extra="Lời giải --solutions và checks/check_solutions.py KHÔNG phải bài sinh viên.",
    )


CHECKS: dict[str, StudentCheck] = {
    "02": _practice("02", "week-02-variables-types", "Biến, kiểu dữ liệu, input và conversion"),
    "03": _practice("03", "week-03-conditionals", "if/elif/else, boolean và validation"),
    "04": _practice("04", "week-04-strings", "Chuỗi, strip/split và regex"),
    "05": _practice("05", "week-05-lists-tuples", "Danh sách, slicing và tuple"),
    "06": _practice("06", "week-06-loops", "for, while, break/continue"),
    "07": _practice("07", "week-07-functions", "Hàm, return, tham số, scope"),
    "08": _practice("08", "week-08-dicts-sets", "Dictionary, set và state"),
    "09": StudentCheck(
        week="09",
        directory="week-09-midterm-project",
        focus="Midterm project (track A/B/C)",
        scope="Dự án cá nhân/nhóm và evidence theo rubric 10 điểm.",
        argv=None,
        extra="Không có checker chấm chung mọi dự án. Dùng rubric và demo của giảng viên.",
    ),
    "10": _practice("10", "week-10-files-io", "File UTF-8, CSV, JSON"),
    "11": _practice("11", "week-11-exceptions", "Exceptions, raise/else/finally"),
    "12": StudentCheck(
        week="12",
        directory="week-12-testing-pytest",
        focus="Kiểm tra chất lượng bốn test do sinh viên viết",
        scope="exercises/test_decision_starter.py, kiểm mutation bằng checker tuần.",
        argv=("weeks/week-12-testing-pytest/checks/check_student_tests.py",),
        extra="Cần pytest. Không dùng checks/check_week.py để chấm sinh viên.",
    ),
    "13": StudentCheck(
        week="13",
        directory="week-13-modules-cli-api",
        focus="Module, CLI, HTTP mô phỏng, adapter",
        scope="practice/starter/ (bốn lab bổ sung); không chấm exercises/ gốc.",
        argv=("-m", "practice.checks.check_lab", "--starter"),
        cwd="weeks/week-13-modules-cli-api",
        extra="Chạy module trong thư mục Week 13; không cần Internet/API key.",
    ),
    "14": StudentCheck(
        week="14",
        directory="week-14-oop-essentials",
        focus="OOP, composition, inheritance",
        scope="exercises/ — bốn bài được learner_tests kiểm trực tiếp.",
        argv=("weeks/week-14-oop-essentials/checks/check_student.py",),
        extra="Cần pytest. Mini-project và phần giải thích vẫn do giảng viên duyệt.",
    ),
    "15": StudentCheck(
        week="15",
        directory="week-15-capstone-project",
        focus="Capstone readiness (không tự chấm điểm)",
        scope="Thư mục dự án chỉ định bởi --project.",
        argv=("weeks/week-15-capstone-project/checks/check_capstone_readiness.py",),
        extra="Bắt buộc --project. Checker có pytest --collect-only và chưa chấm rubric.",
    ),
}


def find(week: str) -> StudentCheck | None:
    return CHECKS.get(week)


def week_readme(week: str) -> Path:
    item = find(week)
    if item is None:
        raise ValueError(f"Chưa có cấu hình tự kiểm cho Week {week}.")
    return REPO_ROOT / "weeks" / item.directory / "assessment" / "STUDENT-GUIDE.md"
