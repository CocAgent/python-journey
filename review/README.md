# Ôn tập Python Journey

Thư mục `review/` cung cấp tài liệu **ôn tập tự chọn** và đề thực hành có thể tự kiểm. Nội dung gắn với các tuần trong Python Journey và không thay thế `SYLLABUS.md`, `FINAL_PROJECT.md`, bài tập chính thức hoặc thang điểm đánh giá của khóa học.

## Chọn lộ trình ôn tập

| Lộ trình | Phù hợp với | Bắt đầu |
|---|---|---|
| **Ôn kiến thức Week 01–11** | Sinh viên muốn củng cố trước khi học kiểm thử `pytest` ở Week 12 | [Kế hoạch 4 buổi](STUDY-PLAN.md) |
| **Đề luyện cơ bản 60 phút** | Sinh viên cần tự kiểm biến, điều kiện, vòng lặp và cấu trúc dữ liệu cơ bản | [Đề luyện 60 phút](mock-exams/de-01/README.md) |
| **Đề tổng hợp 90 phút** | Sinh viên muốn ôn số, chuỗi, list, dictionary và lập trình hướng đối tượng | [Đề tổng hợp 90 phút](mock-exams/de-90-phut-01/README.md) |

**Lưu ý về kiến thức tiên quyết:** đề 90 phút có câu lập trình hướng đối tượng với lớp `DienThoai`. Trong lộ trình Python Journey, nội dung OOP được học kỹ hơn ở Week 14. Sinh viên chưa học phần này có thể làm Câu 1–4 trước, học ví dụ OOP có hướng dẫn rồi hoàn thành Câu 5. Không dùng đề 90 phút như điều kiện hoàn thành bắt buộc của Week 11.

## Bộ ôn kiến thức theo tuần

- [16 câu hỏi dự đoán kết quả](QUICK-CHECK.md) và [đáp án giải thích](ANSWER-KEY.md).
- [Ba bài thực hành tích hợp](practice/README.md): quản lý điểm, lưu JSON và xử lý lỗi.
- [Mẫu ghi bằng chứng học tập](EVIDENCE-TEMPLATE.md): dự đoán, kết quả, lỗi đã sửa và kiểm tra lại.
- [Hướng dẫn sử dụng trên máy từ xa](REMOTE-DESKTOP-SETUP.md) nếu người học truy cập máy qua Chrome Remote Desktop.

## Cách sử dụng

**Tải mã Python thực hành từ GitHub** (không chạy trực tiếp file từ Google Docs). Mở terminal tại thư mục gốc `python-journey`.

```bash
# Ôn 3 bài thực hành tích hợp
python review/practice/checks/check_review.py --starter

# Kiểm riêng lời giải tham khảo của 3 bài tích hợp (không chấm mã sinh viên)
python review/practice/checks/check_review.py --solutions

# Tự chấm đề tổng hợp 90 phút
python review/mock-exams/de-90-phut-01/autograde_de1.py --student

# Kiểm đáp án tham khảo (không chấm mã sinh viên)
python review/mock-exams/de-90-phut-01/autograde_de1.py --reference
```

Khi file khởi đầu còn `TODO`, kết quả FAIL hoặc 0 điểm là **đúng thiết kế**. Sinh viên cần viết mã, chạy lại, giải thích lỗi và bổ sung trường hợp kiểm tra mới. Chỉ mở thư mục lời giải sau khi tự thực hiện.

## Nguyên tắc chung

Bộ kiểm thử tự luyện có mục tiêu **phản hồi và hỗ trợ học tập**, không phải hệ thống chấm thi chính thức. Bộ đề công khai cả tình huống kiểm thử và lời giải để sinh viên nghiên cứu. Không sửa mã tự chấm nhằm tạo kết quả PASS giả.

Thực thi mã do bản thân viết hoặc từ nguồn đáng tin cậy. Timeout không đủ để cách ly mã của người khác. **Không nộp mật khẩu, token, mã kết nối máy từ xa hoặc dữ liệu cá nhân không cần thiết.**

Phương pháp học: **Học → Viết mã → Kiểm tra → Gỡ lỗi → Cải tiến → Lưu phiên bản → Chứng minh kết quả**.