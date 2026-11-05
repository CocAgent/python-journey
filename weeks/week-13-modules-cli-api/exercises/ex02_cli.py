"""Exercise 02: add one argparse option to a small CLI."""

import argparse


def parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    result = argparse.ArgumentParser(description="Inspect a turn number")
    result.add_argument("--turn", type=int, required=True, help="positive turn number")
    return result


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    args = parser().parse_args()
    if args.turn < 1:
        raise SystemExit("--turn must be a positive integer")
    print(f"turn={args.turn}")


if __name__ == "__main__":
    main()
