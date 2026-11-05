# Bài tập Week 13 — tự làm trước khi xem solutions

## Bài tập tương tự để em tự luyện

Nếu đã hoàn thành bài tập gốc mà vẫn thấy khó chuyển sang dữ liệu khác,
đọc [sổ tay bốn lab có ví dụ giải từng bước](../GUIDED-LABS.md) và
[bài tự luyện Study Progress](../practice/README.md). Đây là bộ bài
**riêng**, không thay thế các starter `ex01_modules`–`ex04_adapter`.


**Chạy từ week root** (thư mục `weeks/week-13-modules-cli-api/`):

```bash
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
python -m exercises.ex04_adapter
```

Các starter **cố ý chưa hoàn thiện TODO**, nhưng phải là Python hợp lệ.
Sau khi điền mã, đối chiếu kết quả:

| Bài | Việc cần hoàn thiện | Output mục tiêu / test lỗi |
|---|---|---|
| 01 | import `choose_action`, main guard | `Hành động: right`; import module không in gì |
| 02 | `argparse --turn` integer bắt buộc | `--turn 3` cho 3; thiếu/không phải số → argparse lỗi |
| 03 | parse fixture 200, xử lý status 500 | `Lesson: 13`; 500 → ValueError được bắt |
| 04 | gọi adapter và kiểm invalid input | `left` khi position=3, goal=1; `True` bị từ chối |

**Tại sao phải dùng `python -m`?** Vì bài `ex01`/`ex03`/`ex04`
import package `bot_course` nằm cùng cấp thư mục `exercises/`.
Nếu chạy `python exercises/ex03_http.py`, import path có thể không tìm
thấy `bot_course`.

**Tự đánh giá:** em có thể giải thích một lỗi, không chỉ copy output.
Khi bí, đọc [hints](../hints.md), sau đó [solutions](../solutions/README.md).
Check tham khảo `checks/check_week.py` xác minh **reference solution**,
không có nghĩa TODO của em đã hoàn tất.
