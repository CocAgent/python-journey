# Gợi ý — Week 11

- Đọc dòng cuối traceback trước.
- Chỉ bắt exception cụ thể mà chương trình có thể xử lý có ý nghĩa.
- Đặt success path trong `else`; dành `finally` cho việc luôn phải chạy.
- Validate tại boundary và đưa giá trị sai vào error message.
- Giữ input nhỏ nhất có thể tái hiện defect.
- Thua một match không tự động có nghĩa là software bug.

## Gợi ý theo tầng — 4 lab mới

Đọc [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md) rồi
[practice/README.md](practice/README.md), chỉ xem
`practice/solutions/` sau khi tự làm.

- **Lab 01:** `try: return int(raw)` /
  `except ValueError: return None`. Không bắt `TypeError`.
- **Lab 02:** tách `try path.read_text` với
  `try int(text)`; bắt đúng `FileNotFoundError`
  và `ValueError`, kiểm phạm vi 0..10.
- **Lab 03:** `if type(action) is not str or action not in ACTIONS:`
  rồi `raise ValueError(f"...{action!r}")`.
- **Lab 04:** `try` chỉ chuyển `int(raw)`,
  `except` append `invalid`, `else` append
  `converted`, `finally` append attempt bất kể lỗi.

Đừng dùng `except Exception: pass` hoặc `return`
trong `finally` để làm checker PASS.
