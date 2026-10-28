# Ghi chú học tập: AI Agent và Workflow

## Phân biệt
- **Workflow cố định**: các hàm thực thi theo trình tự được lập trình sẵn. Đây là trạng thái hiện tại của dự án.
- **LLM Agent**: mô hình nhận nhiệm vụ, suy luận/chọn công cụ theo cấu hình và trả kết quả. Cần giám sát, giới hạn quyền và kiểm tra đầu ra.
- **Multi-agent**: nhiều vai trò phối hợp; không tự động bảo đảm chất lượng hoặc độ chính xác.

## Từ vựng
- **Orchestration**: điều phối công việc giữa các thành phần.
- **Tool calling**: mô hình đề nghị gọi một công cụ qua giao diện được cho phép.
- **Handoff**: chuyển giao nhiệm vụ hoặc quyền điều phối giữa các agent.
- **Guardrails**: các kiểm tra và giới hạn trước/sau khi xử lý.
- **Human approval**: yêu cầu người dùng duyệt trước thao tác có tác động.

## Đề xuất thứ tự học
1. Nắm cách `run_pipeline` truyền dữ liệu giữa 3 hàm.
2. Viết thêm kiểm thử input lỗi và báo cáo thiếu bước.
3. Thử SDK trong nhánh mới, dùng biến môi trường cho khóa API.
4. Thêm tool đọc tệp trong thư mục demo; chưa cấp quyền ghi.
5. Chỉ bật sửa file qua bản vá và bước phê duyệt.

Tham khảo đường dẫn chính thức trong [RESOURCES.md](../RESOURCES.md).
