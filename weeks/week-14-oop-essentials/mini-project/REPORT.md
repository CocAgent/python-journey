# Báo cáo Mini-project Tuần 14 — Bot chiến lược qua nhiều module

1. **Trách nhiệm của mỗi tệp:** `bot.py` định nghĩa lớp `Bot` gom dữ liệu và ủy quyền hành động qua composition; `strategies.py` chứa các hàm chiến lược độc lập (`defensive`, `balanced`, `aggressive`); `main.py` chạy thử nghiệm kịch bản minh họa; `test_bot.py` chứa bộ test pytest tự động.
2. **Dữ liệu đầu vào:** Từ điển `state` gồm vị trí hiện tại `position`, vị trí đích `goal`, và vị trí đối thủ tùy chọn `opponent_position`.
3. **Kết quả mong đợi:** Bot phòng thủ dừng lại khi đối thủ áp sát (cách <= 1 ô); Bot cân bằng đi về đích ở cả 2 hướng (trái/phải) và đứng yên tại đích; đổi chiến lược linh hoạt lúc chạy mà không sửa lớp `Bot`; không làm thay đổi dữ liệu của `state`.
4. **Kết quả thực tế từ pytest:** Toàn bộ 7/7 bài test trong `test_bot.py` PASS 100%.
5. **Lỗi đã phát hiện và xử lý:** Nguy cơ `KeyError` khi `opponent_position` không tồn tại trong `state` -> được xử lý an toàn bằng phương thức `state.get('opponent_position')`.
