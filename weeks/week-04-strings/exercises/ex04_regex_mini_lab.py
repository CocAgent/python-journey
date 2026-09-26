"""Exercise 04: a small regular-expression lab."""

import re  # noqa: F401 — learner uses this import to complete the TODOs.

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# TODO 1: use re.findall and r"PJ-\d{3}" to extract both course codes.
# re.findall trả về list tất cả các chuỗi khớp với pattern trong text
codes: list[str] = re.findall(r"PJ-\d{3}", text)

# TODO 2: use re.search to find the first number sequence.
# re.search tìm khớp đầu tiên; .group() lấy chuỗi khớp
match = re.search(r"\d+", text)
first_number = match.group() if match else None

# TODO 3: use re.fullmatch to validate W followed by exactly two digits.
# re.fullmatch yêu cầu TOÀN BỘ chuỗi khớp với pattern (không có ký tự thừa)
candidate = "W04"
is_week_code = re.fullmatch(r"W\d{2}", candidate) is not None

print(codes)        # ['PJ-101', 'PJ-205']
print(first_number) # '101'
print(is_week_code) # True
