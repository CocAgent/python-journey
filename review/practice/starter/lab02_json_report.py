"""Ôn tập 02 — JSON file persistence (Week 10), không ghi file production."""

import json
from pathlib import Path

FORMAT = "PYTHON JOURNEY REVIEW V1"


def validate_report(report: object) -> bool:
    """Chỉ nhận object có format, count, average, passed đúng schema.

    count: int thật >= 0; count=0 -> average=None, passed=[];
    count>0 -> average: int/float thật trong 0..10;
    passed: list[str] tên không rỗng, không trùng, số tên <= count.
    """
    # TODO: kiểm dict/keys/bool/int/list/str và giá trị.
    raise NotImplementedError("Hãy hoàn thành validate_report")


def save_report(path: Path, report: dict[str, object]) -> Path:
    """Validate trước khi ghi, tạo thư mục cha và dùng UTF-8 + with."""
    # TODO: nếu invalid raise ValueError; dùng json.dump(ensure_ascii=False).
    raise NotImplementedError("Hãy hoàn thành save_report")


def load_report(path: Path) -> dict[str, object]:
    """Đọc JSON và validate; file thiếu/JSON sai giữ exception gốc."""
    # TODO: with path.open('r', encoding='utf-8'), json.load.
    # TODO: sai schema -> ValueError, hợp lệ -> return object.
    raise NotImplementedError("Hãy hoàn thành load_report")


if __name__ == "__main__":
    print("Hãy hoàn thiện TODO; checker sẽ dùng TemporaryDirectory.")
