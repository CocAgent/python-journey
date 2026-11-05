"""Run reference Bot V1 against all three course-local baselines."""

import sys
from pathlib import Path

REFERENCE_DIR = Path(__file__).resolve().parent
REPO_ROOT = REFERENCE_DIR.parents[2]
PROJECT_ROOT = REPO_ROOT / "projects" / "vuacoc-bot-journey"
for path in (REFERENCE_DIR, PROJECT_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from baselines.cautious_bot import choose_action as cautious_bot  # noqa: E402
from baselines.forward_bot import choose_action as forward_bot  # noqa: E402
from baselines.wait_bot import choose_action as wait_bot  # noqa: E402
from bot_v1 import choose_action as bot_v1  # noqa: E402
from local_arena.arena import run_match  # noqa: E402

BASELINES = (
    ("WaitBot", wait_bot),
    ("ForwardBot", forward_bot),
    ("CautiousBot", cautious_bot),
)


def observed_strength(winner: str | None) -> str:
    """Describe one fact visible in a completed match."""
    if winner == "A":
        return "Reached its course-local goal"
    return "Returned legal actions until termination"


def observed_weakness(winner: str | None) -> str:
    """Describe one bounded limitation without a statistical claim."""
    if winner == "B":
        return "Did not reach its goal before the opponent"
    return "Uses only distance and goal direction"


def evaluate() -> list[dict[str, object]]:
    """Return one evidence record for each deterministic baseline."""
    records: list[dict[str, object]] = []
    for opponent_name, opponent_bot in BASELINES:
        result = run_match(bot_v1, opponent_bot)
        records.append(
            {
                "opponent": opponent_name,
                "result": result.winner or "draw",
                "turn_count": len(result.turns),
                "strength": observed_strength(result.winner),
                "weakness": observed_weakness(result.winner),
                "status": result.status,
            }
        )
    return records


def main() -> int:
    """Print reproducible baseline evidence."""
    print("COURSE_LOCAL_ONLY = YES")
    print("VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED")
    for record in evaluate():
        print(
            f"{record['opponent']}: result={record['result']}, "
            f"turns={record['turn_count']}, status={record['status']}"
        )
        print(f"  strength: {record['strength']}")
        print(f"  weakness: {record['weakness']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
