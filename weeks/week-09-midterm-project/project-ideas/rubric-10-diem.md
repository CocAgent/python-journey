# Rubric chung — Chấm dự án giữa kỳ theo thang 10

Bám sát **10 yêu cầu trong tài liệu giảng viên** *Bài tập nhóm thực hành Python.docx*, áp dụng nhất quán cho dự án nhóm/cá nhân, dù chọn Bot, Student Manager hay đề tài tham khảo. **Mỗi tiêu chí trọng số 1 điểm**, chỉ chọn **0 / 0,5 / 1** dựa trên minh chứng thực tế.

> **Giải thích khác biệt phiên bản:** nguồn Word ưu tiên **Python 3.10+**; riêng Python Journey có baseline **Python 3.12+** theo `AGENTS.md` và `SYLLABUS.md`. Sinh viên theo khóa học này dùng Python 3.12+; đây là quy định của khóa, **không phải câu chữ gốc đã bị đổi**.

| STT | Tiêu chí (1 điểm/mục) | 0 điểm | 0,5 điểm | 1 điểm |
|---:|---|---|---|---|
| 01 | Python là ngôn ngữ chính (tài liệu gốc ưu tiên Python 3.10+) | Không phải Python/chủ yếu ngôn ngữ khác | Có Python nhưng không chủ đạo | Python là chính, phiên bản rõ |
| 02 | Cài đặt và chạy theo hướng dẫn (requirements/pyproject nếu cần) | Không chạy được | Chạy nhưng thiếu bước hoặc phụ thuộc | Chạy ổn theo đúng hướng dẫn |
| 03 | Sản phẩm demo rõ (CLI/UI/Web/API/Report) | Không có demo | Demo mơ hồ hoặc khó thấy kết quả | Demo có kết quả cụ thể, dễ quan sát |
| 04 | Mô tả dữ liệu input/output | Không rõ dữ liệu vào/ra | Thiếu input hoặc output hoặc ví dụ | Input/output rõ ràng và có ví dụ |
| 05 | README tối thiểu (mục tiêu, cách chạy, ví dụ, ảnh nếu có) | Không có README | README sơ sài | README đủ mục cơ bản, dễ làm theo |
| 06 | Cấu trúc gọn, dễ đọc (thư mục, tên, style) | Code lộn xộn | Có cấu trúc nhưng chưa thống nhất | Cấu trúc sạch, dễ đọc, thống nhất |
| 07 | Có kiểm thử/checklist chạy lại | Không có kiểm tra | Chỉ kiểm tra thủ công sơ sài | Có test hoặc checklist rõ, tái hiện được |
| 08 | Có Git/commit rõ, tái hiện đúng phiên bản | Không dùng Git | Có Git nhưng commit rời rạc | Commit có ý nghĩa, có mốc/tag hoặc SHA để chạy lại |
| 09 | Phạm vi vừa sức, MVP trước, chia mốc | Phạm vi quá lớn/không khả thi | Có kế hoạch nhưng chưa rõ | Có MVP và mốc khả thi |
| 10 | Đạo đức & an toàn (nguồn, trích dẫn, dữ liệu nhạy cảm) | Vi phạm hoặc không rõ nguồn | Có rủi ro/thiếu trích dẫn | Nguồn hợp lệ, ghi công, bảo vệ dữ liệu |

**Tổng điểm:** ___ / 10.

## Nguyên tắc công bằng

- Dự án **Python thuần CLI làm đúng, giải thích được** có thể đạt đủ 10 điểm. Không cộng điểm chỉ vì cài framework AI/LLM, dùng GPU, nhiều thành viên, giao diện phức tạp hay dự án “hot”.
- Không lấy kết quả PASS của **mã tham chiếu/giáo trình** để tính bài sinh viên. Ghi lệnh và commit thực tế đã kiểm tra.
- Thư viện/AI chỉ là công cụ: tự viết phần logic phù hợp phạm vi, ghi rõ nguồn và công lao; không tải hoặc đưa dữ liệu nhạy cảm vào dịch vụ không rõ quyền sử dụng.
- Tiêu chí số 7 cho phép **test tự động hoặc checklist có thể chạy lại** đúng như tài liệu nguồn; Tuần 09 chưa bắt buộc `pytest` (học ở Tuần 12).
- Với nhóm 1–3 sinh viên, đánh giá sản phẩm theo rubric trên và có thể trao đổi riêng để xác minh đóng góp của từng người; không tự động chia đều hoặc trừ điểm không có bằng chứng.

## Evidence tối thiểu để chấm minh bạch

1. README ghi mục tiêu, yêu cầu Python/những gói đã dùng, lệnh cài/chạy, ví dụ input/output.
2. Demo có ít nhất một input thường và một input biên hoặc sai; lưu output thực tế.
3. Kế hoạch MVP, mã Python và ít nhất một lỗi được ghi nhận đã sửa.
4. Repo/nhánh/commit SHA hoặc bản nộp định danh được; mô tả nguồn dữ liệu, nguồn mã nếu có.
5. Điền [evidence-template](../evidence-template.md) và (nếu chọn Track C) [phiếu đề xuất nhóm](phieu-de-xuat-nhom.md).

**Lưu ý:** đây là bảng chấm của bài giữa kỳ; trọng số **Midterm Project = 20%** trong tổng điểm khóa được quy định ở `SYLLABUS.md` vẫn giữ nguyên.
