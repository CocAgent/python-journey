# AI Agent & Agentic Systems — 11 nguồn mở để học và định hướng nghề nghiệp

> **Phụ lục tự chọn của Week 09 · Kiểm tra repository: 28/10/2026.** Giữ **20 đề tài lõi** tại [catalog chính](catalog-20-du-an.md) và **13 đề tài Commerce & Marketing** tại [phụ lục ngành](commerce-marketing-open-source.md). Không thay [rubric 10 điểm](rubric-10-diem.md), không yêu cầu cài/copy toàn bộ framework. CrewAI đã có mã **A01** trong catalog chính; tài liệu này ghi cả A01 để dễ tra cứu và bổ sung **A02–A11**.

## Vì sao cần học Agent?

Agent engineering kết hợp kỹ năng Python, mô hình hóa dữ liệu, workflow, kiểm thử, quyền truy cập công cụ, đánh giá hành vi và phân tích lỗi. Ở **W09**, chưa có nền tảng để triển khai một agent tự trị dùng LLM đáng tin cậy. Vì vậy mọi đề tài dưới đây có một **MVP mô phỏng Python thuần, offline và xác định**. Sau W12–W15, người học mới cân nhắc sử dụng framework thực tế, dựa trên mục tiêu và khả năng bảo mật.

**Lưu ý giấy phép:** Ngôn ngữ/giấy phép/hoạt động GitHub được đối chiếu theo metadata tại thời điểm trên. Đây không phải audit bảo mật hay bảo đảm miễn phí cho API/cloud. Trước khi dùng hoặc phân phối mã/tài sản, kiểm LICENSE, NOTICE, các dependency và terms đúng phiên bản. Không suy giấy phép của cả dịch vụ thương mại từ giấy phép repository.

## Chọn nhanh

| Mã | Mã nguồn mở | Hướng nghề / kỹ năng | Mức gợi ý | License repository (GitHub) |
|---|---|---|---|---|
| A01 | [CrewAI](https://github.com/crewAIInc/crewAI) | Điều phối Agent theo vai trò | Nâng cao | MIT |
| A02 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | Đầu ra có cấu trúc, validation | Cơ bản → nâng cao | MIT |
| A03 | [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) | Agent workflow, evaluation | Nâng cao | Apache-2.0 |
| A04 | [Hugging Face smolagents](https://github.com/huggingface/smolagents) | Tool calling an toàn, agent tối giản | Cơ bản → nâng cao | Apache-2.0 |
| A05 | [Agno](https://github.com/agno-agi/agno) | Assistant và tri thức có cấu trúc | Nâng cao | Apache-2.0 |
| A06 | [CAMEL](https://github.com/camel-ai/camel) | Multi-agent collaboration, role-play | Nâng cao | Apache-2.0 |
| A07 | [Haystack](https://github.com/deepset-ai/haystack) | Retrieval / RAG foundations | Cơ bản → nâng cao | Apache-2.0 |
| A08 | [Browser Use](https://github.com/browser-use/browser-use) | Browser agent / workflow QA | Nâng cao | MIT |
| A09 | [Deep Agents](https://github.com/langchain-ai/deepagents) | Planning, task decomposition | Nâng cao | MIT |
| A10 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Tool interoperability / protocol | Cơ bản → nâng cao | MIT |
| A11 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Orchestration + enterprise patterns | Nâng cao | MIT |

**Lựa chọn đơn giản nhất để bắt đầu:** A02 (validation), A04 (allowlisted tools), A07 (retrieval), hoặc A10 (tool registry). **Muốn học nhiều Agent:** A01 (CrewAI) hoặc A06 (CAMEL), nhưng MVP chỉ mô phỏng điều phối vai trò. **Hướng tổ chức/doanh nghiệp:** A03 (Google ADK), A09 (Deep Agents), A11 (Microsoft Agent Framework).

Nguồn tương tự đã thuộc **20 lõi** nên không liệt kê trùng: [LangGraph](https://github.com/langchain-ai/langgraph), [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), [OpenClaw](https://github.com/openclaw/openclaw) (TypeScript). [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) được chọn để học giao thức công cụ, **không coi SDK là một tác nhân AI**.

## Các bài toán mẫu triển khai bằng Python thuần

### A01 · CrewAI — có sẵn tại catalog chính

Xem [đề cương A01 CrewAI](catalog-20-du-an.md#ai-agent-mở-rộng--a01--crewai-ngoài-20-nguồn-cốt-lõi): mô phỏng Planner → Validator → Reporter, bảo đảm không báo thành công khi bước kiểm chứng thất bại.

### A02 · PydanticAI

- **Bài toán MVP W09:** Trợ lý sinh kế hoạch học có schema.
- **Input:** Yêu cầu học, thời lượng, danh sách chủ đề dưới dạng dict.
- **Output:** Kế hoạch gồm mục tiêu, số phút và các bước đã validate.
- **Case biên / từ chối:** Thiếu mục tiêu, thời lượng âm, tổng phút vượt ngân sách.
- **Lộ trình W10–W15:** W12 pytest; W13 Pydantic; sau W15 xem typed agent outputs.
- **An toàn:** Không cần LLM để chạy validator; output quy tắc không gọi là AI.

### A03 · Google Agent Development Kit (ADK)

- **Bài toán MVP W09:** Luồng xử lý yêu cầu nhiều bước.
- **Input:** Phiếu tác vụ có trạng thái new/checked/approved.
- **Output:** Danh sách bước đã hoàn tất và trạng thái cuối.
- **Case biên / từ chối:** Bước thất bại, thiếu trạng thái, không được nhảy thẳng từ new sang approved.
- **Lộ trình W10–W15:** W10 lưu log; W12 test; sau W15 nghiên cứu agent evaluation & ADK.
- **An toàn:** Không dùng thông tin định danh hoặc kết nối cloud thật.

### A04 · Hugging Face smolagents

- **Bài toán MVP W09:** Chọn công cụ tính toán theo allowlist.
- **Input:** Yêu cầu giả lập: cộng điểm / tính trung bình / công cụ lạ.
- **Output:** Tên công cụ hợp lệ, kết quả hoặc lý do từ chối.
- **Case biên / từ chối:** Tên công cụ không nằm trong allowlist; chia cho 0; tham số sai.
- **Lộ trình W10–W15:** W12 kiểm thử tool registry; W13 đóng gói; sau W15 đọc công cụ agent.
- **An toàn:** Không chạy code do model sinh, eval, exec, subprocess hay shell.

### A05 · Agno

- **Bài toán MVP W09:** Trợ lý gợi ý tài liệu học từ bộ thẻ kỹ năng.
- **Input:** Danh sách tài liệu mẫu với tag và mức khó; kỹ năng sinh viên.
- **Output:** Top 3 tài liệu phù hợp và giải thích quy tắc.
- **Case biên / từ chối:** Không có tài liệu, tag không trùng, hồ sơ rỗng.
- **Lộ trình W10–W15:** W10 JSON; W13 API local; sau W15 học về state/knowledge agent.
- **An toàn:** Không giả vờ truy xuất tri thức hay bộ nhớ dài hạn ngoài dữ liệu mẫu.

### A06 · CAMEL

- **Bài toán MVP W09:** Author–Reviewer chỉnh kế hoạch qua vòng phản hồi.
- **Input:** Bản kế hoạch, rubric checklist và giới hạn tối đa 2 vòng.
- **Output:** Kế hoạch cuối cùng, log review và trạng thái APPROVED / NEEDS_WORK.
- **Case biên / từ chối:** Reviewer bác bỏ; tối đa lượt; không vòng lặp vô hạn.
- **Lộ trình W10–W15:** W11 bounded loops; W12 regression test; sau W15 multi-agent experiments.
- **An toàn:** Không gọi mô phỏng role-based là cuộc hội thoại LLM thật.

### A07 · Haystack

- **Bài toán MVP W09:** Tìm đoạn tài liệu liên quan và trích nguồn.
- **Input:** 5–10 đoạn ghi chú giả lập, từ khóa tìm kiếm.
- **Output:** Top đoạn khớp + ID nguồn + số lần xuất hiện.
- **Case biên / từ chối:** Truy vấn rỗng, không có kết quả, đoạn trùng, nguồn thiếu.
- **Lộ trình W10–W15:** W10 đọc văn bản; W12 tests; sau W15 học RAG có grounding.
- **An toàn:** Không tạo câu trả lời bịa hoặc khẳng định embedding khi chỉ tìm từ khóa.

### A08 · Browser Use

- **Bài toán MVP W09:** Mô phỏng plan thao tác biểu mẫu trong trang HTML mẫu.
- **Input:** Danh sách trường form giả lập, mục tiêu điền và gửi (simulation).
- **Output:** Kế hoạch bước và danh sách validation lỗi.
- **Case biên / từ chối:** Field không tồn tại, action ngoài allowlist, không có consent.
- **Lộ trình W10–W15:** W12 test validation; W13 nghiên cứu DOM; sau W15 sandbox browser local.
- **An toàn:** Không tự động thao tác tài khoản, email, mua hàng hay website bên ngoài.

### A09 · Deep Agents

- **Bài toán MVP W09:** Chia công việc lớn thành checklist có phụ thuộc.
- **Input:** Yêu cầu dự án, các bước và phụ thuộc dạng dict.
- **Output:** Thứ tự bước hợp lệ, cảnh báo phụ thuộc vòng/trống.
- **Case biên / từ chối:** Chu trình phụ thuộc, bước thiếu, nhiệm vụ rỗng.
- **Lộ trình W10–W15:** W10 lưu JSON; W12 tests; W15 thiết kế task planner nhỏ.
- **An toàn:** Không cấp quyền file write, shell, network hoặc browser cho planner.

### A10 · MCP Python SDK

- **Bài toán MVP W09:** Registry công cụ giả lập với validate input.
- **Input:** Lệnh gọi tool với name/arguments như từ điển.
- **Output:** Kết quả tool đã duyệt hoặc lỗi có mã rõ.
- **Case biên / từ chối:** Tool không tồn tại, tham số thiếu/sai kiểu, từ chối quyền.
- **Lộ trình W10–W15:** W13 module/CLI; sau W15 học MCP server/client & authorization.
- **An toàn:** SDK là giao thức kết nối công cụ, không tự nó là AI agent.

### A11 · Microsoft Agent Framework

- **Bài toán MVP W09:** Bộ chuyển trạng thái và phân công công việc theo quy tắc.
- **Input:** Danh sách tác vụ mẫu, nhân sự/role giả lập và trạng thái.
- **Output:** Danh sách nhiệm vụ được phân, kết quả hợp lệ và audit trail.
- **Case biên / từ chối:** Role chưa được phép, task trùng ID, người xử lý lỗi.
- **Lộ trình W10–W15:** W10 log; W12 tests; W15 project workflow, sau W15 đọc orchestration framework.
- **An toàn:** Đây là hệ sinh thái Python/.NET; không đòi cài dịch vụ doanh nghiệp.


## Khung MVP chung (chỉ dùng kiến thức W01–W08)

**Một đề tài, 3–5 hành vi chính, một command chạy được.** Không thêm framework/LLM chỉ để tăng độ phức tạp:

```text
request (dict/list/str)
    ↓
validate_input()
    ↓
plan_or_select()       # quy tắc rõ ràng; không tuyên bố LLM
    ↓
execute_allowed_step() # giả lập, không network/shell
    ↓
validate_result()
    ↓
report + audit_log
```

Đề xuất cấu trúc thư mục bài của sinh viên:

```text
my-agent-simulator/
├── README.md
├── main.py              # python main.py
├── cases.py             # 1 case hợp lệ, 1 case lỗi
└── AI_USAGE.md          # nếu đã dùng AI hỗ trợ
```

Kiểm thử tối thiểu tại W09: normal case, invalid/boundary case và một lần từ chối có lý do; ghi **expected vs actual**, một bug đã sửa và known limitation. Đề tài không dùng AI vẫn đạt điểm tối đa khi đủ rubric. **Không yêu cầu pytest ở W09** (nội dung W12).

## Tiến hóa lên Week 15

| Giai đoạn | Công việc phù hợp | Minh chứng |
|---|---|---|
| W09 | mô phỏng luồng agent bằng Python thuần | chạy offline, output rõ, từ chối hợp lệ |
| W10 | log ra JSON/CSV | file đọc lại được, không lộ secret |
| W11 | lỗi có mã, invalid state, giới hạn số bước | không loop vô hạn, không che exception |
| W12 | pytest normal, boundary, fail-closed | regression tests, đánh giá theo behavior |
| W13 | module + CLI, mock tool adapter | setup và tests không cần API key |
| W14 | composition chiến lược / role | đổi role/strategy không phá core |
| W15 | capstone có README, test và demo/defense | theo **duy nhất** [FINAL_PROJECT.md](../../../FINAL_PROJECT.md) |

## An toàn & tính trung thực trong học thuật

- **Mô phỏng ≠ hệ AI tự trị:** không gắn nhãn “LLM”, “RAG embeddings”, “multi-agent thực tế” nếu chỉ là rule-based.
- **Tool call:** dùng allowlist rõ; không `eval`, `exec`, code sinh tự động, shell, subprocess, đọc file cá nhân hay thực thi hành động bên ngoài.
- **Quyền và dữ liệu:** test bằng dữ liệu giả; không gửi email, duyệt web tài khoản thật, tự động thanh toán, nhập token/secret hoặc đưa dữ liệu cá nhân lên cloud.
- **Chi phí:** framework có thể mở nhưng model APIs, hosting và managed service có thể tính phí; không yêu cầu sinh viên trả tiền.
- **Đánh giá:** kiểm input/output, giới hạn vòng lặp, thất bại an toàn, bằng chứng kiểm thử; không cộng điểm vì framework nổi tiếng.
- **AI_USAGE:** nếu dùng ChatGPT/Codex/agent để viết bài, sinh viên phải giải thích đoạn code, chạy được test và công khai phạm vi dùng AI theo quy định lớp.

## Nguồn không ưu tiên làm bài W09

Không yêu cầu cài nguyên **OpenClaw**, **OpenHands**, **n8n** hay **Dify** chỉ để hoàn thành Python foundations. Một số hệ thống khác ngôn ngữ, phức tạp hoặc có điều kiện license/hosted service riêng; có thể tham khảo sau W15 với sự hướng dẫn. Việc không có tên trong phụ lục không có nghĩa là nguồn đó kém chất lượng.

Quay về [README hướng chọn đề tài](README.md) · [Phiếu đề xuất](phieu-de-xuat-nhom.md) · [Rubric 10 điểm](rubric-10-diem.md).
