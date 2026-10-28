"""Beginner-friendly command-line interface for the reference capstone."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from career_assistant import service


def _print(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="career-assistant",
        description="Knowledge notes and career skills — local SQLite only",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=Path(os.environ.get("CAREER_ASSISTANT_DB", "career.db")),
        help="SQLite file (default: career.db)",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add-note", help="Add a knowledge note")
    add.add_argument("--title", required=True)
    add.add_argument("--body", required=True)
    add.add_argument("--tags", default="")
    commands.add_parser("notes", help="List all notes")
    search = commands.add_parser("search", help="Search notes")
    search.add_argument("query")
    delete = commands.add_parser("delete-note", help="Delete a note")
    delete.add_argument("id", type=int)
    skill = commands.add_parser("skill", help="Set skill level from 0 to 5")
    skill.add_argument("name")
    skill.add_argument("--level", type=int, required=True)
    skill.add_argument("--comment", default="")
    commands.add_parser("skills", help="List skills")
    commands.add_parser("summary", help="Show learning dashboard")
    export = commands.add_parser("export", help="Export notes and skills to JSON")
    export.add_argument("output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    try:
        if args.command == "add-note":
            _print({"id": service.add_note(args.db, args.title, args.body, args.tags)})
        elif args.command == "notes":
            _print(service.list_notes(args.db))
        elif args.command == "search":
            _print(service.search_notes(args.db, args.query))
        elif args.command == "delete-note":
            _print({"deleted": service.delete_note(args.db, args.id)})
        elif args.command == "skill":
            service.set_skill(args.db, args.name, args.level, args.comment)
            _print({"updated": args.name})
        elif args.command == "skills":
            _print(service.list_skills(args.db))
        elif args.command == "summary":
            _print(service.summary(args.db))
        elif args.command == "export":
            _print({"output": str(service.export_json(args.db, args.output))})
        return 0
    except (ValueError, OSError) as error:
        print(f"Lỗi: {error}", file=sys.stderr)
        return 2
