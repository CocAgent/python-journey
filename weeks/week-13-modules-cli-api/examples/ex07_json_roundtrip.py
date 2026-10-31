"""Ví dụ 7: ghi và đọc số lượng sách bằng JSON trong thư mục tạm.

Không tạo dữ liệu thật trong repository, không mở mạng.
Chạy: python -m examples.ex07_json_roundtrip
"""

from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory


def load_book(path: Path) -> dict[str, object]:
    """Chỉ đọc một object có title và copies hợp lệ."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("Không thể đọc file JSON hợp lệ") from error
    if not isinstance(data, dict):
        raise ValueError("JSON phải là object")
    title = data.get("title")
    copies = data.get("copies")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("title không được rỗng")
    if isinstance(copies, bool) or not isinstance(copies, int) or copies < 0:
        raise ValueError("copies phải là số nguyên không âm")
    return {"title": title.strip(), "copies": copies}


def main() -> None:
    with TemporaryDirectory(prefix="week13-demo-") as directory:
        file_path = Path(directory) / "book.json"
        sample = {"title": "  Python cơ bản  ", "copies": 3}
        file_path.write_text(json.dumps(sample, ensure_ascii=False), encoding="utf-8")
        print("Bước 1: lưu JSON UTF-8 vào file tạm")
        result = load_book(file_path)
        print(f"Bước 2: đọc và kiểm => {result['title']}: {result['copies']} quyển")

        file_path.write_text('{"title": "Python", "copies": -1}', encoding="utf-8")
        try:
            load_book(file_path)
        except ValueError as error:
            print("Bước 3: từ chối file sai =>", error)
    print("Bước 4: thư mục tạm đã được dọn")


if __name__ == "__main__":
    main()
