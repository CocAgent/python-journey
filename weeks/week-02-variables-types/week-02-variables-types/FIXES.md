# Nhật ký sửa lỗi

- **Bộ chấm (`runner_w02.py`, `autograde_w02.py`)**: tiến trình con crash `UnicodeEncodeError` trên Windows (cp1252) khi bài làm in chữ có dấu, làm TODO bị chấm lỗi (kể cả BMI). Nay JSON ASCII-safe và ép `-X utf8`.
- **`practice/checks/check_practice.py`**: ép UTF-8 khi chạy bài luyện.
- **`exercises/ex02` TODO 4 (BMI)**: nhận `1,75` (dấu phẩy), `175` (cm → m), báo lỗi khi chiều cao/cân nặng ≤ 0 thay vì `ZeroDivisionError`.
- **`exercises/ex03`, `solutions/ex03`**: số thực nhập bằng dấu phẩy không còn `ValueError`.
- **`html/week02-journey.html`**: ô số dùng `inputmode="decimal"`, nhận dấu phẩy; BMI tự đổi cm → m; mẫu Python trong Playground cũng nhận dấu phẩy.
