# Bộ kiểm thử của Python Journey — hướng dẫn cho giảng viên và maintainer

Thư mục `tests/` là **maintainer CI**, dùng xác nhận giáo trình Python Journey không bị lỗi cấu trúc hoặc hồi quy. **Không phải kho bài nộp hoặc đáp án thi**, và không tự động chấm sinh viên.

## Các nhóm test

| Tệp | Đánh giá gì | Không đánh giá |
|---|---|---|
| `test_course_structure.py` | Cấu trúc 15 tuần, hợp đồng course, một số lệnh tham chiếu | Mã sinh viên |
| `test_week_owned_checks.py` | Chỉ gọi các lệnh kiểm thử tại tuần sở hữu (09/12/14) trong CI | Không lưu đáp án hay logic test của từng tuần |
| `test_assessment_reference.py` | So khớp output, trạng thái chạy, timeout, tổng điểm 5 x 2 | Bài thi thật hay độ chính xác máy chấm |

`assessment_reference.py` là helper dành **chỉ cho test ví dụ tin cậy**; không được quảng bá là sandbox/chấm thi an toàn.

## Bài kiểm thử gắn với từng tuần nằm ở đâu?

| Tuần | Nguồn kiểm thử / kiểm tra chính | Lệnh chạy độc lập |
|---|---|---|
| 09 | `weeks/week-09-midterm-project/checks/check_project_catalog.py` | `python weeks/week-09-midterm-project/checks/check_project_catalog.py` |
| 12 | `weeks/week-12-testing-pytest/examples/test_multi_file_lab.py` và `checks/check_multi_file_faults.py` | `python -m pytest weeks/week-12-testing-pytest/examples/test_multi_file_lab.py -q` |
| 14 | `weeks/week-14-oop-essentials/tests/` và `checks/check_week.py` | `python weeks/week-14-oop-essentials/checks/check_week.py` |

**Nguyên tắc tổ chức:** mỗi tuần sở hữu test, ví dụ và checker của mình. `tests/test_week_owned_checks.py` là **cầu nối CI**, chỉ gọi lại chúng bằng Python trong tiến trình riêng; không viết lại logic chấm ở cấp gốc. Thư mục `tests/` giữ những kiểm tra xuyên suốt 15 tuần và ví dụ về chất lượng chấm dùng chung. Bài sinh viên ở `exercises/` hoặc `learner_tests/` được chạy **riêng**, không qua cầu nối này.

## Bối cảnh tài liệu nguồn trên Drive

Thư mục **Tests Python 2026** của giảng viên có các thư mục đề và script thử nghiệm thuộc nhóm CB / NC / ND, tệp tổng hợp các đề và cả `submissions/`. Chúng tôi chỉ dùng **kiến trúc và lỗi điển hình** làm căn cứ cho test bảo vệ giáo trình.

Đọc [báo cáo rà soát và kế hoạch tích hợp](LEGACY_ASSESSMENT_REVIEW.md) trước khi muốn xây hệ chấm bài thực tế. **Không commit** mã bài nộp, thông tin sinh viên, kết quả thi hay đáp án riêng lên GitHub công khai.

## Chạy kiểm thử tại thư mục gốc repo

```bash
# Chạy toàn bộ maintainer test mặc định theo pyproject.toml.
python -m pytest

# Chỉ thử các nguyên tắc kiểm thử/chấm mẫu.
python -m pytest tests/test_assessment_reference.py -q

# Đúng cổng kiểm tra bảo trì của khóa.
python scripts/verify_course.py
ruff check scripts tests projects/vuacoc-bot-journey
```

**Pytest PASS không đồng nghĩa bài sinh viên PASS.** Các bài tập starter cố ý chưa hoàn thành được test bằng lệnh riêng ở từng tuần, ví dụ `weeks/week-12-testing-pytest/checks/check_student_tests.py` và `weeks/week-14-oop-essentials/checks/check_student.py`.

## Quy tắc chất lượng cho hệ chấm trong tương lai

1. Kết quả phải so khớp đúng **hành vi đã định nghĩa**, không nhận nhầm `"1"` là `"100"`.
2. Không cho điểm nếu chương trình crash, timeout hoặc không chạy được.
3. Có rubric công khai (5 câu × 2 điểm là **một ví dụ**), mẫu test đầy đủ và khả năng tái hiện.
4. Tách mã tham chiếu, mã sinh viên, kết quả kiểm thử và dữ liệu định danh.
5. Đối với mã **không tin cậy**: cần runner/container riêng, không có secrets, hạn mức CPU/RAM/thời gian, cô lập hệ tệp và mạng; `subprocess.run(timeout=...)` **không phải môi trường cô lập an toàn**.
6. Chấm tự động chỉ là bằng chứng một phần; giảng viên cần quy trình xử lý tranh chấp, lỗi môi trường và kiểm tra thủ công khi phù hợp.

Tài liệu này không bổ sung chức năng chấm điểm lên production hoặc xử lý bất kỳ bài nộp thực nào.
