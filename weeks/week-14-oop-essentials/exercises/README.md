# Bốn bài tập OOP — Đã có lời giải trong mã nguồn

Bốn tệp dưới đây hiện chứa lời giải tham khảo để bạn có thể chạy và đối chiếu.
Hãy đọc đề, thử tự giải trước, sau đó so sánh cách làm và tự giải thích được
các điều kiện kiểm tra cũng như kết quả.

1. **ex01_classes.py:** class Progress, kiểm tra total > 0, completed trong
   [0, total], tính phần trăm và định dạng __str__.
2. **ex02_composition.py:** class Bot nhận strategy qua composition; có
   defensive, balanced, aggressive; đổi bot.strategy để đổi hành vi.
   Mô hình di chuyển một chiều trái/phải/đứng yên.
3. **ex03_inheritance.py:** Dog kế thừa Animal, dùng lại name và bổ sung
   phương thức speak().
4. **ex04_dien_thoai.py:** class DienThoai, xác thực dữ liệu và tạo hai object
   iPhone 15 Pro, Galaxy S24 Ultra.

## Chạy kiểm tra

Tại thư mục gốc repository:

    python weeks/week-14-oop-essentials/checks/check_student.py
    python weeks/week-14-oop-essentials/checks/check_week.py

check_student.py kiểm tra các tệp trong exercises/. check_week.py kiểm tra
lời giải tham khảo và ví dụ. Hai lệnh có mục đích riêng; PASS không thay thế
việc bạn tự đọc hiểu và giải thích code.

Bài nộp gợi ý: chạy test, chụp kết quả, giải thích self, composition,
inheritance, lý do kiểm tra dữ liệu và một trường hợp biên.
