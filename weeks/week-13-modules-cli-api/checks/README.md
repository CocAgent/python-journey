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
