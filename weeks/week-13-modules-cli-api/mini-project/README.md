# Mini-project W13 — Local Bot CLI (từ dữ liệu đến hành động)

## Bài toán

Một Bot demo nhận **vị trí hiện tại** và **đích** trong dải `0..4`.
Bot chọn `left`, `right` hoặc `wait`. Không cần giao diện web hay mạng.

> Đây là project **course-local**, không phải mô hình trạng thái/actions của
> VuaCóc production. `VUACOC_RUNTIME_CONTRACT = UNVERIFIED` và
> `PRODUCTION_INTEGRATION = NO`.

## Luồng xử lý

```text
terminal --position 1 --goal 4
           ↓
bot_course/cli.py         argparse + in JSON / lỗi
           ↓
bot_course/adapter.py     validate 0..4, đóng gói dữ liệu
           ↓
bot_course/core.py        choose_action() → right
```

## Chạy demo và quan sát

Từ **repository root**:

```bash
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
python weeks/week-13-modules-cli-api/cli.py --position 4 --goal 1
python weeks/week-13-modules-cli-api/cli.py --position 2 --goal 2
python weeks/week-13-modules-cli-api/cli.py --position 8 --goal 4
```

Ba dòng đầu có `action = right/left/wait`. Dòng cuối in lỗi ra
`stderr` và có exit code `2`. Xem thêm:

```bash
python weeks/week-13-modules-cli-api/checks/check_week.py
```

## Tự phát triển (chọn ít nhất một)

- **A — CLI:** thêm `--verbose` ở `bot_course/cli.py`, hiển thị lý do
  chọn action mà không thay core.
- **B — Validation:** thêm thông báo dễ hiểu cho state thiếu `goal`
  hoặc ngoài phạm vi; có negative test.
- **C — Input/Output:** thêm `--format text|json`, JSON vẫn mặc định,
  nhưng core không nhận format.
- **D — HTTP offline:** mô phỏng status 404/503 và body lỗi, viết report
  phân biệt HTTP status và JSON parse error; **không gọi mạng**.

## Acceptance checks

- [ ] 3 trường hợp `left/right/wait` đúng.
- [ ] Input không hợp lệ bị từ chối (không stack trace cho người dùng).
- [ ] CLI chỉ lo parsing/output, core không import CLI/HTTP.
- [ ] Đọc được `--help`; hiểu exit code 0/2.
- [ ] Có một case thành công và một case lỗi HTTP giả lập.
- [ ] Viết 3–5 dòng giải thích: thay đổi code ở đâu và vì sao?
- [ ] Ghi 1 bug, cách tái hiện, cách sửa, commit có ý nghĩa.

Không có quota file/class/mô hình AI hoặc yêu cầu production integration.

## Giới hạn phải nêu

Bot không tự học, không dùng LLM, không gọi VuaCóc thật, không truy cập
web. Không suy từ kết quả chạy course-local sang chất lượng production.
