# Các mã nguồn mở tham khảo và hướng nghề nghiệp

Tài liệu so sánh dự án upstream. **Không vendoring/copy source code từ các repo
dưới đây vào capstone này.** Code mẫu là triển khai độc lập dựa trên Python
standard library và tích hợp framework thông qua dependency khi người học chọn.

| Repo | Hướng nghề | Có dùng trong bản mẫu? |
|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Agent, gateway, tools, security boundary | **Ý tưởng core/adapter**, không sử dụng source/SDK/API |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | Backend engineering, HTTP/API, validation | Dependency **tùy chọn** |
| [streamlit/streamlit](https://github.com/streamlit/streamlit) | Data apps, dashboards, UI | Dependency **tùy chọn** |
| [fastapi/typer](https://github.com/fastapi/typer) | CLI developer tools | Đọc thêm; core CLI dùng argparse |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | QA, testing, regression | Dependency **dev/test** |

## Giấy phép tham khảo

Tại thời điểm biên soạn, OpenClaw, FastAPI, Typer và pytest công bố MIT;
Streamlit công bố Apache-2.0. Kiểm tra **LICENSE và THIRD_PARTY_NOTICES**
của đúng commit/version trước khi sao chép code hoặc phân phối bản sửa đổi.
Không suy từ giấy phép của framework sang giấy phép của toàn bộ repo này.

## Vì sao không fork nguyên OpenClaw?

OpenClaw là hệ thống lớn trên nền Node.js/TypeScript với gateway, nhiều
kênh giao tiếp, tools và quyền thực thi. Chương trình Python Journey 15 tuần
chưa dạy thiết kế sandbox, xác thực đa người dùng, quản trị secrets hoặc
bảo mật tool-execution. Không nên cho sinh viên chạy agent có quyền truy
cập file/email/shell thực trên máy chỉ để hoàn thành đồ án.

Nếu quan tâm agent engineering, sau W15 có thể học thêm:
- explicit tool registry/allowlist;
- audit logs;
- human approval cho hành động nhạy cảm;
- API auth, rate limiting, isolation;
- prompt injection/threat modeling;
- local deterministic evaluation.

**Không bao giờ sử dụng `eval` hoặc shell execution với prompt đầu vào
không tin cậy.**
