# Kiểm tra Tuần 14

Chạy các lệnh từ thư mục gốc repository. Yêu cầu Python 3.12+ và pytest.

## 1. Kiểm tra bốn bài tập

    python weeks/week-14-oop-essentials/checks/check_student.py

Lệnh này chạy learner_tests trên các tệp trong exercises/.

## 2. Kiểm tra lời giải tham khảo và ví dụ

    python weeks/week-14-oop-essentials/checks/check_week.py

Lệnh này chạy tests/ với solutions/ và ví dụ Bot nhiều module. Đây là bộ test
riêng, không thay thế việc đọc hiểu lời giải.

## 3. Chạy riêng ví dụ Bot nhiều module

    python -m pytest weeks/week-14-oop-essentials/examples/test_oop_team.py -q

Kết quả PASS cho biết các test tự động đã chạy thành công. Hãy tự chạy lại,
đọc test và giải thích được vì sao từng kết quả được mong đợi.
