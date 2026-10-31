"""CLI cho Ticket Desk: giao tiếp người học, không chứa luật nghiệp vụ."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import service, storage


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ticket Desk — offline course project")
    parser.add_argument("--db", type=Path, default=Path("tickets.json"), help="file JSON local")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Tạo ticket")
    add.add_argument("--title", required=True)
    add.add_argument("--priority", choices=("low", "normal", "high"), default="normal")
    commands.add_parser("list", help="Liệt kê ticket")
    close = commands.add_parser("close", help="Đóng ticket")
    close.add_argument("id", type=int)
    commands.add_parser("summary", help="Tổng kết")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    try:
        items = storage.load_tickets(args.db)
        if args.command == "add":
            updated = service.add_ticket(items, args.title, args.priority)
            storage.save_tickets(args.db, updated)
            output: object = updated[-1]
        elif args.command == "close":
            updated = service.close_ticket(items, args.id)
            storage.save_tickets(args.db, updated)
            output = service.find_ticket(updated, args.id)
        elif args.command == "list":
            output = items
        else:
            output = service.summarize(items)
    except (ValueError, OSError) as error:
        print(f"Lỗi: {error}", file=sys.stderr)
        return 2

    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0
