# Rà soát tài liệu “Tests Python 2026” và hướng tích hợp an toàn

**Nguồn kiểm tra:** thư mục Google Drive mà giảng viên cung cấp, không phải một phần của repository. Báo cáo này chỉ tóm tắt tổ chức và mẫu rủi ro quan sát được; không đưa bài thi, đáp án hoặc thông tin sinh viên lên GitHub.

## 1. Những gì đã nhận diện

- Có các nhóm thư mục cho đề CB 01/02, kiểm thử CB, NC và ND; mỗi nhóm có thể chứa `test_de1.py`, `test_de2.py`, `autograde_de1_v1.py`, `autograde_de1_v2.py` hoặc script tương tự.
- Thư mục gốc có `Python_Test_Validation.pdf`, tài liệu tổng hợp nhiều đề 90 phút, các câu về phép toán, `list/dict/set`, hàm, chuỗi, OOP và ở một số đề còn có thao tác file.
- Các thư mục `submissions` và `submissions_de{1,2}` có thể chứa bài nộp. **Không chuyển chúng vào repository**.
- Một script `autograde_de1_v2.py` được đọc làm mẫu cho thấy so khớp đáp án sau khi loại bỏ khoảng trắng, một số dấu câu, và dùng so sánh **chuỗi con**. Script cũng dùng `except:` không định danh khi thử phân tích dict.
- Trong script mẫu đó, từng ca đúng được cộng 1,5 điểm và `max_score` cộng 1,5 theo phần; tuy nhiên phần in kết quả lại cố định nhãn `/10`. Đây là **bất nhất cần rà soát**, không nên sao chép logic sang nơi khác.
- Script mẫu chạy `python <file>` với timeout 3 giây, nhưng không cung cấp cơ chế cô lập mã không đáng tin cậy, giới hạn tài nguyên tổng thể hoặc chống truy cập mạng.

**Giới hạn quan sát:** những phát hiện về logic chấm dựa trên các file mẫu đã xem, **không kết luận mọi bản `v1/v2` hoặc mọi kỳ thi đều mắc cùng lỗi**. Cần kiểm toán theo từng đề trước khi dùng thật.

## 2. Những điểm bắt buộc phân biệt

| Nguồn lịch sử | Bộ test `tests/` trên GitHub | Cách xử lý |
|---|---|---|
| Đề kiểm tra `.pdf` | Kiểm thử chất lượng giáo trình | Giữ ở Drive; không công khai lại |
| `test_de*.py` có expected output | Ví dụ logic so khớp chặt chẽ | Không chuyển đáp án thi vào public CI |
| `autograde_*v1/v2.py` | Bài học về chấm đáng tin cậy | Viết lại và kiểm định riêng nếu muốn chấm thực |
| `submissions*` | Không nằm trong phạm vi maintainer | Giữ nguyên vị trí và quyền truy cập |
| Rubric thi 5 câu × 2 điểm trong tệp tổng hợp | Mẫu `illustrative_exam_score` | Chỉ minh họa cách tính đúng tối đa 10; không tự động áp cho đề khác |

Tệp tổng hợp có cả nội dung thuộc **Tuần 10 (file)** và **Tuần 14 (OOP)**, trong khi giáo trình có tiến độ 15 tuần. Không đưa các bài đó vào test đánh giá đầu ra của Tuần 09.

## 3. Kiểm tra hồi quy mới

`test_assessment_reference.py` dùng toàn bộ dữ liệu **giả lập và chương trình do maintainer tự tạo** để bảo đảm:

- Sai output, sai chữ hoa/thường, sai dòng, so khớp chuỗi con không được tính đúng.
- Script in ra kết quả đúng rồi crash vẫn phải FAIL.
- Chạy quá thời gian không được PASS.
- Câu hỏi chia đều điểm trên các ca hợp lệ; năm câu × hai điểm đúng tối đa 10.
- Mọi tập ca thiếu, sai kiểu hoặc sai số câu đều được từ chối, không im lặng cho điểm.

## 4. Những việc CHƯA thực hiện

- **Chưa** kiểm định mọi đề PDF, đáp án và mọi script `autograde_`.
- **Chưa** thu thập, mở, thực thi hoặc chấm bất kỳ bài nộp sinh viên nào.
- **Chưa** đồng bộ dữ liệu nhạy cảm hoặc bản PDF đề thi lên GitHub.
- **Chưa** triển khai sandbox đa tiến trình, chống gian lận, lưu bảng điểm hay hệ thống chấm production.
- **Chưa** thay đổi quyền truy cập hoặc tổ chức trong Drive.

Nếu cần vận hành chấm bài thật, bước tiếp theo phải là kiểm toán từng bộ đề và đặc tả I/O, khóa phiên bản rubric, thiết lập cô lập chạy code không tin cậy, kiểm tra các trường hợp chuẩn/biên/sai và quy trình xem xét của giảng viên.
