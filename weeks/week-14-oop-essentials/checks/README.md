# Kiểm tra Tuần 14 — Hai phạm vi riêng

**1. Bài tập của sinh viên** (đây mới là lệnh kiểm tra mã của bạn):

```bash
python weeks/week-14-oop-essentials/checks/check_student.py
```

Chạy `learner_tests/test_exercises.py` trên mã ở `exercises/`.
Starter chưa làm **báo FAIL đúng thiết kế**. Khi hoàn thành đúng, test cần PASS;
giảng viên vẫn phải đánh giá giải thích và chất lượng bài làm.

**2. Lời giải tham chiếu và ví dụ** (chỉ để kiểm tra chất lượng giáo trình):

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Lệnh này chạy `tests/` với `solutions/` và các ví dụ. Kết quả PASS
**không chứng minh bài sinh viên đúng**.

**3. Ví dụ Bot nhiều module**

```bash
python -m pytest weeks/week-14-oop-essentials/examples/test_oop_team.py -q
```

Không thay đổi tên tệp bài tập chỉ để chạy check. Tất cả lệnh cần thực thi
ở thư mục gốc repository; yêu cầu Python 3.12+ và pytest.
