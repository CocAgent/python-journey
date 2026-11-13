"""CLI for opt-in local formative grading, never a server-side sandbox."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .report import grade_week01

ROOT = Path(__file__).resolve().parents[2]
WEEK = "weeks/week-01-hello-python"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Python Journey — AutoGrade tự luyện")
    parser.add_argument("command", choices=["grade"])
    parser.add_argument("--week", choices=["01"], required=True)
    parser.add_argument("--submission", type=Path, default=ROOT, help="Thư mục gốc chứa weeks/")
    parser.add_argument("--mode", choices=["student", "reference"], default="student")
    parser.add_argument("--acknowledge-local-code", action="store_true", help="Xác nhận chỉ thực thi code đáng tin trên máy của mình")
    parser.add_argument("--json-out", type=Path, help="Xuất báo cáo JSON (không tự gửi lên mạng)")
    args = parser.parse_args(argv)
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
