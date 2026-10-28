# Lộ trình phát triển dự án 3 Agent Python

> Đây là kế hoạch **dự kiến**, không phải các tính năng đã hoàn thành.

| Giai đoạn | Mục tiêu | Tiêu chí hoàn thành |
|---|---|---|
| 1 — MVP offline | Planner, Developer, Reviewer mô phỏng | Chạy CLI và bộ kiểm thử |
| 2 — Tăng độ tin cậy | Thêm dữ liệu mẫu, log và edge cases | Pytest cho đầu vào hợp lệ/không hợp lệ |
| 3 — LLM Planner | Tích hợp SDK trong nhánh riêng | Phản hồi kế hoạch thực từ LLM, có kiểm soát lỗi |
| 4 — Developer có tool | Đề xuất patch cho file thử nghiệm | Không tự sửa ngoài thư mục whitelist |
| 5 — Reviewer thực tế | Chạy lint/test, đọc kết quả | Phân biệt test pass và chất lượng nghiệp vụ |
| 6 — Dùng cho game 2D | Thử trên dự án mẫu nhỏ | Có diff, test và phê duyệt thủ công |

## Nguyên tắc
- Không ghi khóa API vào Git.
- Các thao tác ghi, xóa, chạy lệnh cần giới hạn quyền và xác nhận.
- Chỉ đánh dấu hoàn thành khi có commit, bài kiểm thử hoặc minh chứng thực tế.
- Giữ MVP cũ để đối chiếu với bản tích hợp AI.
