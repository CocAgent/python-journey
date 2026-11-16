# Student challenges — mở rộng dự án tham khảo

Mục tiêu: không chép nguyên mẫu. Chọn một challenge, viết test trước khi sửa,
ghi commit riêng và giải thích design decision. Trọng số chấm và yêu cầu chính
thức vẫn thuộc [FINAL_PROJECT.md](../../../../FINAL_PROJECT.md).

## Level 1 — Python reliability

**C1. Sửa ghi chú (edit-note).** Thêm service + CLI để cập nhật title/body/tags
mà không thay ID/created_at. Test cho ID không tồn tại và title rỗng.

**C2. Filter tag + paging.** Liệt kê ghi chú theo tag; hỗ trợ `--limit` có
validation và test case empty/invalid.

**C3. Import JSON có validate.** Đọc snapshot đã export; kiểm schema version,
invalid shape, duplicated skill và phục hồi an toàn. Không dùng `eval`.

## Level 2 — Portfolio backend/data

**C4. FastAPI CRUD hoàn chỉnh.** Thêm PATCH/DELETE, status 404/422 nhất quán;
viết TestClient tests; bổ sung examples và mô tả security limitation.

**C5. Dashboard dữ liệu.** Biểu đồ kỹ năng theo nhóm, thống kê tiến độ tuần.
Không tạo dữ liệu kết quả giả để báo cáo thành tích.

**C6. SQLite FTS.** Benchmark có kiểm soát trên dataset giả lập và so sánh
với search hiện có; báo rõ latency, size, limitations.

## Level 3 — AI/agent bridge (ngoài phạm vi bắt buộc W15)

**C7. Rule-based learning coach.** Từ skills và notes, đề xuất 3 việc học tiếp
theo bằng rule deterministic, giải thích lý do; test offline.

**C8. Optional LLM adapter.** Nếu chọn, tách API provider, dùng fake provider
trong tests, quản lý secrets an toàn, không gửi dữ liệu riêng tư mặc định,
không trao quyền shell/email/network cho LLM. Không cần công khai API key.

## Evidence bắt buộc khi nhận challenge

- Problem statement + acceptance criteria.
- Test trước/sau và một edge case.
- Command để người khác tái hiện.
- Một commit phản ánh feature, một commit test/fix nếu thích hợp.
- Một đoạn giải thích thay đổi và trade-off.

Các challenge là **gợi ý mở rộng**, không tạo rubric capstone mới.
