# Mini-project — Bộ kiểm thử cho bot ra quyết định

## Bối cảnh

Bot có một vị trí `position` và một đích đến `goal`. Bot chỉ được chọn ba hành động: `"left"`, `"right"` hoặc `"wait"`.

Bạn là người kiểm thử: nhiệm vụ của bạn là chứng minh bot ra quyết định đúng **trong các tình huống cụ thể**, kể cả khi ai đó vô tình sửa hỏng code.

## Yêu cầu

1. Tự hoàn thành bốn test trong [file starter](../exercises/test_decision_starter.py).
2. Viết thêm **ít nhất hai bộ dữ liệu độc lập**: ví dụ bot đi từ 0 tới 4, hoặc đứng yên khi vị trí bằng mục tiêu.
3. Chọn một phép kiểm tra đã viết và giải thích tại sao `assert action in LOCAL_ACTIONS` chưa đủ.
4. Chạy công cụ kiểm tra lỗi cố ý và ghi lại ít nhất một trường hợp test phát hiện được chương trình sai.
5. Viết báo cáo ngắn: *Tình huống → Mong đợi → Thực tế → Kết quả → Điều rút ra*.

Không cần tạo class, cài công cụ mới hoặc sửa nguồn của dự án Vua Cóc.

## Các lệnh cần chạy ở thư mục gốc repository

```bash
# Chạy bài test do chính bạn hoàn thành.
python -m pytest weeks/week-12-testing-pytest/exercises/test_decision_starter.py -q

# Thử bộ test với bốn lỗi giả lập.
python weeks/week-12-testing-pytest/checks/check_student_tests.py
```

Lệnh sau chỉ để đối chiếu **test tham chiếu** (không chấm bài của bạn):

```bash
python weeks/week-12-testing-pytest/checks/check_week.py
```

## Mẫu báo cáo 5 dòng

```text
1. Tôi muốn xác nhận hành vi:
2. Đầu vào thử nghiệm và kết quả mong đợi:
3. Kết quả thực tế (PASS/FAIL, ghi lệnh đã chạy):
4. Lỗi cố ý mà bộ test phát hiện:
5. Vì sao tôi tin rằng phép kiểm tra này có ích:
```

## Thử thách tự chọn

Nếu đã xong, dùng `@pytest.mark.parametrize` gom các trường hợp đi phải, đi trái và đứng yên trong một hàm test. Chỉ làm khi bạn giải thích được mỗi hàng dữ liệu đại diện cho hành vi nào.
