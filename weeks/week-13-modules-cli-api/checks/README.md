# Week 13 — Reference checks (offline)

Chạy từ **repository root**:

```bash
python weeks/week-13-modules-cli-api/checks/check_week.py
```

Kết quả cần thấy:

```text
Week 13 solution checks: PASS
```

Check này kiểm:
- core `left/right/wait`;
- adapter validate missing/wrong type/out-of-range;
- CLI parse + exit code thành công/lỗi;
- HTTP GET chỉ tạo request metadata, parse 200 và từ chối status/JSON sai;
- chạy **4 lời giải tham khảo** bằng module mode, không gọi network.

Các file `exercises/` là starter có TODO nên **không** được chấm hoàn tất
chỉ vì reference check PASS.

Nếu môi trường có pytest, có thể chạy:

```bash
python -m pytest weeks/week-13-modules-cli-api/tests -q
```

Test sử dụng dữ liệu giả lập; **không gửi HTTP request ra Internet**.

## Bài nâng cao (tùy chọn)

Chạy từ repository root:

```bash
python weeks/week-13-modules-cli-api/checks/check_advanced_ticketdesk.py
python -m pytest weeks/week-13-modules-cli-api/tests -q
```

Checker mới tạo file dữ liệu trong thư mục tạm, không cần network,
API key hay cài FastAPI; test suite gồm cả core Week13 và Ticket Desk.
Xem [hướng dẫn thực hành nâng cao](../advanced_projects/README.md).

## Kiểm thêm bộ bài tương tự

Chạy từ **week root**:

```bash
python -m practice.checks.check_lab --starter
python -m practice.checks.check_lab --solutions
```

`--starter` kiểm code sinh viên đang sửa, trước khi điền TODO sẽ
**FAIL (đúng thiết kế)**. `--solutions` kiểm lời giải tham khảo và
được bảo vệ bởi maintainer CI; không dùng kết quả của solution để thay
bằng chứng tự làm. Đọc [GUIDED-LABS.md](../GUIDED-LABS.md).
