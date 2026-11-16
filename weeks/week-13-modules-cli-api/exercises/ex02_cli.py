"""Bài 02 — thêm argparse --turn và kiểm lỗi người dùng."""

import argparse


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Bộ đếm lượt học")
    # TODO: thêm --turn, type=int, required=True.
    return result


def main() -> None:
    """TODO: parse và in ra số lượt; thử input thiếu và không phải số."""
    args = parser().parse_args()
    print("TODO 02: arguments =", args)


if __name__ == "__main__":
    main()
