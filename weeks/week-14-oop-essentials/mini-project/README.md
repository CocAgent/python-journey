# Mini-project — Bot chiến lược qua nhiều module

## Yêu cầu

Tạo một Bot có thể nhận và thay thế chiến lược, đồng thời tách code thành
**ít nhất hai file**: `bot.py` chứa class `Bot`, `strategies.py` chứa
các hàm chiến lược. Bạn có thể tạo thêm `main.py` để chạy thử và
`test_bot.py` để viết pytest.

Không sửa code arena thật của Vua Cóc; chỉ làm ví dụ ngoại tuyến một chiều.

## Hành vi cần chứng minh

- `Bot(defensive)` đứng yên khi đối thủ ở sát (trong phạm vi một ô).
- `Bot(balanced)` đi về đích bên trái **và** bên phải.
- Đang ở đích thì Bot đứng yên.
- Đổi từ `defensive` sang `balanced` chỉ thay `bot.strategy`, không sửa `Bot`.
- Nếu state thiếu `opponent_position`, defensive vẫn chạy.
- Lưu trạng thái đầu vào rồi đối chiếu: hàm không tự sửa `state`.

## Hướng dẫn

Xem [ví dụ ba module](../examples/oop_team/README.md) để tham khảo cách
chia nhiệm vụ. **Không sao chép nguyên mẫu**: thay đổi dữ liệu thử và giải
thích được vì sao chọn composition thay vì inheritance.

```bash
python -m pytest weeks/week-14-oop-essentials/examples/test_oop_team.py -q
python weeks/week-14-oop-essentials/checks/check_student.py
```

Lệnh đầu chỉ kiểm tra **ví dụ giảng viên**. Lệnh thứ hai kiểm tra **bốn bài tập
trong `exercises/`**. Muốn kiểm thử dự án riêng, sinh viên cần chạy
`python -m pytest` trỏ vào `test_bot.py` mà mình viết.

## Báo cáo ngắn

Viết 5 dòng: trách nhiệm của mỗi tệp, dữ liệu đầu vào, kết quả mong đợi,
kết quả thực tế từ pytest, và một lỗi đã phát hiện/sửa. Bài nộp gồm mã nguồn,
test, ghi nhận lệnh chạy và giải thích.
