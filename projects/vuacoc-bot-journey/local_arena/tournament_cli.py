"""Run the deterministic Week 15 course-local tournament."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from baselines.cautious_bot import choose_action as cautious_bot  # noqa: E402
from baselines.forward_bot import choose_action as forward_bot  # noqa: E402
from baselines.wait_bot import choose_action as wait_bot  # noqa: E402
from student_bot.bot import choose_action as student_bot  # noqa: E402

from local_arena.tournament import evaluate_bot  # noqa: E402


def main() -> int:
    opponents = {
        "wait": wait_bot,
        "forward": forward_bot,
        "cautious": cautious_bot,
    }
    print("COURSE_LOCAL_ONLY = YES")
    print("VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED")
    for row in evaluate_bot(student_bot, opponents):
        print(
            f"student vs {row['opponent']}: {row['outcome']} "
            f"turns={row['turns']} reason={row['reason']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
