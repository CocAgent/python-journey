"""Single-entry Week 02 formative grader with a separate audited test bank.

No sandbox is provided. Run only your own/trusted local exercise code.
Generated reports stay local and are gitignored by reports/.gitignore.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from autograde_w02 import ROOT, WEEK, grade, test_suite_audit
from student_journey import render_report

DEFAULT_REPORT = ROOT / "reports" / "week02-journey.html"
DEFAULT_JSON = ROOT / "reports" / "week02-result.json"


def submission_exercises(location: Path) -> Path:
    """Accept an exercises/ folder, week folder, or complete repository copy."""
    folder = location.expanduser().resolve()
    candidates = (
        folder,
        folder / "exercises",
        folder / "weeks" / "week-02-variables-types" / "exercises",
    )
    required = {"ex01_variables.py", "ex02_type_conversion.py", "ex03_input_calc.py"}
    for candidate in candidates:
        if candidate.is_dir() and all((candidate / f).is_file() for f in required):
            return candidate
    raise ValueError(
        "Không tìm thấy đủ 3 file exercises/ Week 02 trong thư mục bài làm."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Week02: kiểm toán TOÀN BỘ tập test hoặc tự chấm 3 exercises gốc."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--student", action="store_true", help="Chấm code của sinh viên")
    mode.add_argument("--reference", action="store_true", help="Chạy fixture tin cậy của giảng viên")
    mode.add_argument(
        "--audit-tests", action="store_true",
        help="Kiểm tra toàn bộ 3 file test case và 10 tiêu chí, KHÔNG chạy bài sinh viên",
    )
    parser.add_argument(
        "--submission", type=Path,
        help="Thư mục bài làm/exercises hoặc bản sao của repository (chỉ local và tin cậy)",
    )
    parser.add_argument(
        "--acknowledge-local-code", action="store_true",
        help="Xác nhận đã tin cậy code trong --submission, biết rằng không có sandbox",
    )
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args(argv)

    try:
        audit = test_suite_audit()
        if args.audit_tests:
            if args.submission:
                parser.error("--audit-tests không nhận --submission")
            print(json.dumps(audit, ensure_ascii=False, indent=2))
            return 0

        if args.reference and args.submission:
            parser.error("--reference không nhận --submission")
        if args.submission and not args.acknowledge_local_code:
            parser.error(
                "Chỉ chấm thư mục ngoại vi khi có --acknowledge-local-code; "
                "subprocess KHÔNG phải sandbox."
            )
        source = (
            ROOT / "fixtures" / "reference" if args.reference
            else submission_exercises(args.submission)
            if args.submission else WEEK / "exercises"
        )
        result = grade(source, "reference" if args.reference else "student")
        target = args.report.expanduser().resolve()
        output_json = args.json_out.expanduser().resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        output_json.parent.mkdir(parents=True, exist_ok=True)

        # Keep links correct for reports/; do not link external student paths.
        prefix: str | None = "../../../exercises/" if (
            source == WEEK / "exercises"
        ) else None
        target.write_text(
            render_report(result, exercise_href_prefix=prefix), encoding="utf-8"
        )
        output_json.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except (OSError, ValueError) as error:
        print(f"Không thể chấm: {error}")
        return 2

    print("=== WEEK 02 · KIỂM TRA BÀI TẬP GỐC ===")
    print(
        f"Bộ test: {audit['exercises_count']} bài / "
        f"{audit['criteria_count']} TODO / "
        f"{audit['dynamic_case_count']} trường hợp input."
    )
    for item in result["tasks"]:
        print(f"{item['title']}:")
        for check in item["criteria"]:
            state = (
                "PASS" if check["passed"] else
                "REVIEW" if check["reason"].startswith("REVIEW:") else "RETRY"
            )
            print(
                f"  {state} · TODO {check['todo']}: "
                f"{check['earned']:.2f}/{check['maximum']:.2f} — {check['reason']}"
            )
    print(f"Điểm tự luyện: {result['auto_score']:.2f}/10")
    print("Điểm chính thức: chưa có — chờ giảng viên phản biện.")
    print(f"HTML: {target}\nJSON: {output_json}")
    return 0 if result["auto_score"] == 10 else 1


if __name__ == "__main__":
    raise SystemExit(main())
