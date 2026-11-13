# Week 09 — Sinh viên tự kiểm tra: Dự án giữa kỳ

> Hướng dẫn tự học dùng **mã của chính sinh viên**. PASS của bài mẫu không phải điểm của bạn. Checker chỉ kiểm phần ghi bên dưới; giảng viên vẫn quyết định điểm học phần.

## 1. Chuẩn bị

Mở [README của tuần](../README.md), đọc notes, ví dụ và yêu cầu bài tập. Cài Python >=3.12 và mở Terminal ở thư mục gốc `python-journey`. Trên Windows có thể dùng `py`, trên macOS/Linux thường dùng `python3` thay cho `python`. Tải toàn bộ repository (ZIP hoặc Git), không chỉ một tệp `.py`.

**Phạm vi checker:** Dự án tùy chọn Track A/B/C; không có checker chung.

**Hai hoạt động cần tự quan sát:** Chọn một track và theo rubric 10 điểm hiện có. Demo case thường, case biên, một bug, một giới hạn.

## 2. Tự đánh giá dự án giữa kỳ

Đọc [track](../tracks/README.md), chọn đúng **một track** và bám [rubric 10 điểm hiện hành](../project-ideas/rubric-10-diem.md). Viết code của cá nhân/nhóm; ghi một lệnh chạy lại, normal/edge/invalid case, một lỗi đã sửa, known weakness và phân công công việc.

Checker trong `checks/` của Week 09 chỉ kiểm **reference và danh mục học liệu**, không chấm project của sinh viên. Không dùng PASS của chúng làm bằng chứng dự án.

**Chỉ xem hướng dẫn — không có lệnh tự chấm số chung:**

```bash
python -m assessment guide --week 09
```

Điền [minh chứng giữa kỳ](../evidence-template.md) và chuẩn bị demo bảo vệ. Giảng viên chấm theo rubric, không suy điểm từ CI hoặc checker reference.

## 3. Trước khi nộp

- [ ] Project chạy được từ một command ghi rõ trong README.
- [ ] Có normal/edge/invalid, output thực tế, một bug đã sửa.
- [ ] Có demo, known weakness, commit/nguồn và giải thích thiết kế.
- [ ] Không nộp token, secrets hoặc dữ liệu của người khác.

Xem [mẫu minh chứng chung](../../../assessment/EVIDENCE-TEMPLATE.md) nhưng không thay rubric giữa kỳ.
