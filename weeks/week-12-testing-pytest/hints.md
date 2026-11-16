# Gợi ý từng bước — Tuần 12

> Hãy thử viết ít nhất một phép kiểm tra trước khi mở gợi ý. Tài liệu này không cung cấp sẵn cả bài làm.

## Bài 1 — Bot tiến về phía mục tiêu

- **Gợi ý 1:** Nếu `position < goal`, hướng đi hợp lý là gì?
- **Gợi ý 2:** Lưu kết quả `choose_action(...)` vào biến `action`.
- **Gợi ý 3:** Dùng `assert action == ...` với **một kết quả duy nhất**, không dùng `in LOCAL_ACTIONS`.

## Bài 2 — Bot đã tới đích

- **Gợi ý 1:** Khi vị trí và mục tiêu bằng nhau, bot còn cần đi nữa không?
- **Gợi ý 2:** Chọn một giá trị từ `"left"`, `"right"`, `"wait"`.
- **Gợi ý 3:** Nếu code sai luôn trả về `"right"`, test của bạn có thất bại không?

## Bài 3 — Lượt chơi bằng 0

- **Gợi ý 1:** Hàm `validate_turn(0)` cần trả một số hay báo lỗi?
- **Gợi ý 2:** Nhập `pytest` và dùng khối `with pytest.raises(ValueError):`.
- **Gợi ý 3:** Hãy đặt câu lệnh gọi hàm **bên trong** khối `with`.

## Bài 4 — Lỗi đi nhầm hướng

- **Gợi ý 1:** Vị trí lớn hơn mục tiêu nghĩa là đi sang đâu?
- **Gợi ý 2:** Xem lại lỗi cũ: bot lúc nào cũng đi `"right"`.
- **Gợi ý 3:** Một phép kiểm tra chỉ xem action có hợp lệ sẽ không phát hiện lỗi cũ.

## Khi chương trình báo FAIL

1. Chạy lại một test theo tên bằng `python -m pytest duong_dan::ten_test -q`.
2. So sánh kết quả **thực tế** và **mong đợi**.
3. Đọc điều kiện đầu vào của hàm.
4. Không xóa test hoặc đổi `assert` cho qua; hãy sửa lý do sai.

## Khi công cụ thử lỗi báo còn thiếu

Nếu `check_student_tests.py` thông báo chưa phát hiện một lỗi cố ý, xem mô tả lỗi, nghĩ ra đầu vào khiến chương trình đúng và sai có kết quả khác nhau, rồi viết một phép kiểm tra cụ thể.
