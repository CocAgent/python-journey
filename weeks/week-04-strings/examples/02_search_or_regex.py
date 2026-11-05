"""Compare a direct string check with regex pattern search."""

import re

filename = "lesson.py"
print(filename.endswith(".py"))

text = "Các mã là PJ-102, PJ-305 và mã lỗi A-1."
codes = re.findall(r"PJ-\d{3}", text)
print(codes)

first_code = re.search(r"PJ-\d{3}", text)
print(first_code.group() if first_code else "no match")
