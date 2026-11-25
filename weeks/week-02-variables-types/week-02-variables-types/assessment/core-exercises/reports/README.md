# Báo cáo cá nhân — lưu cục bộ, không commit

Khi sinh viên chạy:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student
```

Máy tạo **`week02-journey.html`** và **`week02-result.json`** trong thư mục này. Mở file HTML trên trình duyệt để xem tiến độ ba chặng, điểm từng TODO, trạng thái PASS/RETRY/REVIEW và ba cấp gợi ý. JSON dùng để máy đọc hoặc lưu minh chứng.

- File kết quả được `.gitignore` bảo vệ, không tự commit/push.
- Không tự gửi báo cáo hoặc bài làm ra Internet; không chứa stdout và biến cá nhân.
- Điểm chỉ là **tự luyện /10**, trường `official_score` luôn `null`.
- Để kiểm tra tất cả tập test mà **không chạy bài sinh viên**, dùng `grader.py --audit-tests`.
- Không tải/chạy mã sinh viên lạ trên máy giảng viên, CI có secrets hoặc VPS; đây không phải sandbox.
