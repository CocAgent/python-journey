# Danh mục 20 dự án mã nguồn mở được tuyển chọn — Week 09 (2026)

> **Lịch sử nguồn:** Bản đầu dựa trên tài liệu giảng viên *Bài tập nhóm thực hành Python.docx*, mục “Tổng hợp 20 dự án mã nguồn mở tiềm năng (Python – AI – Agent – Edge – Robotics – Game)”. **Bản này là danh mục được biên tập lại**, không còn là bản sao nguyên danh sách Word. Ý tưởng MVP, tiêu chí tuyển chọn và các nguồn bổ sung là nội dung của Python Journey.
>
> **Đối chiếu metadata:** 28/10/2026, dựa trên GitHub repository public/không archived, hoạt động mã nguồn, ngôn ngữ chính và thông tin giấy phép hiển thị. Đây **không phải** audit độc lập về bảo mật, chất lượng từng bản release hay tính tương thích Python 3.12. Muốn sử dụng source thực tế, phải kiểm tra LICENSE, dependency và phiên bản tại thời điểm cài đặt.

Xem [bản lưu chiểu 20 tên/URL gốc](archive/original-word-sources-20.md) để đối chiếu nguồn giảng viên; file lưu chiểu không phải danh sách khuyến nghị.

**Chỉ chọn 1 MVP bằng Python 3.12+** cho Track C. Không phải clone/cài cả 20 repo, không yêu cầu API key, GPU, web server, robot, tài khoản dịch vụ hoặc truy cập Internet để hoàn thành giữa kỳ. Các ví dụ Python thuần dùng `if/for/list/dict/function` của Week 01–08; tên framework chỉ là **nguồn tham khảo/hướng phát triển nghề**, không phải tiêu chí cộng điểm.

## Mở rộng theo ngành: Thương mại & Marketing

Bên cạnh **20 nguồn cốt lõi**, sinh viên quan tâm ngành kinh doanh có thể chọn
[**13 nguồn mở Commerce & Marketing**](commerce-marketing-open-source.md)
gồm Saleor, Django Oscar, ERPNext, Odoo, Pretix, Medusa, Wagtail,
PostHog, Umami, Mautic, listmonk, Matomo và GrowthBook.

**Đây là phụ lục tự chọn, không phải thêm 13 bài phải làm hay đổi số lượng
nguồn cốt lõi mà checker Week 09 đang kiểm.** Có bài toán MVP Python offline
cho giỏ hàng, tồn kho, CRM, phân khúc khách hàng, chiến dịch và phân tích chuyển đổi.

## Mở rộng AI Agent & Agentic Systems

Ngoài CrewAI **A01** ở phần dưới, đã bổ sung thêm **10 nguồn mở Agent**
vào [**phụ lục A01–A11**](agent-open-source.md): PydanticAI, Google ADK,
smolagents, Agno, CAMEL, Haystack, Browser Use, Deep Agents, MCP Python SDK
và Microsoft Agent Framework. Phụ lục có bài toán Python thuần chạy offline,
đầu vào/đầu ra/edge case, lộ trình Week 10–15 và lưu ý bảo mật.

**Nguồn mở chỉ để tham khảo:** không cần cài các framework hay dùng LLM/API key
trong bài giữa kỳ. Chỉ 20 dự án cốt lõi được tính trong bảng chính; A01–A11
là nhóm tự chọn, không làm thay đổi rubric 10 điểm.

## Nguyên tắc tuyển chọn

- **Tính hữu ích nghề nghiệp:** Backend, QA/automation, data, AI/agent, game; có lộ trình mở rộng W10–W15.
- **Khả năng học:** ý tưởng có thể thu nhỏ thành input → xử lý → output ngoại tuyến, người học hiểu và giải thích được từng hàm.
- **Tín hiệu bảo trì:** repository gốc tồn tại, không archived và có lịch sử cập nhật; sao GitHub chỉ là tham khảo, không thay review code.
- **Giấy phép và an toàn:** không chép mã/dữ liệu nếu chưa kiểm LICENSE và điều kiện sử dụng. Không chạy code bên thứ ba không tin cậy trong máy thật; không nhập secret hay thông tin cá nhân.
- **Cân bằng:** giữ đúng **20 lựa chọn cốt lõi**, có **A01–A11 Agent tự chọn** và **13 nguồn Commerce/Marketing**; hệ thống lớn không được ưu tiên chỉ vì nổi tiếng.

**Nhãn mức:** B = có thể học framework sau khi hoàn thành MVP; C = định hướng nghề nghiệp nâng cao, **không yêu cầu cài/huấn luyện tại W09**. Nhãn không quyết định điểm. Dùng chung [rubric 10 điểm](rubric-10-diem.md) và [phiếu đề xuất nhóm](phieu-de-xuat-nhom.md).

## Danh sách 20 nguồn được chọn

| STT | Repository nguồn mở | Hướng nghề | Mức | Ý tưởng MVP tự xây dựng ở Week 09 |
|---:|---|---|:---:|---|
| 01 | [FastAPI](https://github.com/fastapi/fastapi) | Backend / REST API | B | Sổ yêu cầu hỗ trợ: thêm, tìm, đóng ticket theo trạng thái |
| 02 | [Flask](https://github.com/pallets/flask) | Web backend nhỏ | B | Quản lý lịch sự kiện bằng các hàm Python và CLI |
| 03 | [Django](https://github.com/django/django) | Business web / ORM | C | Quản lý kho sách: nhập, bán, tra cứu tồn kho |
| 04 | [Streamlit](https://github.com/streamlit/streamlit) | Data dashboard | B | Thống kê tiến bộ học tập của một nhóm nhỏ |
| 05 | [Gradio](https://github.com/gradio-app/gradio) | Giao diện demo AI | B | Bộ tư vấn câu hỏi học tập theo từ khóa, không dùng LLM |
| 06 | [Typer](https://github.com/fastapi/typer) | CLI automation | B | Công cụ danh sách việc làm với lệnh add/list/done |
| 07 | [Pydantic](https://github.com/pydantic/pydantic) | Data validation | B | Kiểm tra phiếu đăng ký có trường bắt buộc và khoảng hợp lệ |
| 08 | [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) | Database / backend | B | Theo dõi sách mượn-trả bằng list/dict |
| 09 | [pytest](https://github.com/pytest-dev/pytest) | QA / software reliability | B | Bộ kiểm chứng hàm xếp loại kết quả học tập |
| 10 | [Playwright Python](https://github.com/microsoft/playwright-python) | QA / web automation | C | Bộ kiểm tra quy tắc biểu mẫu giả lập, không mở trình duyệt |
| 11 | [Scrapy](https://github.com/scrapy/scrapy) | Data collection | C | Trích tiêu đề từ các đoạn HTML mẫu được cung cấp sẵn |
| 12 | [pandas](https://github.com/pandas-dev/pandas) | Data analytics | B | Báo cáo doanh thu theo danh mục |
| 13 | [Polars](https://github.com/pola-rs/polars) | Data analytics hiệu năng | B | Tổng hợp đơn hàng theo cửa hàng |
| 14 | [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Machine learning cổ điển | C | Gợi ý phân nhóm bài học bằng rule-based features |
| 15 | [PyTorch](https://github.com/pytorch/pytorch) | Deep learning | C | Tính điểm dự đoán bằng công thức tuyến tính minh bạch |
| 16 | [Hugging Face Transformers](https://github.com/huggingface/transformers) | NLP / model tooling | C | Phân loại câu hỏi theo chủ đề bằng bộ từ khóa |
| 17 | [LangGraph](https://github.com/langchain-ai/langgraph) | Agent workflow / state graph | C | Bộ điều phối các bước tư vấn học tập bằng hàm thuần |
| 18 | [OpenAI Agents SDK (Python)](https://github.com/openai/openai-agents-python) | Agent / tool orchestration | C | Luồng planner → checker → reporter bằng ba hàm Python |
| 19 | [pygame-ce](https://github.com/pygame-community/pygame-ce) | Game Python / event loop | B | Game tìm đường trong mê cung ký tự ở terminal |
| 20 | [OpenClaw](https://github.com/openclaw/openclaw) | Agent systems (TypeScript) | C | Bộ định tuyến công cụ an toàn: chọn tác vụ bằng quy tắc |

## Hướng dẫn nâng cao sau Week 09

Muốn nâng MVP Python thuần thành ứng dụng có **module, CLI, JSON, kiểm thử
và HTTP foundation**, xem [**hướng dẫn nâng cao Week 13**](../../week-13-modules-cli-api/advanced_projects/README.md).
Có mã mẫu **Ticket Desk** lấy cảm hứng từ **01 FastAPI**, kết hợp bài học
**06 Typer** (CLI) và **09 pytest**; ngoài ra có
[blueprint cho đủ 20 lựa chọn](../../week-13-modules-cli-api/advanced_projects/TRACK-BLUEPRINTS.md).
Việc học framework thực tế là tùy chọn, không cộng điểm mặc định và
không làm thay đổi bài giữa kỳ.

## AI Agent mở rộng — A01 · CrewAI (ngoài 20 nguồn cốt lõi)

CrewAI từng thuộc **20 nguồn tham khảo trong tài liệu Word gốc** (xem
[lưu chiểu](archive/original-word-sources-20.md)). Nay đưa trở lại dưới mã
**A01** vì phù hợp định hướng công việc AI Agent sau khi đã có Python cơ bản.
Đây là **đề tài bổ sung tùy chọn**, không thay thế hay tăng 20 đề tài cốt lõi,
không thay rubric.

| Mã | Repository nguồn mở | Hướng nghề | Mức | Ý tưởng MVP tự xây dựng ở Week 09 |
|---|---|---|:---:|---|
| A01 | [CrewAI](https://github.com/crewAIInc/crewAI) | Python multi-agent workflows · role/task orchestration | C | Mô phỏng đội tác vụ Planner → Validator → Reporter bằng hàm Python, chạy offline |

### A01 · CrewAI

- **MVP W09 (Python thuần):** Xây `plan_task(task)`,
  `validate_plan(plan)`, `report_result(plan, verdict)` và
  `run_team(task)`, truyền dữ liệu giữa các vai trò bằng `dict`/ `list`.
  Mô phỏng luồng *vai trò → nhiệm vụ → kết quả* bằng quy tắc xác định,
  không chạy CrewAI thật và **không gọi đây là nhóm AI tự trị**.
- **Input → output và trường hợp biên:** Nhận yêu cầu học tập giả lập
  (`"on_tap_python"`, `"kiem_tra_git"`), xuất bản kế hoạch, kết quả
  kiểm tra và nhật ký mỗi bước. Kiểm thử yêu cầu rỗng/không hỗ trợ,
  kế hoạch thiếu trường, validator từ chối và bảo đảm Reporter không
  báo thành công khi Validator thất bại.
- **Định hướng sau giữa kỳ:** W10 lưu nhật ký JSON; W11 xử lý lỗi
  rõ ràng; W12 thêm pytest; W13 chia module và tạo CLI; W15 tùy chọn
  nghiên cứu [CrewAI Crews và Flows](https://github.com/crewAIInc/crewAI)
  trong môi trường tách biệt, sử dụng dữ liệu giả, fake provider nếu
  cần test. Việc cài framework, LLM/API key hoặc trả phí **không bắt buộc**.
- **Giải thích kỹ thuật:** CrewAI là framework **Python**, cung cấp
  khái niệm agents theo vai trò (Crews) và workflows (Flows); nội dung
  W09 chỉ học ý tưởng decomposition/handoff, không phải sử dụng API
  tương thích với CrewAI.
- **An toàn và minh bạch:** Không trao shell/network/email/đọc tệp cá
  nhân cho tác nhân, không nhúng secret hoặc đưa dữ liệu người dùng
  vào model; khi thực sự tích hợp LLM ở môn nâng cao cần giới hạn
  tool permissions, ghi audit log, xác nhận người dùng và kiểm soát
  chi phí. Báo kết quả mô phỏng là *rule-based*, không gọi là inference.
- **Nguồn và bản quyền:** [Repository CrewAI](https://github.com/crewAIInc/crewAI)
  công bố MIT tại thời điểm đối chiếu 28/10/2026; kiểm LICENSE đúng
  phiên bản trước khi sao chép/distribute source.

## Đề cương MVP: đầu vào, đầu ra, edge case và mở rộng

### 01 · FastAPI

- **MVP W09 (Python thuần):** Sổ yêu cầu hỗ trợ: thêm, tìm, đóng ticket theo trạng thái.
- **Input → output và trường hợp biên:** List dict ticket → danh sách lọc, số ticket mở; thử ticket ID không tồn tại.
- **Định hướng sau giữa kỳ:** W13: API GET/POST + validation; W15: tests, deployment localhost.

### 02 · Flask

- **MVP W09 (Python thuần):** Quản lý lịch sự kiện bằng các hàm Python và CLI.
- **Input → output và trường hợp biên:** Danh sách sự kiện → lịch sắp xếp; thử ngày sai và danh sách rỗng.
- **Định hướng sau giữa kỳ:** W13+: web routes/form, test client, không deploy công khai khi chưa có auth.

### 03 · Django

- **MVP W09 (Python thuần):** Quản lý kho sách: nhập, bán, tra cứu tồn kho.
- **Input → output và trường hợp biên:** Bản ghi sách dạng dict → tồn kho; thử bán quá tồn.
- **Định hướng sau giữa kỳ:** W15+: học ORM/admin/migration trên dữ liệu giả.

### 04 · Streamlit

- **MVP W09 (Python thuần):** Thống kê tiến bộ học tập của một nhóm nhỏ.
- **Input → output và trường hợp biên:** Điểm mẫu → trung bình và số đạt; thử dữ liệu rỗng.
- **Định hướng sau giữa kỳ:** W13+: dashboard bảng/biểu đồ bằng Streamlit.

### 05 · Gradio

- **MVP W09 (Python thuần):** Bộ tư vấn câu hỏi học tập theo từ khóa, không dùng LLM.
- **Input → output và trường hợp biên:** Câu hỏi → nhãn + giải thích; thử câu không khớp.
- **Định hướng sau giữa kỳ:** W13+: đưa hàm hiện có vào UI Gradio.

### 06 · Typer

- **MVP W09 (Python thuần):** Công cụ danh sách việc làm với lệnh add/list/done.
- **Input → output và trường hợp biên:** Tên việc + trạng thái → báo cáo; thử tên rỗng.
- **Định hướng sau giữa kỳ:** W13+: đổi argparse/CLI sang Typer; help + validation.

### 07 · Pydantic

- **MVP W09 (Python thuần):** Kiểm tra phiếu đăng ký có trường bắt buộc và khoảng hợp lệ.
- **Input → output và trường hợp biên:** Dict biểu mẫu → danh sách lỗi; thử thiếu trường/sai tuổi.
- **Định hướng sau giữa kỳ:** W13+: chuyển rule validation sang Pydantic models.

### 08 · SQLAlchemy

- **MVP W09 (Python thuần):** Theo dõi sách mượn-trả bằng list/dict.
- **Input → output và trường hợp biên:** Người mượn, mã sách → trạng thái mượn; thử trả sách chưa mượn.
- **Định hướng sau giữa kỳ:** W10+: SQLite; W15+: SQLAlchemy sessions/transactions.

### 09 · pytest

- **MVP W09 (Python thuần):** Bộ kiểm chứng hàm xếp loại kết quả học tập.
- **Input → output và trường hợp biên:** Danh sách input/expected → báo cáo pass/fail thủ công; thử 0/10 và ngoài khoảng.
- **Định hướng sau giữa kỳ:** W12: viết pytest cases, regression test; không bắt buộc pytest ở W09.

### 10 · Playwright Python

- **MVP W09 (Python thuần):** Bộ kiểm tra quy tắc biểu mẫu giả lập, không mở trình duyệt.
- **Input → output và trường hợp biên:** Danh sách thao tác test → pass/fail; thử trường rỗng.
- **Định hướng sau giữa kỳ:** Sau W13: test UI trang local được phép; không automation đăng nhập trái phép.

### 11 · Scrapy

- **MVP W09 (Python thuần):** Trích tiêu đề từ các đoạn HTML mẫu được cung cấp sẵn.
- **Input → output và trường hợp biên:** Chuỗi HTML giả lập → danh sách tiêu đề; thử cấu trúc thiếu.
- **Định hướng sau giữa kỳ:** Sau W13: spider trên website có quyền thu thập; tôn trọng robots/ToS.

### 12 · pandas

- **MVP W09 (Python thuần):** Báo cáo doanh thu theo danh mục.
- **Input → output và trường hợp biên:** List dict giao dịch → tổng và nhóm; thử danh sách rỗng, giá âm.
- **Định hướng sau giữa kỳ:** W10+: CSV/pandas DataFrame; kiểm tra schema dữ liệu.

### 13 · Polars

- **MVP W09 (Python thuần):** Tổng hợp đơn hàng theo cửa hàng.
- **Input → output và trường hợp biên:** List dict đơn hàng → doanh số; thử số lượng 0.
- **Định hướng sau giữa kỳ:** W13+: so sánh DataFrame pandas/Polars sau khi hiểu cơ sở.

### 14 · scikit-learn

- **MVP W09 (Python thuần):** Gợi ý phân nhóm bài học bằng rule-based features.
- **Input → output và trường hợp biên:** Điểm và thời gian học → gợi ý có giải thích; thử dữ liệu thiếu.
- **Định hướng sau giữa kỳ:** Sau W15: mô hình ML với train/test split và baseline.

### 15 · PyTorch

- **MVP W09 (Python thuần):** Tính điểm dự đoán bằng công thức tuyến tính minh bạch.
- **Input → output và trường hợp biên:** Giờ học + số bài → điểm dự đoán; thử input âm.
- **Định hướng sau giữa kỳ:** Sau W15: tensor, autograd; không cần GPU/huấn luyện ở W09.

### 16 · Hugging Face Transformers

- **MVP W09 (Python thuần):** Phân loại câu hỏi theo chủ đề bằng bộ từ khóa.
- **Input → output và trường hợp biên:** Danh sách câu → nhãn và số lượng; thử câu rỗng.
- **Định hướng sau giữa kỳ:** Sau W15: inference có mẫu và license phù hợp; không tải model lớn mặc định.

### 17 · LangGraph

- **MVP W09 (Python thuần):** Bộ điều phối các bước tư vấn học tập bằng hàm thuần.
- **Input → output và trường hợp biên:** State dict → bước tiếp theo; thử state thiếu/điểm biên.
- **Định hướng sau giữa kỳ:** Sau W15: state graph và checkpoint; không cấp quyền tool nguy hiểm.

### 18 · OpenAI Agents SDK (Python)

- **MVP W09 (Python thuần):** Luồng planner → checker → reporter bằng ba hàm Python.
- **Input → output và trường hợp biên:** Nhiệm vụ mẫu → kế hoạch, kiểm tra, báo cáo; thử bước lỗi.
- **Định hướng sau giữa kỳ:** Sau W15: agent tools, approval, fake provider; không cần API key ở W09.

### 19 · pygame-ce

- **MVP W09 (Python thuần):** Game tìm đường trong mê cung ký tự ở terminal.
- **Input → output và trường hợp biên:** Bản đồ + lệnh → vị trí và thắng/thua; thử va tường.
- **Định hướng sau giữa kỳ:** Sau W09: UI 2D, event loop, sprite; không bắt buộc đồ họa.

### 20 · OpenClaw

- **MVP W09 (Python thuần):** Bộ định tuyến công cụ an toàn: chọn tác vụ bằng quy tắc.
- **Input → output và trường hợp biên:** Yêu cầu → tên hàm được phép + lý do; thử tác vụ không được phép.
- **Định hướng sau giữa kỳ:** Sau W15: nghiên cứu gateway/approval/log; không fork/cài toàn bộ, không shell tools.

## Những nguồn không còn ưu tiên trong danh mục Week 09

**Không kết luận những repo dưới đây kém chất lượng.** Chúng có thể rất mạnh trong lĩnh vực riêng, nhưng bản trước gây hiểu lầm rằng sinh viên nhập môn cần chọn từ các hệ thống quá lớn, thiên về C++/robotics/embedded, hoặc trùng ý tưởng MVP. Vì thế thay bằng các nguồn Python sát nghề nghiệp hơn:

| Nguồn cũ | Lý do rời danh mục ưu tiên W09 | Nếu quan tâm vẫn có thể học |
|---|---|---|
| Apache Airflow, Prefect | Hai orchestration engines quá nặng cho chương trình dùng hàm cơ bản; ý tưởng pipeline bị trùng | Data engineering sau W13 |
| DVC | Data versioning/MLOps cần workflow và Git/data lineage trước | MLOps sau W15 |
| JupyterLab | IDE/notebook hữu ích nhưng không phải dự án giải quyết vấn đề độc lập; trùng ý tưởng thống kê | Công cụ hỗ trợ học data |
| CrewAI | Không nằm trong **20 lựa chọn lõi** vì framework đa agent nâng cao; nay có **A01** là mô phỏng offline cho sinh viên muốn tìm hiểu | Dùng CrewAI thật sau W15 khi có nền tảng bảo mật và kiểm thử |
| ONNX Runtime, OpenVINO, llama.cpp | Runtime inference thiên về C++/phần cứng/tối ưu; MVP W09 không thực sự thực hành công cụ gốc | Inference/edge sau W15 |
| TensorFlow Lite Micro | Embedded/TinyML cần kiến thức phần cứng/C++ | IoT/Edge nâng cao |
| ROS 2, PyBullet, Panda3D | Robot/physics/3D nặng, khó setup, không cần cho việc học Python nền tảng | Robotics/3D nâng cao |
| pygame/pygame | Giữ hướng game nhưng ưu tiên [pygame-ce](https://github.com/pygame-community/pygame-ce) có hoạt động cập nhật gần hơn tại ngày rà soát | Học game Python tương tự |

Tổng cộng: **13 nguồn cũ rời danh mục**, thay bằng **13 lựa chọn mới hoặc thay thế**, giữ 7 nguồn gốc phù hợp nhất. Đây là quyết định *scope/pedagogy*, không phải bảng xếp hạng chất lượng upstream.

## Quy trình nộp đề tài (1–3 sinh viên hoặc cá nhân)

1. Chọn **một đề tài** trong danh sách hoặc tự đề xuất vấn đề khác; làm [phiếu đề xuất](phieu-de-xuat-nhom.md).
2. Ghi 3–5 chức năng MVP, dữ liệu mẫu, **một input bình thường và một input biên/không hợp lệ**, expected/actual.
3. Code **Python thuần** với hàm, danh sách/từ điển; chạy một lệnh offline. Các framework từ bảng là **tùy chọn sau khi MVP PASS**.
4. Chụp/log kết quả thật, ghi một lỗi đã sửa, một known limitation, README, Git commit SHA và [evidence](../evidence-template.md).
5. Ghi công nguồn, xác minh license nếu thật sự dùng mã/tài nguyên, không tự động gửi dữ liệu tới bên thứ ba.
6. Đối với scraping/browser automation, chỉ truy cập dữ liệu/test site **được phép**, tôn trọng ToS/robots và không vượt CAPTCHA hoặc cơ chế bảo vệ.
7. **Không yêu cầu pytest ở W09** (dạy ở W12), HTTP/API ở W13, LLM hoặc agent server. Nhánh AI có thể dùng rule deterministic; **không gọi chatbot quy tắc là LLM**.

**Rubric và quyền đề xuất đề tài khác không thay đổi.** Đây chỉ là catalog tham khảo, không phải syllabus thứ hai, thư viện bắt buộc hay bằng chứng sản phẩm đã PASS.
