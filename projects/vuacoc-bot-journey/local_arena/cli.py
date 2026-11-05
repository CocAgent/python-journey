"""Small CLI for course-local Line Arena matches."""

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def bot_registry() -> dict[str, object]:
    """Return the fixed local bot selections."""
    from baselines.cautious_bot import choose_action as cautious_bot
    from baselines.forward_bot import choose_action as forward_bot
    from baselines.wait_bot import choose_action as wait_bot
    from student_bot.bot import choose_action as student_bot

    return {
        "wait": wait_bot,
        "forward": forward_bot,
        "cautious": cautious_bot,
        "student": student_bot,
    }


def parse_args() -> argparse.Namespace:
    """Parse a minimal fixed-selection CLI."""
    parser = argparse.ArgumentParser(description="Run a course-local Line Arena match")
    choices = tuple(bot_registry())
    parser.add_argument("--bot-a", choices=choices, default="forward")
    parser.add_argument("--bot-b", choices=choices, default="wait")
    parser.add_argument("--max-turns", type=int, default=6)
    parser.add_argument("--replay", action="store_true")
    return parser.parse_args()


def main() -> int:
    """Run a selected local match and print result evidence."""
    from local_arena.arena import run_match
    from local_arena.replay import concise_summary

    args = parse_args()
    bots = bot_registry()
    result = run_match(bots[args.bot_a], bots[args.bot_b], args.max_turns)

    print("COURSE_LOCAL_ARENA = YES")
    print("VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED")
    print(
        f"{args.bot_a} vs {args.bot_b}: "
        f"status={result.status} winner={result.winner} reason={result.reason}"
    )
    if args.replay:
        print(concise_summary(result))
    return 0 if result.status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
