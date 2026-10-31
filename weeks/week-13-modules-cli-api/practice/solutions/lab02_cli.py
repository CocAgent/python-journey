"""Lab 2 solution: argparse chỉ parse kiểu, core kiểm giá trị."""

from __future__ import annotations

import argparse
import json
import sys

from practice.study_core import status_for_score


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Báo cáo điểm (offline demo)")
    parser.add_argument("--score", type=float, required=True, help="Điểm 0..10")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    try:
        result = {"score": args.score, "status": status_for_score(args.score)}
    except ValueError as error:
        print(f"Lỗi: {error}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
