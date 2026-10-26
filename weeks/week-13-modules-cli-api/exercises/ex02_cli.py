"""Exercise 02: add one argparse option to a small CLI."""

import argparse


def parser() -> argparse.ArgumentParser:
    """Create a parser with one required integer turn argument."""
    result = argparse.ArgumentParser(description="Inspect a course turn")
    result.add_argument("--turn", type=int, required=True)
    return result


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    print(parser().parse_args())


if __name__ == "__main__":
    main()
