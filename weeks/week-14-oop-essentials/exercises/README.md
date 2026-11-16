# Bốn bài tập OOP — Sinh viên tự hoàn thành

Các tệp `ex01_` đến `ex04_` là **starter**, chưa có đáp án. Khi chưa làm,
`NotImplementedError` là dấu hiệu cố ý để không có PASS giả.

1. **[ex01_classes.py](ex01_classes.py):** tạo `Progress(completed, total)` có
   `percentage()`, `__str__()`. Từ chối `total <= 0` hoặc `completed`
   ngoài `[0, total]`. `str(Progress(3, 4))` phải đúng
   `"Progress: 3/4 (75%)"`.
2. **[ex02_composition.py](ex02_composition.py):** tạo `Bot(strategy)` có
   `choose_action(state)`; tự viết `defensive`, `balanced`, `aggressive`.
   Cả ba hoạt động với đích trái/phải/đã đến; defensive phải đứng yên khi
   đối thủ cách tối đa 1 ô. Thay `bot.strategy` phải đổi hành vi.
3. **[ex03_inheritance.py](ex03_inheritance.py):** tạo `Animal(name)`, `Dog(Animal)`;
   `Dog("Milo").speak()` trả `"Milo: woof"`. Giải thích bằng một câu
   vì sao Dog “là một” Animal.
4. **[ex04_dien_thoai.py](ex04_dien_thoai.py):** tạo `DienThoai` có thuộc tính
   `ma_may`, `ten_may`, `hang_san_xuat`, `dung_luong_pin`,
   `gia_ban`. `thongtindienthoai()` **trả chuỗi** đủ năm thông tin.
   Từ chối chuỗi rỗng, pin không dương, giá âm. Tạo hai object như bên dưới.

| Mã | Tên máy | Hãng | Pin (mAh) | Giá (VND) |
|---|---|---|---:|---:|
| DT01 | iPhone 15 Pro | Apple | 3274 | 28.990.000 |
| DT02 | Galaxy S24 Ultra | Samsung | 5000 | 29.990.000 |

## Cách kiểm tra **bài của mình**

Tại thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/checks/check_student.py
```

- Chưa làm: test phải FAIL vì `NotImplementedError`.
- Làm đúng: các test tự động cần PASS.
- PASS không thay thế việc giải thích thiết kế và đánh giá của giảng viên.
- Bài của sinh viên nằm trong `exercises/`, không sửa `solutions/`
  để đánh lừa kết quả kiểm tra.

**Bài nộp:** bốn tệp đã hoàn thành, kết quả kiểm thử thực tế và giải thích
ngắn về `self`, composition, inheritance và lý do kiểm tra dữ liệu.
