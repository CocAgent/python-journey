# Week 12 — Sinh viên tự kiểm tra: Viết test với pytest

> Hướng dẫn tự học dùng **mã của chính sinh viên**. PASS của bài mẫu không phải điểm của bạn. Checker chỉ kiểm phần ghi bên dưới; giảng viên vẫn quyết định điểm học phần.

## 1. Chuẩn bị

Mở [README của tuần](../README.md), đọc notes, ví dụ và yêu cầu bài tập. Cài Python >=3.12 và mở Terminal ở thư mục gốc `python-journey`. Trên Windows có thể dùng `py`, trên macOS/Linux thường dùng `python3` thay cho `python`. Tải toàn bộ repository (ZIP hoặc Git), không chỉ một tệp `.py`.

**Phạm vi checker:** exercises/test_decision_starter.py; mutation checker có bốn lỗi cố ý.

**Hai hoạt động cần tự quan sát:** Bốn test phải PASS trên module đúng và phát hiện bốn lỗi mô phỏng. Giải thích vì sao assert True không kiểm được hành vi.

## 2. Viết, chạy và tự sửa

1. Xem `exercises/` và `mini-project/` để biết **yêu cầu chính**. Nếu checker của tuần dùng `practice/starter/`, đó chỉ là **lab bổ sung**, không thay bài tập gốc. Riêng Week 12/14, checker kiểm trực tiếp một phần `exercises/`.
2. Làm TODO bằng code của chính mình, lưu file (`Ctrl+S`). Thử một input thường, một input biên, một input sai. Ghi dự đoán trước khi chạy.
3. Xem đầu ra/traceback; khi FAIL, tìm đúng file sinh viên và sửa nguyên nhân. Không sửa checker, lời giải mẫu hoặc test để tạo PASS giả.
4. Nếu bí, đọc `hints.md` hoặc hướng dẫn practice trước; chỉ đối chiếu solutions sau khi tự thử.

## 3. Lệnh tự kiểm thống nhất

Đứng ở **gốc** `python-journey`:

```bash
python -m assessment guide --week 12
python -m assessment selfcheck --week 12 --acknowledge-local-code
```

`--acknowledge-local-code` nghĩa là bạn xác nhận chỉ chạy code **của mình hoặc đáng tin** tại máy cá nhân. Không có sandbox an toàn để chấm bài của người lạ. Checkers có thể thực thi/import mã sinh viên. **Cần pytest** theo tài liệu SETUP.

Nếu chưa cập nhật CLI mới, dùng lệnh checker sinh viên **có thật** của tuần:

```bash
python weeks/week-12-testing-pytest/checks/check_student_tests.py
```

Week 13 cần `cd` vào thư mục tuần khi dùng lệnh module trực tiếp; wrapper ở trên tự chọn thư mục đó.

## 4. Đọc trạng thái & xuất báo cáo

- **PASS / exit 0:** đạt bài trong phạm vi checker, **chưa phải điểm của toàn tuần**.
- **RETRY / exit 1:** còn lỗi; đọc tên lab hoặc test, expected/actual rồi tự sửa.
- **Lỗi cấu hình / exit 2:** kiểm tham số, đường dẫn, phiên bản Python hoặc dependency. Từng checker có thể có mã lỗi riêng.
- Starter ban đầu chưa làm TODO mà **FAIL/RETRY là đúng**, không phải máy bị hỏng.
- **Chỉ chạy chế độ STUDENT** (`--starter`, `check_student.py` hoặc wrapper); không dùng `--solutions`/`check_solutions.py`/`check_week.py` làm điểm sinh viên.

Xuất báo cáo **cục bộ**:

```bash
python -m assessment selfcheck --week 12 --acknowledge-local-code --json-out .learner-output/week12.json
```

Báo cáo ghi `mode: student`, `scope`, `status`, stdout, stderr và `auto_score: null`, `official_score: null`. **Không tự quy đổi PASS thành điểm 10**. Dùng cùng tên sẽ ghi đè báo cáo cũ; đổi tên nếu muốn giữ lịch sử. Không tự upload, báo cáo có thể chứa thông tin từ output bài làm.

## 5. Checklist và minh chứng

- [ ] Hoàn thành `exercises/` và mini-project chính theo yêu cầu tuần, ngoài phạm vi checker.
- [ ] Sửa đúng code sinh viên; thử input thường/biên/sai.
- [ ] Chạy đúng checker sinh viên, lưu PASS/RETRY thật.
- [ ] Ghi một lỗi tái hiện, cách sửa, command chạy lại và kết quả.
- [ ] Giải thích thuật toán/hành vi được; công khai việc dùng AI nếu có.
- [ ] Ghi commit hoặc hình thức nộp do giảng viên quy định; không gửi secrets.

Dùng [mẫu minh chứng dùng chung](../../../assessment/EVIDENCE-TEMPLATE.md). Giảng viên đánh giá các phần còn lại theo rubric hiện hành của tuần.
