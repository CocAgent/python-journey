"""Entry point: python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4.

Python tìm thấy bot_course vì thư mục chứa cli.py tự nằm trên import path.
Không chỉnh sys.path bên trong Bot Core.
"""

from bot_course.cli import main, parse_args

__all__ = ["main", "parse_args"]


if __name__ == "__main__":
    raise SystemExit(main())
