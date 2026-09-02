# W10 — Replay + Data

## Python focus

File I/O, `pathlib`, JSON và CSV.

## Milestone

Lưu diễn biến hoặc kết quả match local để người học có evidence có thể mở lại,
đọc và phân tích. JSON phù hợp dữ liệu có cấu trúc; CSV phù hợp bảng kết quả
đơn giản.

Mọi artifact replay trong milestone phải ghi:

```text
COURSE LOCAL FORMAT
NOT VUACOC PRODUCTION FORMAT
```

## Learning moves

1. Chọn dữ liệu tối thiểu cần lưu để tái hiện một quyết định.
2. Tạo đường dẫn bằng `pathlib`.
3. Ghi và đọc lại dữ liệu bằng context manager.
4. Kiểm tra dữ liệu đọc lại trước khi phân tích.

## Evidence

- Một replay local có thể lưu rồi đọc lại.
- Một CSV tổng hợp kết quả course-local hoặc báo cáo tương đương.
- README giải thích file nào là input và file nào là output.
- Không file nào được tuyên bố tương thích production khi contract chưa verified.
