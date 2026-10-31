# Thư viện ý tưởng dự án Python — Week 09

**Chọn một vấn đề vừa sức, xây một chương trình chạy được, kiểm thử và giải thích được.**

Trang này giúp sinh viên tìm một đề tài dựa trên **năng lực đã học ở Week 01–08** và định hướng nghề nghiệp. Đây là **Track C tự chọn** của giữa kỳ, bên cạnh **Track A VuaCóc Bot V1** và **Track B Student Manager**. Sinh viên có thể làm cá nhân hoặc nhóm **1–3 người** và **chỉ cần hoàn thành một track**.

Không phải cài đặt cả framework, xây hệ thống production hoặc hoàn thành mọi ý tưởng trong danh mục.

## Chọn danh mục phù hợp

| Danh mục | Quy mô | Dành cho ai | Ví dụ |
|---|---:|---|---|
| [20 dự án nền tảng](catalog-20-du-an.md) | **20** | Người học Python, Web, Data, QA, AI, Game | FastAPI, pandas, pytest, LangGraph, OpenClaw |
| [Thương mại & Marketing](commerce-marketing-open-source.md) | **13** | Quan tâm bán hàng, CRM, ERP, dashboard, analytics | Saleor, ERPNext, Odoo, PostHog, Umami |
| [AI Agent & Agentic Systems](agent-open-source.md) | **11** | Muốn học agent tools, workflows, retrieval, orchestration | CrewAI, PydanticAI, ADK, smolagents, MCP SDK |

**Quy ước số lượng:** 20 là **danh mục lõi** được kiểm chứng riêng; 13 Commerce/Marketing và 11 Agent là **phụ lục tự chọn**. CrewAI thuộc nhóm Agent (**A01**) và cũng có một mục mô tả trong catalog chính; đây **không phải** đề tài lõi thứ 21. Không tính LangGraph/OpenAI Agents SDK/OpenClaw lặp lại trong phụ lục Agent vì chúng đã nằm trong 20 lõi. Không thay rubric giữa kỳ.

Tất cả link GitHub dẫn đến **nguồn tham khảo**, không phải mã phải fork, cài hoặc nộp lại. Danh mục đã được biên tập từ nguồn giảng viên; [20 nguồn Word ban đầu được lưu chiểu](archive/original-word-sources-20.md).

## Gợi ý theo nghề nghiệp và mức học

| Quan tâm nghề gì? | Hãy bắt đầu bằng MVP Python thuần | Công nghệ tìm hiểu sau |
|---|---|---|
| **Backend / API** | Quản lý ticket, CRUD sách, validate biểu mẫu | FastAPI, Django, Pydantic, SQLAlchemy |
| **E-commerce / Business** | Giỏ hàng, tồn kho, pipeline khách hàng | Saleor, Odoo, ERPNext |
| **Data / Marketing** | Doanh thu, campaign conversion, phễu mua hàng | pandas, Streamlit, PostHog, Umami |
| **QA / Automation** | Chạy checklist test, kiểm dữ liệu đầu vào | pytest, Playwright, Typer |
| **AI / Agent Engineering** | Planner → Validator → Reporter, tool allowlist, retrieval | CrewAI, PydanticAI, smolagents, Haystack, MCP SDK |
| **Game / thuật toán** | Mê cung terminal hoặc Bot chiến lược | pygame-ce, VuaCóc Bot Journey |

**Sinh viên mới học:** ưu tiên quản lý ticket, giỏ hàng, tính báo cáo, validate form, tool registry hoặc truy vấn ghi chú. **Sinh viên khá:** thêm workflow nhiều bước, negative controls, record/replay hoặc phân lớp service/adapter. **Sinh viên quan tâm AI:** không cần LLM/API key ở giữa kỳ; tự viết một chương trình *mô phỏng* điều phối bằng `function`, `list`, `dict`.

## Quy trình thực hiện giữa kỳ — từ chọn đề tài đến nộp bài

1. **Chọn một vấn đề:** đọc một dòng đề xuất MVP; có thể tự đề xuất đề tài khác. Điền [phiếu đề xuất](phieu-de-xuat-nhom.md) với scope và phần việc của từng thành viên.
2. **Chốt chức năng:** định nghĩa 3–5 hành vi nghiệp vụ, input → output, một trường hợp bình thường và một trường hợp lỗi/biên. Không ép một quota hàm không cần thiết.
3. **Viết Python 3.12+ chạy offline:** tận dụng `if`, `for`, `function`, `list/dict/set`; dùng dữ liệu mẫu, không cần framework, Docker, internet, GPU hoặc dịch vụ trả phí.
4. **Chạy và kiểm chứng:** ghi rõ command chạy, expected/actual, ít nhất một bug và cách sửa, một known limitation. `pytest` là nội dung Week 12 nên **không bắt buộc ở Week 09**.
5. **Viết README bài làm:** mục tiêu, chức năng, setup, lệnh chạy, cấu trúc, các case test, giới hạn và nguồn tham khảo.
6. **Commit và chứng minh:** ghi commit SHA, hoàn thiện [mẫu minh chứng](../evidence-template.md), demo được trước người chấm và tự giải thích code.

**Lệnh minh họa** (với bài do sinh viên tự viết, ở thư mục của bài):

```bash
python --version
python main.py
```

Không có lệnh cài/chạy chung cho mọi repository tham khảo. Làm MVP Python thuần trước, không clone nguyên hàng chục repository.

## Điều gì được chấm?

Dùng duy nhất [rubric 10 điểm của giảng viên](rubric-10-diem.md) và [hướng dẫn Track C](../tracks/open-source-inspired.md): đúng yêu cầu, chạy được, cấu trúc hợp lý, test/checklist thực tế, tài liệu, Git và trách nhiệm dữ liệu. **Không cộng điểm chỉ vì chọn AI agent, framework mới, mô hình lớn hoặc công nghệ phức tạp.**

Đây là **midterm Week 09**, không phải capstone Week 15. Khi phát triển tiếp đến cuối khóa, dùng [FINAL_PROJECT.md](../../../FINAL_PROJECT.md) làm nguồn yêu cầu/rubric duy nhất; phần Agent có [lộ trình W09→W15](agent-open-source.md#tiến-hóa-lên-week-15).

## Quy tắc nguồn mở, quyền riêng tư và AI

- **Tham khảo ≠ sao chép:** hãy kiểm LICENSE, NOTICE, dependencies, asset licenses của phiên bản nguồn; ghi công rõ ràng nếu tái sử dụng. Link public không đồng nghĩa mọi việc sao chép đều được phép.
- **Trung thực năng lực:** chương trình `if/for` mô phỏng agent là *rule-based simulator*, không phải LLM/agent tự trị. Không giả mạo kết quả chạy test, nguồn dữ liệu hay hiệu quả mô hình.
- **Không thử trên dữ liệu thật:** không dùng tài khoản cá nhân, email khách hàng, thẻ thanh toán, dữ liệu nhận diện hoặc secret/API key trong project bài học.
- **Không hành động nguy hiểm:** không chạy tool không kiểm soát, shell/code model sinh, automation web không được phép hoặc gửi marketing thật. Nếu cần cài upstream sau giữa kỳ, dùng môi trường tách biệt và kiểm chính sách nguồn.
- **AI hỗ trợ học tập:** có thể dùng công cụ AI theo quy định lớp, nhưng phải giải thích được code, tự kiểm thử và ghi rõ phạm vi hỗ trợ trong minh chứng.

## Tài liệu và biểu mẫu

- [Catalog 20 nguồn lõi](catalog-20-du-an.md) · [Phụ lục 13 Commerce & Marketing](commerce-marketing-open-source.md) · [Phụ lục 11 Agent](agent-open-source.md)
- [Phiếu đề xuất và phân công nhóm](phieu-de-xuat-nhom.md) · [Rubric 10 điểm](rubric-10-diem.md) · [Mẫu minh chứng giữa kỳ](../evidence-template.md)
- [Hướng dẫn Track C](../tracks/open-source-inspired.md) · [Week 09](../README.md) · [Tài liệu Week 15](../../week-15-capstone-project/README.md)

**Mục tiêu cuối cùng:** chọn ít nhưng làm thật — *Learn → Build → Test → Debug → Improve → Commit → Prove*.
