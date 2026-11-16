# Week 13 — Đọc code bằng mắt, chạy ví dụ, tự dự đoán rồi biến đổi

**Ba ví dụ giải thích chi tiết, chạy hoàn toàn offline**. Sinh viên chỉ cần
Python >=3.12, không cần tài khoản, API key, `pip install` hoặc Internet.

Tài liệu này là **bước đệm** từ [ví dụ cơ bản 01–04](README.md) sang
[bốn bài tự luyện](GUIDED-LABS.md). Nội dung mới không đổi rubric hoặc
điều kiện hoàn thành tuần.

## Trước khi chạy: đứng đúng thư mục

Mở terminal tại gốc repository `python-journey/`, sau đó:

```bash
cd weeks/week-13-modules-cli-api
python -m examples.ex05_trace_student_flow
python -m examples.ex06_http_error_cases
python -m examples.ex07_json_roundtrip
```

Nếu `ModuleNotFoundError: bot_course`, em thường đang đứng sai
working directory. Hãy kiểm nơi có cả `examples/` và `bot_course/`
rồi chạy lại `python -m ...`. **Đừng sửa `sys.path` trong core để chữa cháy.**

## Cách học mỗi ví dụ (8–12 phút)

1. Đọc đầu vào trong `main()`, **đoán output trên giấy** trước khi chạy.
2. Chạy lệnh, so output thực với dự đoán.
3. Mở file trong `examples/`, chỉ ra từng bước chuyển dữ liệu.
4. Thay **một** giá trị dữ liệu giả; tự thử một ca sai.
5. Quay về file gốc (Git hoặc Undo), không sửa lời giải `practice/solutions/`.
6. Viết 2 câu: “lỗi được phát hiện ở tầng nào?” và “có sửa core không?”.

## Ví dụ 5 — Từ chuỗi JSON thành quyết định Bot

**Mục tiêu:** hiểu ba bước khác nhau: *parse → validate → decide*.

```text
'{"position": 1, "goal": 4}'    chuỗi JSON (text)
                 ↓ json.loads
{"position": 1, "goal": 4}      Python dict
                 ↓ adapter.validate_state
(position=1, goal=4)           dữ liệu hợp lệ 0..4
                 ↓ core.choose_action
"right"                        hành động
                 ↓ main print
Bước 3: action = right         output CLI
```

Chạy `python -m examples.ex05_trace_student_flow`.

**Đầu ra chính cần thấy:**

```text
Bước 3: action = right
Bước 4: thử position=99 (phải từ chối)
Từ chối: position phải từ 0 đến 4
```

Các dòng đầu còn thông báo `Bước 1` và `Bước 2`. Dòng `Từ chối`
là tình huống lỗi **được bắt có chủ đích**, nên chương trình vẫn kết thúc
bình thường. Nếu `position=99`, adapter từ chối **trước khi gọi core**.

### Giải thích code quan trọng

```python
def build_action(raw_state: str) -> dict[str, str]:
    state = json.loads(raw_state)   # JSON text → Python object
    return course_local_action(state)  # adapter validate → core quyết định
```

Đây là ý tưởng rút gọn; file thực có `try/except json.JSONDecodeError`
để đổi lỗi JSON thành `ValueError` dễ đọc. Nếu JSON cho ra `list`
thay vì `dict`, adapter cũng phải từ chối.

**Tự thử:** đổi `position` thành `4` (→ `wait`), đổi `goal`
thành `0` khi position 1 (→ `left`), rồi đổi `position` thành
`true` trong chuỗi JSON (→ `ValueError`, không phải vị trí 1).

**Bài tương tự:** [Lab 4 — adapter báo cáo điểm](GUIDED-LABS.md#lab-4--adapter-giữ-nghiệp-vụ-độc-lập-giao-diện).
Thay `position/goal` bằng `student/score`; đừng chép
`choose_action()` vào bài tính điểm.

## Ví dụ 6 — Status đúng chưa đủ: JSON cũng có thể sai

**Mục tiêu:** phân biệt **lỗi HTTP**, **lỗi định dạng JSON** và
**lỗi quy tắc dữ liệu**. Đây là tình huống mô phỏng response bằng
`status` và `body: bytes`, **không gọi HTTP thật**.

Chạy `python -m examples.ex06_http_error_cases`.

| Input giả | Tầng kiểm | Điều cần quan sát |
|---|---|---|
| `200, b'{"lesson": 13}'` | OK cả ba tầng | `OK: lesson=13` |
| `503, b'{"lesson": 13}'` | HTTP status | `LỖI` dù JSON đúng |
| `200, b"not-json"` | JSON parse | `LỖI` vì body không phải JSON |
| `200, b"{}"` | Schema | `LỖI` vì thiếu lesson |
| `200, b'{"lesson": -1}'` | Business rule | `LỖI` vì lesson không dương |

Ví dụ có hàm:

```python
def read_lesson(status: int, body: bytes) -> int:
    data = parse_json_response(status, body)
    lesson = data.get("lesson")
    if isinstance(lesson, bool) or not isinstance(lesson, int) or lesson < 1:
        raise ValueError("JSON phải có lesson là số nguyên dương")
    return lesson
```

`parse_json_response` đã kiểm status 2xx và body JSON object.
`read_lesson` chỉ bổ sung **quy tắc riêng của bài học**.

**Tự thử:** thay `b'{"lesson": -1}'` bằng `b'{"lesson": true}'`.
Python xem `bool` là một nhánh của `int`, vì thế phải chặn
`bool` riêng. Thử tiếp `b'[]'`: đây là JSON hợp lệ nhưng
**không phải object** mà ví dụ yêu cầu.

**Bài tương tự:** [Lab 3 — đọc điểm từ HTTP fixture](GUIDED-LABS.md#lab-3--http-response--json-offline-không-gửi-request).
Thay `lesson` bằng `score` và áp dụng `validate_score(0..10)`.

## Ví dụ 7 — Ghi JSON vào file tạm, đọc lại và kiểm lỗi

**Mục tiêu:** hiểu `json.dumps` khác `json.loads`,
`str` khác `bytes`, và vì sao file hỏng **không được coi là dữ liệu rỗng**.

```text
{"title": "  Python cơ bản  ", "copies": 3}
             ↓ json.dumps + write_text(UTF-8)
           book.json (file tạm)
             ↓ read_text(UTF-8) + json.loads
{"title": "  Python cơ bản  ", "copies": 3}
             ↓ validate trong load_book()
{"title": "Python cơ bản", "copies": 3}
```

Chạy `python -m examples.ex07_json_roundtrip`. Quan sát:

```text
Bước 1: lưu JSON UTF-8 vào file tạm
Bước 2: đọc và kiểm => Python cơ bản: 3 quyển
Bước 3: từ chối file sai => copies phải là số nguyên không âm
Bước 4: thư mục tạm đã được dọn
```

**Vì sao không dùng `except:` rồi trả `[]`?** Nếu file JSON hỏng,
trả danh sách rỗng sẽ che mất dữ liệu đã có; người dùng tưởng dữ liệu bị
xóa sạch. Cần báo lỗi rõ ràng. `TemporaryDirectory()` tự dọn tài nguyên
demo khi kết thúc.

**Tự thử:** đổi `copies` từ `3` thành `0` (hợp lệ);
sau đó thành `true`, `-1` hoặc `"ba"` (phải từ chối).
Không tạo file với tên thật/khách hàng thật. Đây chỉ là demo một
người dùng; **chưa có khóa file, transaction hay database production**.

**Bài tương tự:** tự viết `load_cart(path)` cho
`{"sku":"P01","qty":2,"price_vnd":12000}`:
`qty` là số nguyên dương, `price_vnd` là số nguyên không âm.
Không dùng `float` cho số tiền VND. Viết một ca sai rồi thử.
Đây là hướng nối tới [catalog Commerce & Marketing](../week-09-midterm-project/project-ideas/commerce-marketing-open-source.md).

## Kết hợp thành mini-project

Sau ba ví dụ trên, em có thể triển khai một *vertical slice* nhỏ:

```text
CLI (argparse) → parse/validate → core logic → JSON output
                                ↓
                      optional file JSON
```

Ví dụ chọn **giỏ hàng mini**:
- `core.py`: tính `qty × price_vnd` sau khi kiểm dữ liệu;
- `cli.py`: đọc `--sku`, `--qty`, `--price-vnd`, in JSON;
- `storage.py` (tự chọn): ghi/đọc file JSON và chặn schema sai;
- `test` hoặc checklist: normal `qty=2`, boundary `qty=1`,
  invalid `qty=0`, `price_vnd=-1`, sai kiểu, thiếu SKU.

**Tiêu chí hoàn thành là hành vi đúng + bằng chứng thật**, không phải số
file/class/functions tối thiểu, không cần FastAPI, Docker hoặc model AI.

## Bảng tra nhanh khi debug

| Triệu chứng | Hỏi trước | Cách xử lý |
|---|---|---|
| `ModuleNotFoundError` | Có đứng tại week root? | `cd weeks/week-13-modules-cli-api`, dùng `python -m` |
| `KeyError: score` | JSON có field `score` không? | Kiểm field trước khi truy cập |
| `JSONDecodeError` | body/file có phải JSON hợp lệ không? | Bắt lỗi parse cụ thể, không báo OK |
| `TypeError` với `True` | bool có lọt qua int? | Chặn `isinstance(value, bool)` |
| CLI trả code 2 | lỗi parse hay lỗi nghiệp vụ? | Xem `stderr`, không in JSON thành công |
| File tạm không thấy | Đã ra khỏi `TemporaryDirectory`? | File demo cố ý tự dọn |

## Tự kiểm và tự đánh giá

Sau khi chạy ba ví dụ, hãy tự trả lời mà không xem lại source:

1. `json.loads` nhận kiểu gì và trả kiểu gì?
2. Tại sao HTTP `200` không đủ để kết luận dữ liệu đúng?
3. `core` hay `adapter` có trách nhiệm kiểm shape của input?
4. Một lỗi đầu vào có nên được chuyển thành “thành công” không?
5. `print` ở đâu và `return` ở đâu để code dễ test?
6. `--starter` khác `--solutions` như thế nào?

**Đáp án gợi ý:** (1) JSON text/bytes → Python object, phải kiểm
kiểu trả về; (2) body có thể sai JSON/schema; (3) adapter kiểm shape,
core kiểm quy tắc nghiệp vụ; (4) không; (5) core trả giá trị, entrypoint
in ra; (6) starter kiểm bài em, solutions chỉ kiểm đáp án tham khảo.

Tiếp tục với [GUIDED-LABS.md](GUIDED-LABS.md), kiểm bài em bằng
`python -m practice.checks.check_lab --starter`, rồi nếu muốn nâng cao
hãy xem [Ticket Desk](advanced_projects/README.md).
