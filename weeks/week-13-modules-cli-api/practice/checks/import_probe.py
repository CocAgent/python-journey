"""Isolated import side-effect probe for Week 13 lab 1."""

from __future__ import annotations

import importlib
import sys


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python -m practice.checks.import_probe module_name")
    importlib.import_module(sys.argv[1])


if __name__ == "__main__":
    main()
