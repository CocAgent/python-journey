# Hints — Week 04

## Indexing and methods

- Ký tự cuối dùng index `-1`; đảo chuỗi dùng slice step `-1`.
- Normalize thường bắt đầu bằng `strip()` và `lower()`.
- `split()` tạo pieces; `join()` ghép pieces bằng separator.

## F-strings

- `:.2f` giữ hai chữ số thập phân; `:,` thêm dấu phân cách hàng nghìn.

## Regex mini-lab

- Dùng raw string: `r"PJ-\d{3}"`.
- `search` tìm một match, `findall` lấy nhiều match, `fullmatch` yêu cầu toàn
  bộ text khớp pattern.
- No-match từ `search` là `None`; kiểm tra trước khi gọi `.group()`.

## Ba bài tương tự có máy tự kiểm

Xem [ví dụ có giải thích](WORKED-EXAMPLES.md) và
[practice/README.md](practice/README.md) trước khi tra lời giải.

- **Lab 01 — Keyword:** `keyword = input(...).strip()`. Kiểm
  `if not keyword:` trước `keyword[0]` và `keyword[-1]`;
  dùng `keyword[::-1]` để đảo.
- **Lab 02 — Word counter:** `words = sentence.lower().split()`,
  `normalized = " ".join(words)`, sau đó `words.count("python")`.
  Không đếm `pythonic` thành `python`.
- **Lab 03 — Event code:** `re.fullmatch(r"EV-[0-9]{3}", code)`.
  `re.search` chỉ tìm đoạn, sẽ cho `EV-123X` qua nhầm.

Chạy `python weeks/week-04-strings/practice/checks/check_practice.py
--starter` từ gốc repo. Trước khi hoàn thiện TODO, FAIL là
**đúng thiết kế**, không được sửa máy kiểm để giả PASS.
