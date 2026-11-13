"""CLI for opt-in local formative grading, never a server-side sandbox."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .report import grade_week01
from .student_registry import find, week_readme
from .student_selfcheck import selfcheck, write_report

ROOT = Path(__file__).resolve().parents[2]
WEEK = "weeks/week-01-hello-python"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Python Journey — AutoGrade tự luyện")
    parser.add_argument("command", choices=["grade", "selfcheck", "guide"])
    parser.add_argument("--week", choices=[f"{n:02d}" for n in range(1, 16)], required=True)
    parser.add_argument("--submission", type=Path, default=ROOT, help="Chỉ áp dụng cho chấm Week 01")
    parser.add_argument("--mode", choices=["student", "reference"], default="student")
    parser.add_argument("--acknowledge-local-code", action="store_true", help="Xác nhận chỉ thực thi code đáng tin trên máy của mình")
    parser.add_argument("--json-out", type=Path, help="Xuất báo cáo JSON cục bộ")
    parser.add_argument("--project", type=Path, help="Thư mục capstone cá nhân — Week 15")
    parser.add_argument("--run-tests", action="store_true", help="Week 15: chạy pytest thật trên project đã tin cậy")
    args = parser.parse_args(argv)

    if args.command == "guide":
        if args.mode != "student" or args.project or args.run_tests or args.json_out:
            parser.error("guide chỉ hiện tài liệu; không chấp nhận tham số chấm hoặc xuất báo cáo.")
        if args.week == "01":
            guide = ROOT / WEEK / "assessment" / "STUDENT-GUIDE.md"
            print(f"Week 01: {guide}")
            print("Chấm bài thật: python -m assessment grade --week 01 --acknowledge-local-code")
            return 0
        spec = find(args.week)
        if spec is None:
            parser.error("Không tìm được tuần này.")
        print(f"Week {args.week}: {spec.focus}")
        print(f"Hướng dẫn: {week_readme(args.week)}")
        print(f"Phạm vi: {spec.scope}")
        print(spec.extra)
        if spec.week == "09":
            print("Đọc rubric dự án; không có một lệnh tự chấm điểm chung.")
        elif spec.week == "15":
            print("Lệnh: python -m assessment selfcheck --week 15 --project DUONG_DAN --acknowledge-local-code")
        else:
            print(f"Lệnh: python -m assessment selfcheck --week {args.week} --acknowledge-local-code")
        return 0

    if args.mode != "student" and (args.command == "selfcheck" or args.week != "01"):
        parser.error("Reference mode chỉ hỗ trợ lệnh grade của Week 01.")
    if args.command == "grade" and args.week != "01":
        parser.error("Chấm điểm số mới hỗ trợ Week 01; tuần khác dùng selfcheck không quy đổi điểm.")
    if args.command == "selfcheck" and args.week != "01":
        if args.submission.resolve() != ROOT:
            parser.error("--submission không áp dụng cho checker các tuần 02–15.")
        if not args.acknowledge_local_code:
            parser.error("Tự kiểm mã học viên phải có --acknowledge-local-code; không chạy mã lạ.")
        spec = find(args.week)
        if spec is None or spec.argv is None:
            parser.error("Week 09/chặng dự án chưa có checker chung; đọc hướng dẫn và rubric.")
        try:
            code, result = selfcheck(spec, project=args.project, run_tests=args.run_tests)
            if args.json_out:
                write_report(result, args.json_out)
        except (OSError, ValueError) as exc:
            print(f"AutoGrade: không thể tự kiểm — {exc}", file=sys.stderr)
            return 2
        print(f"Tuần {args.week} — chỉ kiểm: {spec.scope}")
        if result["checker_stdout"]:
            print(result["checker_stdout"])
        if result["checker_stderr"]:
            print(result["checker_stderr"], file=sys.stderr)
        print(f"Tự kiểm: {result['status']} (không quy đổi thành điểm học phần).")
        print("Giảng viên vẫn cần duyệt bài tập gốc, mini-project và minh chứng.")
        return code

    if args.project is not None or args.run_tests:
        parser.error("--project/--run-tests chỉ dành cho selfcheck Week 15.")
    if args.mode == "student" and not args.acknowledge_local_code:
        parser.error("Chấm mã sinh viên yêu cầu --acknowledge-local-code. Đừng chạy mã lạ trên máy có bí mật.")
    base = (ROOT / "assessment" / "fixtures" / "week01" / "reference") if args.mode == "reference" else args.submission.resolve()
    rubric = ROOT / WEEK / "assessment" / "rubric.json"
    try:
        result = grade_week01(base, rubric, reference=args.mode == "reference")
        if args.json_out:
            target = args.json_out.resolve()
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"AutoGrade: không thể đánh giá — {exc}", file=sys.stderr)
        return 2
    print(f"Chế độ: {result['mode'].upper()} — Week 01")
    for task in result["tasks"]:
        for check in task["checks"]:
            icon = "PASS" if check["passed"] else "RETRY"
            print(f"  {icon} {check['id']}: {check['earned']:.2f}/{check['maximum']:.2f} — {check['label']}")
            if check["hint"]:
                print(f"    Gợi ý: {check['hint']}")
    print(f"Điểm tự động: {result['auto_score']:.2f}/5.00; chờ giảng viên: tối đa 5.00 điểm.")
    print("Đây chỉ là kết quả tự luyện, không phải điểm chính thức.")
    return 0 if result["auto_score"] == result["auto_max_points"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
