"""Teaching CLI that calls the network-free bot core."""

import argparse
import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parent
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.adapter import course_local_action  # noqa: E402


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments, optionally from a supplied list for testing."""
    parser = argparse.ArgumentParser(description="Run a course-local decision")
    parser.add_argument("--position", type=int, required=True)
    parser.add_argument("--goal", type=int, required=True)
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    print(course_local_action({"position": args.position, "goal": args.goal}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
