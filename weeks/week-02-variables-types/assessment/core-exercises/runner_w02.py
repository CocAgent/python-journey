"""Run a trusted Week02 TODO fragment. This is NOT a security sandbox."""

from __future__ import annotations

import io
import json
import runpy
import sys
from contextlib import redirect_stdout
from pathlib import Path

WATCHED = ("ten", "tuoi", "diem_tb", "dang_hoc", "a", "b", "x")


def main() -> int:
    path = Path(sys.argv[1]).resolve()
    source_input = sys.argv[2]
    prior_stdin = sys.stdin
    output = io.StringIO()
    try:
        sys.stdin = io.StringIO(source_input)
        with redirect_stdout(output):
            namespace = runpy.run_path(str(path), run_name="__main__")
        variables = {}
        for name in WATCHED:
            if name in namespace:
                value = namespace[name]
                if type(value) in (str, int, float, bool) and len(str(value)) <= 120:
                    variables[name] = {"type": type(value).__name__, "value": value}
        result = {"ok": True, "stdout": output.getvalue()[:8000], "vars": variables}
    except Exception as error:
        result = {
            "ok": False, "stdout": output.getvalue()[:8000],
            "error": type(error).__name__, "message": str(error)[:180],
        }
    finally:
        sys.stdin = prior_stdin
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
