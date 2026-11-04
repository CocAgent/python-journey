"""Run ONE self-study case in an isolated child process (not a security sandbox)."""

from __future__ import annotations

import importlib.util
import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path


FIELDS = ("MaMay", "TenMay", "HangSanXuat", "DungLuongPin", "GiaBan")


def phone_result(phone):
    """Normalize a DienThoai instance to inspectable values."""
    if type(phone).__name__ != "DienThoai":
        raise TypeError("Expected DienThoai object")
    result = {name: getattr(phone, name) for name in FIELDS}
    result["info"] = phone.thongtindienthoai()
    return result


def run(file_path: Path, kind: str, name: str, args: list):
    folder = file_path.parent
    sys.path.insert(0, str(folder))  # Cau5b can import Cau5a in same folder.
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {file_path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[file_path.stem] = module
    spec.loader.exec_module(module)

    if kind == "class":
        obj = getattr(module, name)(*args)
        return phone_result(obj), "class"
    if kind == "factory":
        objects = getattr(module, name)(*args)
        if type(objects) is not list:
            return objects, type(objects).__name__
        # True class instances must originate from the shared Cau5a class.
        import Cau5a  # noqa: PLC0415

        if any(not isinstance(phone, Cau5a.DienThoai) for phone in objects):
            raise TypeError("Expected instances of Cau5a.DienThoai")
        return [phone_result(phone) for phone in objects], "list"
    obj = getattr(module, name)(*args)
    return obj, type(obj).__name__


def main() -> int:
    file_path = Path(sys.argv[1]).resolve()
    kind = sys.argv[2]
    name = sys.argv[3]
    args = json.loads(sys.argv[4])
    output = io.StringIO()
    try:
        with redirect_stdout(output):
            value, typename = run(file_path, kind, name, args)
        result = {"ok": True, "value": value, "type": typename}
    except Exception as error:
        result = {"ok": False, "error": type(error).__name__, "message": str(error)}
    result["printed"] = output.getvalue()
    result["args_after"] = args
    try:
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
    except (TypeError, ValueError):
        print(json.dumps({"ok": False, "error": "NotJSONSerializable"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
