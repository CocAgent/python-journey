# Lời giải tham khảo — Week 13

**Hãy thử exercises trước**, chỉ mở lời giải sau khi đã dự đoán output và
tự sửa ít nhất một lỗi. Các file ở đây hoàn chỉnh và chạy offline.

Từ thư mục week root:

```bash
python -m solutions.ex01_modules
python -m solutions.ex02_cli --turn 3
python -m solutions.ex03_http
python -m solutions.ex04_adapter
```

| File | Ý chính |
|---|---|
| `ex01_modules.py` | import và main guard; không có side effect khi import |
| `ex02_cli.py` | argparse parse, số nguyên và tham số bắt buộc |
| `ex03_http.py` | JSON fixture + xử lý status khác 2xx |
| `ex04_adapter.py` | gọi adapter với state hợp lệ và không hợp lệ |

Kiểm tra solution:

```bash
python checks/check_week.py
```

Tất cả kiểm tra chạy với dữ liệu giả, không gọi network.
