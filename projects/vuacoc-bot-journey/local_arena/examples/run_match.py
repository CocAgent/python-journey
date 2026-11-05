"""Run the stable ForwardBot versus WaitBot example."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def main() -> None:
    """Run and print one deterministic evidence match."""
    from baselines.forward_bot import choose_action as forward_bot
    from baselines.wait_bot import choose_action as wait_bot
    from local_arena.arena import run_match
    from local_arena.replay import concise_summary

    result = run_match(forward_bot, wait_bot)
    print("EXAMPLE = ForwardBot vs WaitBot")
    print(concise_summary(result))


if __name__ == "__main__":
    main()
