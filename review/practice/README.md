# Bài thực hành tích hợp Week 01–11

Đây là **3 bài ôn tập tự chọn**, không sửa bài tập gốc hoặc rubric.
Chúng được thiết kế theo phương pháp của các tuần đã nâng cấp:
**Dự đoán → Chạy → Giải thích → Sửa lỗi → Viết bài khác → Kiểm chứng**.

## Chuẩn bị

Mở terminal tại **gốc repository `python-journey/`**.
Python >=3.12, không cần cài thư viện ngoài.

Mở `starter/` và tự điền các TODO. Chưa được mở `solutions/`.
Máy kiểm **import và gọi hàm thật**, không chấp nhận in sẵn đáp án
ra terminal để tạo PASS giả.

## Lab 01 — Gradebook: tổng hợp học viên

File `starter/lab01_gradebook.py`, hàm
`summarize_students(records)`.

| Input | Return mong đợi |
|---|---|
| `[{"name":" An ","score":8},{"name":"Bình","score":4},{"name":"Chi","score":9}]` | `{"count":3,"average":7.0,"passed":["An","Chi"]}` |
| `[]` | `{"count":0,"average":None,"passed":[]}` |
| `[{"name":"Mít","score":5}]` | `{"count":1,"average":5.0,"passed":["Mít"]}` |
| Điểm `True`, -1 hoặc 11 | `ValueError` |
| Thiếu `name` hoặc `score`; tên trùng sau `strip().casefold()` | `ValueError` |

Dùng `for`, `if`, `dict.get`, `set`, `.strip()`,
`return` và `sum/len` hoặc cộng biến tích lũy.
Hàm **không được sửa records**. Đừng chia cho 0 khi input rỗng.

## Lab 02 — Lưu báo cáo dưới dạng JSON

File `starter/lab02_json_report.py`:

```python
validate_report(report) -> bool
save_report(path, report) -> Path
load_report(path) -> dict
```

Report gồm **bốn field**:

```python
{
    "format": "PYTHON JOURNEY REVIEW V1",
    "count": 3,
    "average": 7.0,
    "passed": ["An", "Chi"],
}
```

- `count`: int thật, không phải bool, không âm.
- Nếu `count=0`: `average=None` và `passed=[]`.
- Nếu `count>0`: average là số 0..10; danh sách `passed`
  gồm các tên khác rỗng, không trùng, số tên không vượt count.
- JSON **parse được** không có nghĩa **đúng schema**.
- File thiếu: `FileNotFoundError`, JSON hỏng:
  `json.JSONDecodeError`, schema sai: `ValueError`.
- **Kiểm report trước khi ghi**; nếu invalid, không làm hỏng
  bản file hợp lệ đã tồn tại.

Lưu với `pathlib.Path`, `with path.open`,
`encoding="utf-8"`, `json.dump(..., ensure_ascii=False)`.
Máy kiểm tự tạo **thư mục tạm**; không ghi dữ liệu thật.

**Gợi ý nối hai Lab:** lấy dict trả về từ Lab 01, thêm
`"format": "PYTHON JOURNEY REVIEW V1"`, rồi đưa vào Lab 02.
Đây là ý tưởng mở rộng tự chọn, không cần thay signature.

## Lab 03 — Sửa bug logic và dùng exception đúng

File `starter/lab03_debugging.py` có hai hàm:

- `distance(start,end)`: với vị trí nguyên 0..10, trả khoảng
  cách **không âm**. `distance(4,1)` và `distance(1,4)`
  đều là 3. Input sai kiểu, bool hoặc ngoài phạm vi → `ValueError`.
- `parse_score(raw,audit)`: chuyển text thành điểm 0..10,
  trả None cho chữ sai hoặc ngoài phạm vi. Dùng
  `try/except ValueError/else/finally`.
  Audit hợp lệ: `accepted`, `attempt:'8'`;
  input `bad`: `invalid`, `attempt:'bad'`;
  score 11: `out_of_range`, `attempt:'11'`.
  Với `None`, `TypeError` phải tiếp tục nổi lên, nhưng
  `finally` vẫn ghi `attempt:None`.

**Bẫy:** `end-start` cho kết quả âm khi đảo chiều;
`abs(end-start)` mới đúng. Lỗi logic có thể không tạo traceback.

## Chạy máy tự kiểm

```bash
# Ban đầu FAIL (0/3) là đúng: learner starter còn TODO
python review/practice/checks/check_review.py --starter

# Chỉ tham khảo sau khi tự làm, không phải kết quả sinh viên
python review/practice/checks/check_review.py --solutions
```

Sau khi làm đúng cả ba bài:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Review student: PASS (3/3)
```

Nếu FAIL, đọc tên Lab và thông báo; sửa **starter** chứ
không sửa bộ kiểm. Kết quả PASS chỉ xác nhận các case đã
kiểm; hãy thử thêm một input tương tự và giải thích vì sao
code đúng. Ghi lại trong [mẫu evidence](../EVIDENCE-TEMPLATE.md).
