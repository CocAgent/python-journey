# Gợi ý theo từng mức — Tuần 14

Hãy thử tự làm, chỉ đọc mức tiếp theo khi còn vướng. Không dùng gợi ý để
bỏ qua việc tự viết code.

## Bài 1 — Progress

- **Mức 1:** Mỗi tiến độ cần lưu những thuộc tính nào?
- **Mức 2:** `completed` phải nằm giữa 0 và `total`; `total` không thể là 0.
- **Mức 3:** `percentage()` trả kết quả, `__str__()` trả chuỗi; cả hai không nên tự in.

## Bài 2 — Bot và chiến lược

- **Mức 1:** Truyền hàm vào `Bot(strategy)` cũng giống truyền một giá trị.
- **Mức 2:** `choose_action` gọi `self.strategy(state)`, không quyết định thay strategy.
- **Mức 3:** So sánh `position` với `goal` để chọn left/right/wait.
- **Mức 4:** Dùng `state.get("opponent_position")` vì có thể thiếu thông tin đối thủ.
- **Thử lỗi:** Bot với goal=0 có được đi trái không? Đổi `bot.strategy` có đổi kết quả không?

## Bài 3 — Animal và Dog

- **Mức 1:** `Dog(Animal)` biểu thị quan hệ “là một”.
- **Mức 2:** `Dog` có thể dùng `self.name` được `Animal` khởi tạo.
- **Thử lỗi:** `isinstance(Dog("Milo"), Animal)` có đúng không?

## Bài 4 — DienThoai

- **Mức 1:** `__init__` nhận năm giá trị rồi lưu bằng `self.`.
- **Mức 2:** Cần từ chối mã/tên/hãng rỗng, pin ≤ 0, giá < 0.
- **Mức 3:** `thongtindienthoai` trả chuỗi đủ năm trường; mã gọi `print()` ở ngoài.
- **Thử lỗi:** tạo hai điện thoại: chúng có các thuộc tính độc lập không?

## Khi pytest báo FAIL

Đọc **tên test → dữ liệu vào → actual/expected → traceback**.
Đừng xóa test, đổi assert cho qua hoặc thay `NotImplementedError` bằng `pass`.
