"""CLI dùng argparse: nhập dữ liệu → adapter → in JSON ra terminal."""

import argparse
import json
import sys

from bot_course.adapter import course_local_action


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """argv tùy chọn giúp test parser mà không cần mở terminal."""
    parser = argparse.ArgumentParser(
        description="Bot demo offline — vị trí từ 0 đến 4 (course-local)"
    )
    parser.add_argument("--position", type=int, required=True, help="vị trí hiện tại")
    parser.add_argument("--goal", type=int, required=True, help="vị trí đích")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Trả exit code 0 khi thành công, 2 cho input sai."""
    args = parse_args(argv)
    try:
        result = course_local_action({"position": args.position, "goal": args.goal})
    except ValueError as error:
        print(f"Lỗi dữ liệu: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
