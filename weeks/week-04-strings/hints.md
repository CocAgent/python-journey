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
