"""Behavioral check for the Week 09 Bot V1 reference track."""

import sys
from pathlib import Path

CHECKS_DIR = Path(__file__).resolve().parent
REPO_ROOT = CHECKS_DIR.parents[2]
PROJECT_ROOT = REPO_ROOT / "projects" / "vuacoc-bot-journey"
REFERENCE_DIR = CHECKS_DIR.parent / "reference"
for path in (PROJECT_ROOT, REFERENCE_DIR):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from bot_v1 import LOCAL_ACTIONS, choose_action  # noqa: E402
from evaluate_baselines import BASELINES, evaluate  # noqa: E402
from local_arena.arena import run_match  # noqa: E402


def check_bot_callable_and_actions() -> None:
    """Check interface and representative structured states."""
    if not callable(choose_action):
        raise AssertionError("choose_action must be callable")
    states = (
        {"position": 0, "opponent_position": 4, "goal": 4},
        {"position": 4, "opponent_position": 2, "goal": 4},
        {"position": 3, "goal": 0},
    )
    for state in states:
        action = choose_action(state)
        if action not in LOCAL_ACTIONS:
            raise AssertionError(f"illegal course-local action: {action!r}")


def check_matches_complete() -> None:
    """Check bounded completion against exactly three baselines."""
    if len(BASELINES) != 3:
        raise AssertionError(f"expected 3 baselines, got {len(BASELINES)}")
    for name, baseline in BASELINES:
        result = run_match(choose_action, baseline)
        if result.status != "completed":
            raise AssertionError(f"match with {name} did not complete")
        if len(result.turns) > result.max_turns:
            raise AssertionError(f"match with {name} exceeded max_turns")


def check_evaluation_records() -> None:
    """Check the evaluator produces the required evidence fields."""
    records = evaluate()
    if len(records) != 3:
        raise AssertionError(f"expected 3 records, got {len(records)}")
    required = {"opponent", "result", "turn_count", "strength", "weakness"}
    for record in records:
        missing = required - record.keys()
        if missing:
            raise AssertionError(f"evaluation record missing: {sorted(missing)}")


def main() -> int:
    """Run reference checks and return a process exit code."""
    try:
        check_bot_callable_and_actions()
        check_matches_complete()
        check_evaluation_records()
    except (AssertionError, AttributeError, RuntimeError) as error:
        print(f"Week 09 midterm reference checks: FAIL — {error}")
        return 1

    print("Week 09 midterm reference checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
