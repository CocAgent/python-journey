# Mini-project — Replay Inspector

Lưu một replay course-local rồi tải lại để kiểm tra labels và số turn.

## Contract

```text
COURSE LOCAL FORMAT
NOT VUACOC PRODUCTION FORMAT
```

Chạy project implementation:

```bash
python projects/vuacoc-bot-journey/local_arena/examples/replay_roundtrip.py
```

Đây là format học tập offline, không phải schema hay API của production VuaCóc.

## Bước đệm trước Replay Inspector

Sau [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md), làm
[Lab 03 JSON replay](../practice/README.md) để phân biệt
JSON hợp cú pháp với JSON hợp **schema course-local**,
và biết từ chối khi thiếu hai nhãn. Sau đó mới chạy
`replay_roundtrip.py` theo contract dự án.

Không dùng lab này để khẳng định tương thích production.
