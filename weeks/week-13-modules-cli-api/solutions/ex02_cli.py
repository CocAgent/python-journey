"""Lời giải 02 — argparse đọc tham số có tên."""

import argparse


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Đếm lượt học tập")
    result.add_argument("--turn", type=int, required=True, help="số lượt")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.turn < 0:
        parser().error("--turn phải >= 0")
    print("Lượt:", args.turn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
