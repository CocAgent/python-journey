# Hướng dẫn nâng cao Week 13 — Từ 20 ý tưởng mã nguồn mở đến dự án chạy được

**Tùy chọn, sau phần cơ bản của Week 13.** Hãy hoàn thành [Week 13 README](../README.md)
và [mini-project Bot CLI](../mini-project/README.md) trước khi học tiếp.

Nguồn ý tưởng: [20 dự án tuyển chọn ở Week 09](../../week-09-midterm-project/project-ideas/catalog-20-du-an.md).
Đây là **đường nâng cấp từ sản phẩm Python cơ bản**, không yêu cầu clone toàn bộ
FastAPI, Django, LangGraph hay OpenClaw. Không có rubric, điểm cộng hoặc deadline mới.

## Bạn sẽ học thêm gì?

Một dự án Week 09 thường là một file Python với `list/dict/function`. Sau W10
(JSON), W11 (exceptions), W12 (pytest) và W13 (packages/CLI/HTTP), bạn có thể:

- phân tách **logic nghiệp vụ → lưu trữ → CLI/HTTP** để dễ thay đổi;
- kiểm lỗi dữ liệu từ file, terminal, phản hồi HTTP;
- giữ code nghiệp vụ test được mà không cần mạng;
- có đầu ra tái hiện được bằng command và bằng chứng kiểm thử;
- thử một framework *tùy chọn* sau khi đường Python thuần đã PASS.

### Chọn lộ trình theo hướng nghề

| Track | Tham chiếu catalog | Dự án tự xây dựng ở W13 | Điểm mở rộng sau W13 |
|---|---|---|---|
| **A. Backend/CLI** | 01 FastAPI · 06 Typer · 07 Pydantic · 09 pytest | **Ticket Desk**: quản lý ticket có CLI, JSON, HTTP giả | API thật chạy localhost (tùy chọn) |
| **B. Data/Analytics** | 04 Streamlit · 12 pandas · 13 Polars | Báo cáo campaign/đơn hàng từ fixture | Dashboard và DataFrame |
| **C. Agent/Workflow** | 17 LangGraph · 18 OpenAI Agents SDK · 20 OpenClaw | Planner → Checker → Reporter, không LLM | Graph / tool interface có kiểm soát |
| **D. Web/Automation** | 02 Flask · 03 Django · 08 SQLAlchemy · 10 Playwright · 11 Scrapy | Ticket/biểu mẫu/HTML sample xử lý offline | local web, DB, authorized browser QA |
| **E. ML/Giao diện/Game** | 05 Gradio · 14 scikit-learn · 15 PyTorch · 16 Transformers · 19 pygame-ce | Phân loại rule-based hoặc trò chơi terminal | thư viện/GUI khi đã vững nền tảng |

**Các số 01–20 là mã nguồn tham khảo trong catalog**, không phải 20 bài tập phải nộp.
Sinh viên chỉ cần chọn *một* track. Track A có mẫu chạy được ngay; B–E có
[blueprint từng bước](TRACK-BLUEPRINTS.md) để tự phát triển.

## Track A — Ticket Desk: từ project 01 FastAPI đến CLI có cấu trúc

**Problem:** Một nhóm muốn lưu ticket yêu cầu hỗ trợ. Mỗi ticket có
`id`, `title`, `priority` (`low|normal|high`), `status`
(`open|closed`). Dữ liệu demo không có thông tin khách hàng thật.

```text
CLI ──→ storage.load/save(JSON) ──→ service (add/find/close/summary)
          │                              ↑
          └──── optional HTTP adapter ───┘
```

**Cấu trúc mã đã có:**

```text
advanced_projects/
├── README.md                       # hướng dẫn này
├── TRACK-BLUEPRINTS.md             # hướng dẫn cho 19 mã khác
└── ticketdesk/
    ├── __main__.py                 # python -m advanced_projects.ticketdesk
    ├── cli.py                      # argparse, exit code
    ├── service.py                  # rules, input validation
    ├── storage.py                  # local JSON; không có database server
    ├── http_demo.py                # 200/404 dạng bytes, không network
    └── fastapi_optional.py         # FastAPI local-only, cài riêng nếu muốn
```

### Bước 1 — chạy thử, không cài dependency bên ngoài

Từ **repository root**, đi vào thư mục Week 13:

```bash
cd weeks/week-13-modules-cli-api
python -m advanced_projects.ticketdesk --help
python -m advanced_projects.ticketdesk --db demo-tickets.json add --title "Sửa chức năng đăng nhập" --priority high
python -m advanced_projects.ticketdesk --db demo-tickets.json add --title "Kiểm tra báo cáo" --priority normal
python -m advanced_projects.ticketdesk --db demo-tickets.json list
python -m advanced_projects.ticketdesk --db demo-tickets.json summary
python -m advanced_projects.ticketdesk --db demo-tickets.json close 1
python -m advanced_projects.ticketdesk --db demo-tickets.json summary
```

**Kết quả mong đợi:** hai ticket `id=1,2`, trước khi đóng là
`{"total":2,"open":2,"closed":0}`, sau khi đóng `id=1` là
`{"total":2,"open":1,"closed":1}` (CLI in JSON dạng nhiều dòng).
File `demo-tickets.json` được tạo trong working directory; chỉ dùng dữ
liệu giả. Sau khi thực hành, tự xóa file này nếu không cần.

### Bước 2 — dự đoán hai lỗi trước khi chạy

```bash
python -m advanced_projects.ticketdesk --db demo-tickets.json add --title " "
python -m advanced_projects.ticketdesk --db demo-tickets.json close 999
python -m advanced_projects.ticketdesk --db demo-tickets.json close 1
```

Cả ba trả **exit code 2** và không ghi thay đổi thành công. Em hãy
trả lời: vì sao `argparse` chưa đủ để kiểm chuỗi rỗng và ticket đã đóng?
Xem `service.py` để phân biệt parse với business validation.

### Bước 3 — hiểu HTTP theo cách offline

```bash
python -m advanced_projects.ticketdesk.http_demo
```

Quan sát `HTTP giả lập 200` (đã tìm thấy) và `404` (không tìm thấy).
`make_get_response()` xây status và JSON bytes, **không mở HTTP server,
không gọi network, không tương đương `FastAPI` hoặc `REST API` thật**.

### Bước 4 — chạy bài test

Quay về **repository root**:

```bash
cd ../..
python -m pytest weeks/week-13-modules-cli-api/tests -q
python weeks/week-13-modules-cli-api/checks/check_advanced_ticketdesk.py
```

Script kiểm tra advanced chỉ dùng standard library, tạo file trong
`tempfile.TemporaryDirectory()`. Pytest của Week 13 kiểm cả reference
cơ bản và nâng cao; các bài learner TODO vẫn tách biệt.

### Bước 5 — thử FastAPI thật (chỉ sau khi bản offline PASS)

Tạo venv riêng theo [SETUP.md](../../../SETUP.md). **Tùy chọn và cần cài dependency**, không thuộc gate mặc định:

```bash
python -m pip install fastapi uvicorn
cd weeks/week-13-modules-cli-api
python -m uvicorn advanced_projects.ticketdesk.fastapi_optional:app --host 127.0.0.1 --port 8000
```

Mở `http://127.0.0.1:8000/docs` bằng browser và thử `GET /health`,
`GET /tickets`, `POST /tickets`, `POST /tickets/{id}/close`.
Đây là API development demo, **không có đăng nhập/authorization,
không được expose ra Internet**. `httpx` chỉ cần nếu muốn viết
`FastAPI TestClient` test nâng cao. API bản thật này không thuộc
CI mặc định và phải kiểm riêng trước khi demo.

### Bước 6 — chủ động nâng cấp, không chép mẫu

Chọn một: thêm `--priority` filter cho `list`, thêm
`reopen-ticket` với business rule, hoặc thêm `GET /tickets/{id}` ở
API localhost. Trước khi làm, viết acceptance criteria, sau đó
test normal/invalid case, ghi commit và giải thích một trade-off.

**Bộ test hiện tại là kiểm mã tham khảo**, không chứng minh bạn đã làm xong
tính năng mới nếu chưa viết test riêng.

## Kiểm tra trước khi nộp bằng chứng

- [ ] Chạy được một luồng end-to-end và một lỗi nhập sai.
- [ ] Hiểu được vì sao `service` không import `argparse`/FastAPI.
- [ ] Phân biệt **response mô phỏng** với web server thật.
- [ ] Test dữ liệu rỗng, ID không tồn tại, trạng thái không hợp lệ.
- [ ] README bài làm ghi command, expected/actual, bug đã sửa, limitations.
- [ ] Git commit thể hiện thay đổi tự viết; không sao chép code nguyên repo upstream.
- [ ] Khi hướng sang Week 15, tuân thủ [FINAL_PROJECT.md](../../../FINAL_PROJECT.md) làm rubric duy nhất.

## Những giới hạn có chủ đích

File JSON chỉ cho **một người chạy tại một thời điểm**, không có locking,
atomic replace, đăng nhập, phân quyền hoặc xử lý transaction thương mại.
Không lưu PII; không dùng để triển khai production. Track Agent không có
LLM hay tool execution thật. Các framework tham khảo có thể đổi API;
hãy kiểm docs/version/LICENSE trước khi học triển khai thật.

**Đường học:** *Python core → modules → CLI → test → offline HTTP → optional API → capstone*.
