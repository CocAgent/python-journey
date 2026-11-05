# Blueprint nâng cao cho các ý tưởng catalog Week 09

Mục đích: giúp bạn thấy **một ý tưởng Python thuần ở Week 09** có thể tiến
lên **modules, CLI, HTTP foundations ở Week 13** mà không phải cài toàn bộ
framework gốc. Danh sách đối chiếu từ [20 nguồn chính](../../week-09-midterm-project/project-ideas/catalog-20-du-an.md);
giữ nguyên mục tiêu sư phạm gốc và không tạo bài bắt buộc mới.

**Quy tắc chung:** Mỗi đề tài chọn một chức năng chính; tách `core.py`
(hàm thuần) với `cli.py` (input/output) và nếu cần `storage.py`
(JSON/CSV). Chạy một normal case và một negative case; ghi evidence và test.
HTTP dùng fixture, **không tự gửi request đến endpoint bên ngoài**.

| Mã | Nguồn tham khảo | Vertical slice nâng cao hợp W13 | Normal / negative case |
|---:|---|---|---|
| 01 | [FastAPI](https://github.com/fastapi/fastapi) | Ticket Desk CLI → HTTP adapter; [code đã có](README.md#track-a--ticket-desk-từ-project-01-fastapi-đến-cli-có-cấu-trúc) | tạo ticket / ID không tồn tại |
| 02 | [Flask](https://github.com/pallets/flask) | Event Scheduler: module sắp xếp sự kiện, CLI list/add | lịch hợp lệ / ngày sai |
| 03 | [Django](https://github.com/django/django) | Book Inventory: kiểm nhập/xuất sách qua service | nhập kho / bán vượt tồn |
| 04 | [Streamlit](https://github.com/streamlit/streamlit) | Student Scores: read JSON/CSV, summary CLI | danh sách có điểm / rỗng |
| 05 | [Gradio](https://github.com/gradio-app/gradio) | FAQ Keyword Helper: module rule + CLI hỏi đáp | câu hỏi khớp / không khớp |
| 06 | [Typer](https://github.com/fastapi/typer) | Task CLI: argparse subcommands trước, đổi adapter tùy chọn | task mới / tên rỗng |
| 07 | [Pydantic](https://github.com/pydantic/pydantic) | Registration Validator: validate dict trước khi render JSON | đủ trường / thiếu/sai kiểu |
| 08 | [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) | Library Loans: list/dict → lưu JSON; không ORM bắt buộc | mượn sách / trả chưa mượn |
| 09 | [pytest](https://github.com/pytest-dev/pytest) | Grade Checker: chia module, test boundary theo W12 | điểm 8 / điểm -1 |
| 10 | [Playwright Python](https://github.com/microsoft/playwright-python) | Form Validator: mô phỏng field/action allowlist | form hợp lệ / field lạ |
| 11 | [Scrapy](https://github.com/scrapy/scrapy) | HTML Extractor: parse fixture HTML có sẵn | tìm tiêu đề / không có tag |
| 12 | [pandas](https://github.com/pandas-dev/pandas) | Sales Report: CSV → sum/group bằng Python trước | số liệu hợp lệ / giá âm |
| 13 | [Polars](https://github.com/pola-rs/polars) | Order Report: list dict → tổng theo cửa hàng | orders chuẩn / quantity 0 |
| 14 | [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Learning Groups: dự đoán rule-based có giải thích | đủ feature / thiếu |
| 15 | [PyTorch](https://github.com/pytorch/pytorch) | Linear Score: module công thức tuyến tính, không train model | input hợp lệ / thời gian âm |
| 16 | [Transformers](https://github.com/huggingface/transformers) | Topic Router: phân loại bằng keyword + evidence | match / empty |
| 17 | [LangGraph](https://github.com/langchain-ai/langgraph) | State Machine: plan → review → report bằng dict | approved / failed state |
| 18 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 3-role Workflow: planner → checker → reporter, không LLM | success / checker rejects |
| 19 | [pygame-ce](https://github.com/pygame-community/pygame-ce) | Maze CLI: board text + move engine | đi hợp lệ / va tường |
| 20 | [OpenClaw](https://github.com/openclaw/openclaw) | Safe Tool Registry: route name → allowlisted function | approved / unknown tool |

## Học thật, không chạy framework cho có

### Track B — Data (04, 12, 13)

1. Mỗi bản ghi có `category`, `amount_vnd` là **số nguyên** và
   `date`; dữ liệu ở `fixtures/orders.json` giả lập.
2. Tạo `parse_orders()` kiểm kiểu và amount không âm; `report()` nhóm
   theo category, hiển thị tổng tiền và count.
3. CLI nhận `--file` và `--category`; một input rỗng → tổng bằng 0.
4. Sau khi test đúng, có thể dựng Streamlit/pandas/Polars trên một adapter
   **tùy chọn**; không thay core chỉ để hiển thị biểu đồ.

### Track C — Agent (17, 18, 20)

1. Input là `task: dict` và danh sách công cụ **giả lập** đã được phép:
   `{"add": add, "mean": mean}`.
2. Planner chỉ chọn công cụ và tạo arguments; checker kiểm tool name,
   kiểu dữ liệu, hạn mức bước; reporter in status.
3. Từ chối tool không có trong registry. Không `eval`, `exec`, shell,
   browser thật, LLM provider hoặc email.
4. Log một run có `status=APPROVED|REJECTED` và lý do. Kiểm fail-closed
   ở negative test, không in “thành công” khi checker thất bại.
5. **Mô phỏng có quy tắc ≠ autonomous AI agent**; code nguồn mở chỉ truyền
   cảm hứng thiết kế, không tuyên bố tương thích runtime.

### Track D — Web/Automation (02, 03, 08, 10, 11)

Lấy một mẫu form hoặc HTML do giáo viên cung cấp sẵn. Viết module parse/
validate, CLI xuất JSON, kiểm input thiếu và trạng thái lỗi. Nếu sau W13
dùng browser automation, chỉ dùng **website local hoặc được phép**,
tôn trọng ToS/robots và không vượt CAPTCHA hay kiểm soát truy cập.

### Track E — ML/Game (05, 14, 15, 16, 19)

Tập trung vào **hành vi quan sát được**: phân loại theo keyword, công thức
tuyến tính hoặc một bước di chuyển trên bản đồ ký tự. Sinh viên
không cần model weights, GPU, training, giao diện đồ họa hay API key.
Khi đã có core+tests, có thể thử UI/ML framework ngoài chương trình.

## Mẫu acceptance criteria dùng cho mọi track

```text
GIVEN input hợp lệ
WHEN chạy command
THEN output đúng định dạng và giá trị

GIVEN input không hợp lệ / tài nguyên không tồn tại
WHEN chạy command
THEN có lỗi rõ + exit code khác 0, không làm bẩn dữ liệu

GIVEN code được import như module
WHEN chạy import
THEN không in/log/run CLI ngoài ý muốn
```

Giữ test của Week 12 và notebook thử nghiệm tách biệt.
Chỉ thêm framework khi có **lợi ích đo được** (API, UI, truy vấn DB,
model inference), không vì tên repo có nhiều sao.

Sau khi hoàn tất, quay về [hướng dẫn Ticket Desk](README.md) hoặc
[Week 15](../../week-15-capstone-project/README.md) để làm capstone
theo rubric duy nhất của `FINAL_PROJECT.md`.
