"""Child-process evaluator for one case. Used by autograde_de1.py.

Only run your own or trusted student code. Timeout is NOT a sandbox.
"""

from __future__ import annotations

import importlib.util
import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path


def decode(value):
    if isinstance(value, dict) and set(value) == {"__tuple__"}:
        return tuple(decode(item) for item in value["__tuple__"])
    if isinstance(value, list):
        return [decode(item) for item in value]
    if isinstance(value, dict):
        return {key: decode(val) for key, val in value.items()}
    return value


def encode(value):
    if isinstance(value, tuple):
        return {"__tuple__": [encode(item) for item in value]}
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(val) for key, val in value.items()}
    return value


def main() -> int:
    file_path = Path(sys.argv[1]).resolve()
    function_name = sys.argv[2]
    raw_args = json.loads(sys.argv[3])
    args = [decode(item) for item in raw_args]
    response = {}
    output = io.StringIO()
    try:
        spec = importlib.util.spec_from_file_location("student_de1", file_path)
        if spec is None or spec.loader is None:
            raise RuntimeError("Cannot load module")
        module = importlib.util.module_from_spec(spec)
        with redirect_stdout(output):
            spec.loader.exec_module(module)
            function = getattr(module, function_name)
            result = function(*args)
        response = {
            "ok": True,
            "value": result,
            "type": type(result).__name__,
        }
    except Exception as exc:
        response = {"ok": False, "error": type(exc).__name__, "message": str(exc)}
    response["args_after"] = encode(args)
    response["printed"] = output.getvalue()
    try:
        print(json.dumps(response, ensure_ascii=False, allow_nan=False))
    except (TypeError, ValueError) as exc:
        print(json.dumps({"ok": False, "error": "NonJSONReturn", "message": str(exc)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
