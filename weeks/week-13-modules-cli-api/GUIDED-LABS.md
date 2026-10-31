# Week 13 — Sổ tay thực hành từng bước: đọc ví dụ → tự viết → tự kiểm

> **Đối tượng:** sinh viên mới học Python, đã học hàm/list/dict, JSON và lỗi
> chương trình ở các tuần trước. Bài này **không cần Internet/API key** và
> chỉ dùng Python >=3.12.

**Trước khi tự viết TODO:** nếu vẫn chưa hình dung luồng dữ liệu, xem
[**ba ví dụ có giải thích input → từng bước → output → lỗi**](WALKTHROUGH-EXAMPLES.md).
Chạy `python -m examples.ex05_trace_student_flow`, `ex06_http_error_cases`
và `ex07_json_roundtrip` từ week root. Chúng dùng miền bài toán khác
để em chuyển kiến thức sang Study Progress, không phải bài giải starter.

Bạn không cần hiểu tất cả code ngay từ đầu. Mỗi lab gồm:
**nhìn kết quả → đọc từng dòng quan trọng → chạy mẫu → viết bài tương tự →
thử ca lỗi → giải thích bằng lời**.

## 0. Chuẩn bị: biết mình đang ở thư mục nào

Clone repo theo [SETUP.md](../../SETUP.md) hoặc tải repo đã được giảng viên
cung cấp. Mở terminal ở thư mục `python-journey`, kiểm tra Python:

```bash
python --version
cd weeks/week-13-modules-cli-api
python -m examples.ex01_modules
```

Nếu Windows không nhận `python`, thử `py -3` và thay `python` bằng lệnh đó
trong các ví dụ. Không nhập dấu `$`, `>` đầu dòng nếu terminal hiển thị chúng.

Tất cả lệnh `python -m ...` bên dưới chạy từ **thư mục week root**,
tức là nơi có `bot_course/`, `examples/` và `practice/`.

### Cấu trúc cần nhớ

```text
week-13-modules-cli-api/
├── bot_course/           # code mẫu gốc
├── examples/             # demo chạy được: xem trước
├── exercises/            # bài tập 01–04 đang có TODO
├── solutions/            # đáp án tham khảo của bài tập gốc
└── practice/             # BÀI TƯƠNG TỰ: Sổ điểm học tập (bổ sung)
    ├── study_core.py     # hàm xử lý điểm đã cho
    ├── starter/          # em tự viết: 4 lab TODO
    ├── solutions/        # lời giải có thể chạy
    └── checks/           # kiểm bài em và bài tham khảo, tách biệt
```

**Phân biệt:** `starter` được phép còn thiếu, nên **checker sẽ FAIL** trước
khi em làm. Không sửa `solutions/` để làm bài, không copy đáp án trước khi
tự thử. Test CI của repository chỉ bảo vệ **lời giải tham khảo**.

## Lab 1 — Module / import / main guard

### 1A. Quan sát ví dụ có sẵn

```bash
python -m examples.ex01_modules
```

Kết quả gồm dòng `Đi từ 1 đến 4: right` và `Đang ở đích: wait`.

Trong `bot_course/core.py`, hàm `choose_action(position, goal)`
chỉ quyết định hướng đi, không in ra màn hình.
Trong `examples/ex01_modules.py`:

```python
from bot_course.core import choose_action

def main():
    print(choose_action(1, 4))  # right

if __name__ == "__main__":
    main()
```

- `bot_course`: thư mục package.
- `core`: file `core.py` (module).
- `choose_action`: hàm import từ module.
- `main guard`: chỉ chạy `main()` khi gọi ví dụ, không chạy khi
  chương trình khác import nó.

Kiểm tra **import không tự in gì**:

```bash
python -c "import examples.ex01_modules"
```

### 1B. Tự làm bài tương tự — mô tả điểm

Mở `practice/study_core.py`. Mã có sẵn **validate điểm 0–10** và
`status_for_score(score)`, trả `"Đạt"` khi điểm từ 5 trở lên, ngược lại
`"Cần luyện tập"`. Ngưỡng **5 chỉ để học code**, không phải quy chế học phần.

Mở `practice/starter/lab01_module.py`. Tự hoàn thành:

1. Import `status_for_score` bằng `from practice.study_core import ...`.
2. Hàm `describe_score(7.5)` phải trả `"Điểm 7.5: Đạt"`.
3. Hàm `describe_score(3)` phải trả `"Điểm 3: Cần luyện tập"`.
4. Khi chạy file, in mô tả của 7.5; khi import file, không in gì.

Thử:

```bash
python -m practice.starter.lab01_module
python -c "import practice.starter.lab01_module"
```

**Tự giải thích:** vì sao `return` trong `describe_score` khác
`print` trong `main`? Vì sao `import` không nên tự in dòng demo?

### 1C. Thử ca lỗi

`status_for_score(-1)`, `status_for_score(11)`,
`status_for_score(True)` phải từ chối bằng `ValueError`.
**Bài của em không cần sửa `study_core.py`** để biến các ca sai thành hợp lệ.

## Lab 2 — CLI với argparse: đọc option, bắt lỗi, trả exit code

### 2A. Chạy chương trình gốc

```bash
python -m bot_course.cli --help
python -m bot_course.cli --position 1 --goal 4
python -m bot_course.cli --position 99 --goal 4
```

Nhìn file `bot_course/cli.py`. Phân biệt:

- `add_argument("--position", type=int, required=True)`: lấy dữ liệu
  từ command line.
- `parse_args(argv)`: biến text thành kiểu số nguyên.
- `course_local_action(...)`: **kiểm quy tắc nghiệp vụ 0..4**.
- `json.dumps(result, ensure_ascii=False)`: in dữ liệu JSON.
- `return 0`: thành công; `return 2`: dữ liệu sai. Đừng in
  `{"success":true}` nếu kiểm tra thất bại.

### 2B. Tự làm bài tương tự — CLI đọc điểm

Mở `practice/starter/lab02_cli.py`. Yêu cầu:

1. Tạo parser nhận **bắt buộc** `--score`, kiểu `float`.
2. Dùng `status_for_score` để kiểm điểm và phân loại.
3. In JSON có hai trường `score` và `status` nếu hợp lệ.
4. Điểm 12: in lỗi ngắn lên `stderr`, trả code 2,
   **không in JSON giả thành công**.
5. Thiếu `--score` hoặc `--score xyz`: `argparse` trả code 2.

```bash
python -m practice.starter.lab02_cli --help
python -m practice.starter.lab02_cli --score 7.5
python -m practice.starter.lab02_cli --score 12
```

**Expected valid output** (thứ tự key không quan trọng):

```json
{"score": 7.5, "status": "Đạt"}
```

Câu hỏi kiểm tra: `type=float` đã đủ để ngăn điểm 12 chưa?
**Chưa**: argparse chỉ biết đó là một số, core mới biết khoảng hợp lệ.

## Lab 3 — HTTP response + JSON offline (không gửi request)

### 3A. Chạy demo có sẵn

```bash
python -m examples.offline_http
```

Đọc `bot_course/http_foundation.py`.
`build_get_request()` chỉ **tạo đối tượng Request**, không gửi mạng.
`parse_json_response(status, body)` kiểm status 2xx, giải mã UTF-8,
parse JSON và kiểm **object/dict**. Status 503 hay JSON sai phải báo lỗi.

```python
from bot_course.http_foundation import parse_json_response

data = parse_json_response(200, b'{"score": 7.5}')
print(data["score"])  # 7.5
```

### 3B. Tự làm bài tương tự — đọc điểm từ fixture HTTP

Mở `practice/starter/lab03_http.py`. Viết
`read_score_response(status, body)`:

1. Gọi `parse_json_response(status, body)`.
2. Lấy `data["score"]` **có kiểm tra trường thiếu**.
3. Gọi `status_for_score(score)` để phân loại.
4. Trả dict `{"score": 8, "status": "Đạt"}` cho
   `(200, b'{"score": 8}')`.

Phải có **ít nhất 3 ca từ chối**:

| Dữ liệu | Kết quả đúng |
|---|---|
| `(200, b'{"score": 8}')` | dict điểm 8, trạng thái Đạt |
| `(404, b'{"score": 8}')` | `ValueError` do status |
| `(200, b'not-json')` | `ValueError` do JSON |
| `(200, b'{}')` | `ValueError` do thiếu score |
| `(200, b'{"score": 15}')` | `ValueError` do ngoài 0–10 |

Chạy:

```bash
python -m practice.starter.lab03_http
```

**Không gọi `urlopen()`, `requests.get()` hoặc một API online thật**:
bài học này chỉ xử lý phản hồi HTTP *giả lập*.

## Lab 4 — Adapter: giữ nghiệp vụ độc lập giao diện

### 4A. Quan sát ví dụ có sẵn

```bash
python -m examples.ex04_adapter
```

`bot_course/core.py` không chứa CLI. `bot_course/adapter.py` kiểm input
rồi gọi core. Một ngày khác muốn thay CLI bằng web thì core vẫn dùng lại.

### 4B. Tự làm bài tương tự — adapter từ form sang kết quả

Mở `practice/starter/lab04_adapter.py`. Viết
`make_student_report(payload)`:

- Input hợp lệ: `{"student": "  An  ", "score": 7.5}`.
- Output: `{"student": "An", "score": 7.5, "status": "Đạt"}`.
- `student` rỗng, `score` thiếu, `score=True`, điểm 15:
  **phải từ chối** bằng `ValueError`.
- Dùng lại `status_for_score` ở core; **không copy quy tắc phân loại**
  sang adapter.

Chạy:

```bash
python -m practice.starter.lab04_adapter
```

Câu hỏi: nếu mai này input đến từ web form hoặc JSON file, lớp nào
chịu trách nhiệm **kiểm cấu trúc dữ liệu**, lớp nào chịu trách nhiệm
**quy tắc 0–10**?

## 5. Tự kiểm: làm xong thật hay chỉ mới chạy starter?

```bash
# chạy từ week root
python -m practice.checks.check_lab --starter
```

**Trước khi làm TODO: script này FAIL là đúng.** Nó kiểm trực tiếp
`describe_score`, CLI, HTTP và adapter của *starter*.
Sau khi hoàn thiện 4 lab, cần thấy:

```text
Week 13 guided student labs: PASS (4/4)
```

Nếu gặp lỗi, đọc tên `Lab 1/2/3/4`, đối chiếu input và
expected/actual. **Đừng sửa checker để biến FAIL thành PASS.**

Chỉ khi đã tự thử và giải thích được code, mở:
[solutions/](practice/solutions/) và so sánh với code của mình.

```bash
# đáp án tham khảo — PASS sẵn; không chứng minh em đã hoàn thành starter
python -m practice.checks.check_lab --solutions
```

## 6. Bài mở rộng tương tự — chọn một, không sao chép đáp án

| Đề tài | Dữ liệu | Tính năng sinh viên tự triển khai | Ca lỗi cần có |
|---|---|---|---|
| **Thư viện sách** | `{"title":"Python","copies":3}` | CLI tìm, mượn và lưu JSON | mượn quá số lượng |
| **Giỏ hàng** | `{"sku":"P01","price_vnd":12000,"qty":2}` | core tính tiền, CLI nhập giỏ | giá âm, mã hàng lạ |
| **Todo** | `{"task":"Ôn Python","done":false}` | CLI add/list/done | task rỗng, ID lạ |
| **Safe agent simulator** | `{"task":"mean","numbers":[2,4]}` | core chọn tool trong allowlist, adapter tạo report | tên tool không được phép |

Hãy viết một bản `core.py`, một `cli.py` và ít nhất một
`test` hoặc checklist có **expected vs actual**. Nếu chưa học web,
dùng dữ liệu JSON giả lập; không cần dịch vụ bên ngoài.
Các ý tưởng nối với [20 dự án Week 09](../week-09-midterm-project/project-ideas/catalog-20-du-an.md)
và [hướng dẫn nâng cao Ticket Desk](advanced_projects/README.md).

## 7. Sổ ghi bằng chứng để trình bày với giảng viên

Điền vào README bài của em, không sao chép kết quả của đáp án:

```text
Tên Lab / đề tài:
Lệnh chạy từ thư mục nào:
Input thường → Expected → Actual:
Input sai → Expected → Actual:
Một lỗi đã gặp:
Nguyên nhân:
Đã sửa ở hàm / file nào:
Kết quả tự kiểm:
Commit Git:
Một giới hạn chưa xử lý:
AI đã hỗ trợ gì, em tự kiểm lại bằng cách nào:
```

Bộ lab này **không tạo rubric mới** cho giữa kỳ hay capstone.
Dùng [rubric Week 09](../week-09-midterm-project/project-ideas/rubric-10-diem.md)
và [FINAL_PROJECT.md](../../FINAL_PROJECT.md) khi cần.
