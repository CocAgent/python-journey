# Gợi ý — Week 10

- Ghép đường dẫn bằng `Path("folder") / "file.txt"`.
- Tạo thư mục cha bằng `path.parent.mkdir(parents=True, exist_ok=True)`.
- Khi ghi CSV, mở file với `newline=""`.
- Key JSON phải là chuỗi; value phải tương thích với JSON.
- Sau khi tải replay, kiểm tra nhãn và schema trước khi tin dữ liệu.

## Gợi ý theo tầng cho 3 bài thực hành bổ sung

Xem [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md),
sau đó [practice/README.md](practice/README.md).

- **Lab 01:** dùng `path.parent.mkdir(parents=True,
  exist_ok=True)`; `with path.open(..., encoding="utf-8")`.
  Viết `"\n".join(lines)` và newline cuối nếu list không rỗng.
- **Lab 02:** validate *trước khi ghi*, dùng
  `csv.DictWriter` + `writeheader()`; khi load,
  `csv.DictReader` trả điểm dạng text nên cần `int()`,
  kiểm range và header.
- **Lab 03:** `json.dump(..., ensure_ascii=False)` và
  `json.load`; **parse hợp lệ chưa đủ**. Kiểm labels,
  turns là list, turn nguyên >=1, action thuộc set hợp lệ.

Chạy `--starter` để kiểm code tự viết; chỉ sau đó mở
`practice/solutions/`. Đừng sửa checker để giả PASS.
