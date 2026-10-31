# Week 11 — Bốn bài Exceptions tự thực hiện có machine check

Xem trước [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md).
Các file `starter/` có **TODO thật**, máy check import và
**gọi hàm** (không so dòng `print` giả). `solutions/`
là lời giải tham khảo để đối chiếu *sau* khi tự làm.

## Lab 01 — Phân biệt lỗi input với bug khác

`safe_int("42")` → `42`, `safe_int("bad")` →
`None`. Dữ liệu sai kiểu như `None` phải gây
`TypeError`, **không** bị broad except nuốt mất.
Dùng đúng `except ValueError`.

## Lab 02 — Đọc điểm từ file

`read_score(path)` xử lý file mất (`None`), số 0..10
(hợp lệ), chữ hoặc ngoài phạm vi (`None`). Viết
hai khối try riêng: **read file** và **parse integer**.
Dùng UTF-8; file trong checker được tạo ở
`TemporaryDirectory`. Truyền nhầm `str` thay vì
`Path` phải khiến lỗi lập trình nổi rõ (`AttributeError`).

## Lab 03 — Raise có thông tin

`validate_action("wait")` → `"wait"`;
`validate_action("teleport")` → `ValueError`
mà message phải chứa `'teleport'`.
Không return action hợp lệ giả từ dữ liệu sai.
Action là dữ liệu **course-local**, không phải contract production.

## Lab 04 — `try/except/else/finally`

`valid_score(raw, audit)`: kiểm 0..10, trả int/None và
ghi vào list audit của caller.

| Input | Return | Hai sự kiện được thêm |
|---|---|---|
| `"8"` | 8 | `converted`, `attempt:'8'` |
| `"bad"` | None | `invalid`, `attempt:'bad'` |
| `"11"` | None | `converted`, `attempt:'11'` |
| `None` | TypeError | chỉ `attempt:None` |

`finally` phải chạy cả khi có TypeError, **không che**
exception đó. Không dùng `return` từ `finally`.

## Chạy từ gốc `python-journey`

```bash
python weeks/week-11-exceptions/practice/checks/check_practice.py --starter
python weeks/week-11-exceptions/practice/checks/check_practice.py --solutions
```

Chưa viết TODO → `Week 11 student practice: FAIL (0/4)`
là đúng; khi hoàn thiện → `PASS (4/4)`. Reference
`PASS (4/4)` **không chứng minh sinh viên làm xong**.

Mỗi lab phải ghi: một input bình thường, một input sai,
exception type hoặc return, nguyên nhân và một regression
được thử lại. Không sửa checker để tạo PASS giả.
