# Kiểm tra Tuần 12 — hai mục đích khác nhau

## A. Kiểm thử phần sinh viên tự viết

```bash
python -m pytest weeks/week-12-testing-pytest/exercises/test_decision_starter.py -q
python weeks/week-12-testing-pytest/checks/check_student_tests.py
```

- Lệnh thứ nhất chạy trực tiếp bốn bài test sinh viên cần hoàn thành. Starter ban đầu **FAIL có chủ đích**.
- Lệnh thứ hai chạy bài test sinh viên trên chương trình đúng và bốn chương trình cố ý sai. Chỉ báo đạt khi bài làm PASS với chương trình đúng và **phát hiện đủ bốn lỗi**.
- Công cụ dùng file tạm, không ghi đè code sinh viên. Đây là hỗ trợ học tập, **không phải máy chấm điểm cuối cùng**.

## B. Kiểm thử lời giải tham chiếu của giáo trình

```bash
python -m pytest weeks/week-12-testing-pytest/tests -q
python weeks/week-12-testing-pytest/checks/check_week.py
```

Hai lệnh này kiểm tra **bộ tham chiếu** `tests/test_decision.py`, **không kiểm tra bài làm của sinh viên**.

## C. Chạy ví dụ trong bài giảng

```bash
python -m pytest weeks/week-12-testing-pytest/examples -q
```

**Quy tắc báo cáo:** ghi chính xác lệnh đã chạy, kết quả, và đó là test của ai. Không dùng kết quả PASS từ bộ tham chiếu để khẳng định một bài nộp đã đúng.

---

## D. Ví dụ tự kiểm tra lỗi qua nhiều tệp

```bash
python -m pytest weeks/week-12-testing-pytest/examples/test_multi_file_lab.py -q
python weeks/week-12-testing-pytest/checks/check_multi_file_faults.py
```

Ví dụ gồm **8 ca kiểm thử** và **6 lỗi giả lập trong `pricing.py`, `storage.py`, `service.py`**. Chỉ chạy trên file tạm, không sửa bài nộp. Đây là **kiểm thử chất lượng tài liệu mẫu**, không phải bài tự động chấm sinh viên. Xem [hướng dẫn](../examples/multi_file_lab/README.md).
