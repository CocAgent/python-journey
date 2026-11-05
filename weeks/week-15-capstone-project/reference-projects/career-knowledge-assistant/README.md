# Career Knowledge Assistant — Reference Capstone

**Python Journey W15 · Fully working reference project · Python >=3.12**

> Vấn đề: sinh viên có ghi chú, các kỹ năng và tiến độ học ở nhiều nơi nhưng
> khó tìm lại kiến thức và chứng minh tiến bộ. Ứng dụng này giúp quản lý chúng
> trong một cơ sở dữ liệu SQLite trên chính máy của người học.

Đây là **mã tham khảo hoàn chỉnh**, không phải bài làm để sao chép nộp.
Giảng viên có thể dùng để demo và review code. Sinh viên nên fork rồi
chọn một yêu cầu mới để tự thực hiện, bổ sung test và giải thích được thay đổi.

## Chức năng

1. Tạo, liệt kê và xóa ghi chú kiến thức.
2. Tìm kiếm ghi chú theo tiêu đề, nội dung, tag (không phân biệt hoa/thường).
3. Theo dõi kỹ năng nghề nghiệp theo mức 0–5, cập nhật đánh giá.
4. Dashboard tóm tắt số ghi chú, số kỹ năng, mức trung bình và tag phổ biến.
5. Xuất dữ liệu ra JSON UTF-8 để lưu trữ/chuyển hệ thống.

Mức tối thiểu **không đòi API key, AI model, GPU hay internet** khi chạy.

## Cài đặt — standard path

Mở terminal tại thư mục chứa file README này.

```bash
python --version
python -m venv .venv
```

Kích hoạt Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Sau đó:

```bash
python -m pip install -e ".[dev]"
python -m career_assistant --help
```

Nếu PowerShell chặn Activate.ps1, dùng trực tiếp `.venv\Scripts\python.exe`
để chạy các lệnh, không cần thay đổi chính sách bảo mật hệ thống.

## Chạy — demo đầy đủ

```bash
python -m career_assistant --db demo.db add-note --title "pytest" --body "Test edge case và regression" --tags "python,testing"
python -m career_assistant --db demo.db add-note --title "REST API" --body "HTTP GET, status codes" --tags "backend,python"
python -m career_assistant --db demo.db notes
python -m career_assistant --db demo.db search python
python -m career_assistant --db demo.db skill Python --level 4 --comment "Built projects"
python -m career_assistant --db demo.db skill Git --level 3
python -m career_assistant --db demo.db skills
python -m career_assistant --db demo.db summary
python -m career_assistant --db demo.db export exports/portfolio.json
```

Expected behavior: commands print JSON, SQLite file `demo.db` is created,
export `exports/portfolio.json` contains `notes`, `skills`, `schema_version`.

Để xóa một ghi chú:

```bash
python -m career_assistant --db demo.db delete-note 1
```

## Test

```bash
python -m pytest -q
```

Test suite bao phủ CRUD, search, empty/invalid input, cập nhật kỹ năng,
SQL injection string như dữ liệu thông thường, export JSON và CLI.
Optional API tests tự skip nếu chưa cài extra tương ứng.

Để chạy Week 15 readiness checker từ **repository root**:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py \
  weeks/week-15-capstone-project/reference-projects/career-knowledge-assistant --run-tests
```

Chỉ chạy test/code từ nguồn tin cậy. Checker này không chấm điểm.

## Cấu trúc & thiết kế

```text
career-knowledge-assistant/
├── pyproject.toml
├── README.md
├── AI_USAGE.md
├── OPEN_SOURCE_GUIDE.md
├── PROJECT_CHALLENGES.md
├── career_assistant/
│   ├── __main__.py       # python -m career_assistant
│   ├── cli.py            # argparse adapter
│   ├── service.py        # logic nghiệp vụ, không phụ thuộc framework
│   ├── storage.py        # SQLite transaction + SQL tham số hóa
│   ├── api.py            # optional FastAPI adapter
│   └── dashboard_app.py  # optional Streamlit UI
└── tests/
```

**Design decision:** giữ `service.py` độc lập với FastAPI, Streamlit và CLI.
Đây là cách tiếp cận "core → adapter" lấy cảm hứng từ kiến trúc phân tách
công cụ/transport trong agent systems; **không sử dụng code, API hay SDK của
OpenClaw**. SQLite được chọn vì không cần server, dễ backup và hợp trình độ W15.

Trade-off: text search hiện quét danh sách ghi chú bằng Python, đủ cho dữ liệu
nhỏ; ứng dụng lớn hơn nên dùng SQLite FTS hoặc search index.

## Tùy chọn phát triển nghề Backend — FastAPI

```bash
python -m pip install -e ".[api,api-test]"
python -m uvicorn career_assistant.api:app --host 127.0.0.1 --port 8000
```

Mở `http://127.0.0.1:8000/docs` và thử các endpoint:
`GET /health`, `GET/POST /notes`, `GET /search?q=...`,
`GET/PUT /skills`, `GET /summary`.

Đây là **development API không có authentication**, không public lên
Internet và không sử dụng với dữ liệu nhạy cảm.

## Tùy chọn phát triển Data/AI App — Streamlit

```bash
python -m pip install -e ".[dashboard]"
python -m streamlit run career_assistant/dashboard_app.py
```

UI cũng dùng service/SQLite, không cần viết lại nghiệp vụ.

## Cải tiến & kiểm tra năng lực

Đọc [PROJECT_CHALLENGES.md](PROJECT_CHALLENGES.md) trước khi mở rộng.
Mỗi challenge nên có code, test, commit và evidence. Hướng nghề:
Backend/API, Automation/CLI, Data dashboard, hoặc AI agent foundations.

**Không bắt buộc xây AI agent** để được xem là hoàn thành capstone.
Các nguồn mở và giấy phép tham khảo nằm trong
[OPEN_SOURCE_GUIDE.md](OPEN_SOURCE_GUIDE.md).

## Known limitations

- Một người dùng cục bộ; chưa có đăng nhập, phân quyền hay multi-tenant.
- Chưa hỗ trợ chỉnh sửa ghi chú trực tiếp (đây là challenge cho sinh viên).
- Search phù hợp tập dữ liệu nhỏ, chưa có FTS/index.
- Export JSON là snapshot, **không tự động backup/restore** hay mã hóa.
- Không có LLM, tool execution, web scraping hoặc tương thích OpenClaw.
- API chỉ để chạy localhost; **không an toàn để public** ở cấu hình này.

## AI usage

Xem [AI_USAGE.md](AI_USAGE.md). Sinh viên phải viết báo cáo AI của chính
mình khi làm project và chứng minh đã kiểm chứng output.

## Demo / bảo vệ (5–8 phút)

1. Giải thích vấn đề và scope.
2. Demo add/search/skill/summary/export.
3. Chạy pytest, giải thích một edge case.
4. Trình bày SQL parameterization và cách xử lý invalid level.
5. Cho thấy commit đã thêm một challenge và test regression.

Rubric duy nhất của môn là
[FINAL_PROJECT.md](../../../../FINAL_PROJECT.md).
