"""Lab 03 — re.fullmatch: mã sự kiện giả lập 'EV-' + ba chữ số ASCII.

Nhập "EV-123" -> "Mã hợp lệ: EV-123".
Nhập "EV-12", "EV-123X", "XEV-123" -> "Mã không hợp lệ".
Không phải chuẩn vé sự kiện ngoài đời.
"""

import re

code = input("Mã vé: ").strip()

# TODO 1: dùng re.fullmatch(r"EV-[0-9]{3}", code).
# TODO 2: nếu match -> in "Mã hợp lệ: <code>".
# TODO 3: nếu không -> in "Mã không hợp lệ".
# Không dùng re.search vì search có thể chấp nhận thêm chữ ở hai đầu.
print("TODO Lab 03: chưa hoàn thành")
