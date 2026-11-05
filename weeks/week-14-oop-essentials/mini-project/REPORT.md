# Báo Cáo Ngắn — Mini-project Tuần 14: Bot Chiến Lược Đa Module

1. **Trách nhiệm của mỗi tệp:**
   - `bot.py`: Định nghĩa lớp `Bot` tuân thủ nguyên lý Composition, ủy quyền toàn bộ việc ra quyết định cho `self.strategy(state)`.
   - `strategies.py`: Định nghĩa các hàm chiến lược độc lập (`defensive`, `balanced`, `aggressive`), dễ mở rộng mà không chạm vào `Bot`.
   - `main.py`: Kịch bản mẫu mô phỏng hoạt động và hoán đổi chiến lược runtime.
   - `test_bot.py`: Bộ kiểm thử pytest tự động xác thực toàn bộ các quy tắc biên.

2. **Dữ liệu đầu vào:**
   - Từ điển `state` gồm tọa độ `position` (int), mục tiêu `goal` (int) và tùy chọn vị trí đối thủ `opponent_position` (int).

3. **Kết quả mong đợi:**
   - Bot phòng thủ dừng lại khi đối thủ cách $\le 1$ ô; di chuyển đúng hướng hai chiều khi an toàn; đứng yên khi ở đích; đổi chiến lược mà không sửa lớp `Bot`; không gây đột biến dữ liệu `state`.

4. **Kết quả thực tế từ pytest:**
   - 8/8 tests tự động trong `test_bot.py` đều PASS (100%), không phát sinh cảnh báo hay ngoại lệ không mong muốn.

5. **Lỗi/trường hợp biên đã phát hiện và xử lý:**
   - Xử lý biên trường hợp thiếu `opponent_position` bằng phương thức `state.get(...)` thay vì truy cập chỉ mục trực tiếp `state[...]` để tránh lỗi `KeyError`.
   - Dùng hàm `abs(opponent - position) <= 1` để kiểm tra khoảng cách an toàn chính xác cho cả đối thủ ở bên trái và bên phải.
