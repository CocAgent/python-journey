"""Ví dụ 06 — Khi nào dùng search, findall, fullmatch?

Mã EV-123 là định dạng GIẢ LẬP (EV- + chính xác ba chữ số ASCII).
Chạy từ repo root:
    python weeks/week-04-strings/examples/06_regex_search_vs_fullmatch.py
"""

import re

pattern = r"EV-[0-9]{3}"

for value in ("EV-123", " EV-123 ", "EV-12", "EV-123X", "XEV-123", "ev-123"):
    candidate = value.strip()
    found_inside = re.search(pattern, candidate) is not None
    exact_match = re.fullmatch(pattern, candidate) is not None
    print(f"{value!r}: search={found_inside}, fullmatch={exact_match}")

# findall chỉ trích chuỗi khớp; đây chưa phải bộ kiểm mã trên văn bản bất kỳ.
message = "Vé EV-123 và EV-456 đã phát hành"
codes = re.findall(pattern, message)
print(f"Mã tìm được: {codes}")

# search không có match trả None; phải kiểm trước khi .group().
missing = re.search(pattern, "Không có mã vé")
print(f"Không tìm thấy: {missing is None}")
