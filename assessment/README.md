# Python Journey AutoGrade — AG-01 + AG-02

**Lộ trình sinh viên Week 01–15:** xem [Cổng tự kiểm](STUDENT-PORTAL.md). Week 01 có chấm 11 tiêu chí/5 điểm thực hành; Week 02–14 tái sử dụng checker sinh viên đã có (chưa quy đổi điểm), Week 15 readiness cơ học, Week 09 dự án giảng viên đánh giá.

AutoGrade là **công cụ tự kiểm tại máy cá nhân**, không phải hệ thống chấm thi chính thức. Bộ chấm điểm số AG-01 chỉ hỗ trợ Week 01; AG-02 thêm lệnh `guide` và `selfcheck` các tuần sau (không tự phát điểm). Yêu cầu Python >=3.12.

## Hướng dẫn dành cho sinh viên

Mở [Hướng dẫn tự kiểm tra & đánh giá Week 01](../weeks/week-01-hello-python/assessment/STUDENT-GUIDE.md). Nội dung có quy trình Windows/macOS/Linux, cách đọc PASS/RETRY, báo cáo JSON, lỗi thường gặp và minh chứng 5 điểm chờ giảng viên.

## Bắt đầu

Ở thư mục gốc `python-journey`, sau khi đã tự sửa `weeks/week-01-hello-python/exercises/ex01_hello.py`, `ex02_calculator.py` và `mini-project/starter_basic.py`:

```bash
python -m assessment grade --week 01 --acknowledge-local-code
python -m assessment grade --week 01 --acknowledge-local-code --json-out .learner-output/week01.json
```

Nếu chỉ muốn kiểm bộ bài mẫu **không phải mã sinh viên**:

```bash
python -m assessment grade --week 01 --mode reference
```

Có thể đặt `--submission /path/to/workspace` để đánh giá một bản copy địa phương có bố cục `weeks/` như repository. Điểm tự động tối đa **5/5**, năm điểm còn lại (môi trường/REPL, sửa lỗi có minh chứng, Git/evidence) do giảng viên đánh giá. `official_score` luôn `null`; bản này không đăng điểm hoặc nộp dữ liệu lên mạng.

## Nguyên tắc kiểm định

- `checks/check_week.py` và bộ pytest của Week 01 vẫn chỉ kiểm lời giải/ví dụ giảng viên, **không chuyển đổi thành điểm sinh viên**.
- `ex03_input.py`, phần nhập tên của mini-project, và công cụ AI đều tùy chọn; **không trừ điểm W01**.
- Kết quả dựa vào stdout và dấu hiệu phép toán có trong AST để phản hồi; **không khẳng định quyền tác giả, chống gian lận hoặc đúng với mọi trường hợp**. Tên, sở thích và các kết quả định dạng đa dạng có thể cần giảng viên xem xét lại.
- File trong `assessment/fixtures/week01/reference/` là bài mẫu dành riêng để kiểm thử **máy chấm**, không phải bài nộp.
- Chương trình của người học có quyền chạy mã tùy ý khi thực thi. Subprocess, timeout và thư mục tạm **không phải sandbox**. Không dùng CLI này để chấm bài nộp từ người lạ, đặc biệt trên máy có secrets, dữ liệu thật hoặc trong workflow GitHub có token. Nếu muốn chấm tập trung, phải xây runner cô lập về network, filesystem, CPU/RAM và quyền truy cập trước.

## Tự kiểm các tuần còn lại

```bash
python -m assessment guide --week 02
python -m assessment selfcheck --week 02 --acknowledge-local-code
python -m assessment selfcheck --week 02 --acknowledge-local-code --json-out .learner-output/week02.json
```

Week 09: không có checker chung; dùng rubric dự án. Week 15: `python -m assessment selfcheck --week 15 --project path/to/my-project --acknowledge-local-code`. Cảnh báo: readiness dùng pytest collect nên chỉ chạy dự án tin cậy.

`selfcheck` chỉ gọi đúng checker STUDENT của tuần, `auto_score`/ `official_score` luôn `null`; không chấm thay bài tập gốc nằm ngoài phạm vi checker. Hướng dẫn và lệnh trực tiếp từng tuần: [cổng sinh viên](STUDENT-PORTAL.md).

## Mở rộng bộ chấm điểm chính thức

`assessment/engine/` tách cấu hình thang điểm (`rubric.json`), thực thi (`runner.py`), điều kiện kiểm tra (`evaluator.py`), và báo cáo máy đọc (`report.py`). Khi xây AG-03, cần bổ sung rubric điểm học phần được duyệt, test đa dạng và runner an toàn trước khi xem xét chấm tập trung. **Không tự nhận hệ thống hiện đã hỗ trợ 15 tuần**.

## Tiêu chí nghiệm thu

- Thư mục starter chưa hoàn thiện: tự kiểm `0/5`, báo `RETRY`, không báo PASS giả.
- Bộ fixture chuẩn: `5/5`, đầy đủ 11 tiêu chí.
- Một phép tính chỉ in kết quả cứng mà không có biểu thức: không đạt điều kiện phép toán tương ứng.
- Lỗi cú pháp, timeout, thiếu file: kết quả 0 ở tiêu chí liên quan, không làm vỡ hệ thống.
- JSON phân biệt `mode=student` và `mode=reference`; có mã kỹ năng, SHA-256 mã bài và rubric, điểm máy, chỗ chờ giảng viên; không chứa PII.
- Không thay đổi rubric `exercises/README.md`, học liệu, bài thi chính thức hay production.
