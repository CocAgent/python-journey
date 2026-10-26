# Tank Duel 2D

Game Pygame hai xe tăng nhìn từ trên xuống, dùng Python 3.10+.

## Chạy trên VS Code (Windows)

1. Mở VS Code → File → Open Folder → chọn thư mục `tank_duel`.
2. Mở Terminal → New Terminal (PowerShell), chạy:

Với Python 3.14, lệnh cài sẽ dùng `pygame-ce` (vẫn `import pygame` trong mã) để tải bản dựng sẵn. Với Python 3.10–3.13, lệnh cài dùng `pygame`.

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py main.py
```

Nếu PowerShell không cho kích hoạt môi trường, dùng trực tiếp `.venv\Scripts\python.exe -m pip install -r requirements.txt` rồi `.venv\Scripts\python.exe main.py`.

## Điều khiển

- Người 1: `W A S D` để đi và đổi hướng nòng; `Space` để bắn.
- Người 2: mũi tên để đi và đổi hướng nòng; `Enter` để bắn.
- Giữ nút bắn để bắn theo nhịp hồi 0,52 giây. Nhấn `Esc` để về menu.
- Phím `1`–`6` chọn mục trong menu; `Enter` xác nhận tên.

## Quy tắc

Mỗi xe có 100 HP. Đạn thường gây 20 sát thương; sau 180 giây, xe còn nhiều HP hơn thắng, bằng nhau thì hòa. Tường và thùng chặn xe, đạn và tầm nhìn; thùng có 60 HP và có thể bị phá. Bụi cây không chặn di chuyển/đạn, nhưng bot không nhìn thấy xe ở trong bụi từ bên ngoài; xe ở trong bụi vẫn được vẽ dưới lớp bụi. Bot chỉ bắn khi nhìn thấy xe đối thủ. Bot Địa ngục dự đoán theo vận tốc đang quan sát, thử hướng vòng khi gặp vật cản; đây là AI quy tắc, không đảm bảo luôn chọn được đường tối ưu.

Vật phẩm xuất hiện lần đầu sau 5 giây, rồi mỗi 7 giây: `H` hồi 30 HP (tối đa 100); `D` gây 30 thay vì 20 sát thương; `G` nhận 60% sát thương; `S` tăng tốc từ 165 lên 210 pixel/giây. Ba hiệu ứng kéo dài 8 giây và nhặt lại sẽ làm mới thời gian.

Xếp hạng dùng SQLite trong `ranking.db` (tạo khi xem bảng hoặc xong trận xếp hạng). Người mới 0 điểm; thắng +20, thua -10 (không dưới 0), hòa 0. Mỗi trận xếp hạng cập nhật số trận; thắng/thua chỉ tăng khi không hòa. Rank tính từ điểm hiện tại.

## Kiểm tra từng chế độ

1. **Đấu thường:** chọn `2`, kiểm tra hai bộ phím, bắn phá thùng và màn kết quả. Không tạo điểm hạng.
2. **Luyện tập:** chọn `1`, rồi lần lượt `1`–`4` để thử từng mức bot. Không cộng điểm.
3. **Máy vs Máy:** chọn `4`, chọn riêng mức bot 1 rồi bot 2; quan sát hai bot tự di chuyển/bắn.
4. **Vật phẩm:** chờ 5 giây, lái xe qua biểu tượng; kiểm tra HP hoặc số giây hiệu ứng trên giao diện.
5. **Xếp hạng:** chọn `3`, nhập hai tên khác nhau, kết thúc trận; xem điểm cũ, biến động và rank. Chọn `5` để kiểm tra bảng điểm. Thử nhập trùng tên để xem yêu cầu nhập lại.

## Cấu trúc và mở rộng

- `main.py`: menu, vòng lặp trận, hiển thị và điều khiển bàn phím.
- `entities.py`: xe, đạn, vật cản, quy tắc va chạm và hiệu ứng.
- `bots.py`: bốn cấp AI, trả lệnh đi/ngắm/bắn cho cùng đối tượng xe.
- `maps.py`: danh sách vị trí xuất phát, vật cản; thêm bản đồ bằng một cấu hình mới trong `MAPS` và chọn tên trong `make_game`.
- `ranking.py`: bảng SQLite và tính mức rank.

Tất cả người và bot dùng cùng `Tank.move()`, `Tank.shoot()` và `Tank.hit()`. Ở chế độ hai người, nên dùng bàn phím có khả năng nhận nhiều phím cùng lúc.

## Các tính năng mở rộng

- Chọn một trong ba bản đồ: Đấu trường, Pháo đài, Đồng trống. Mỗi hiệp đổi hai vị trí xuất phát để cân bằng.
- Chọn ngoại hình xe trước trận: Cổ điển, Trinh sát, Thiết giáp. Cả ba có cùng 100 HP, tốc độ và sát thương.
- Mỗi trận tối đa ba hiệp; người đầu tiên thắng hai hiệp thắng trận. Hiệp hòa không tính thắng; hết ba hiệp thì so số hiệp thắng. Chỉ cập nhật điểm hạng **một lần** sau cả trận hoàn tất. Rời trận sớm không cập nhật điểm.
- Mỗi hiệp đếm ngược 3, 2, 1. Bấm `P` để tạm dừng/tiếp tục; lúc dừng bấm `Esc` để về menu.
- Bốn loại đạn miễn phí: Thường (20 HP), Nhanh (bay nhanh và hồi bắn 0,38 giây), Nổ (vùng nổ bán kính 55 pixel, sát thương phụ 60% nếu không bị tường chắn), Xuyên thùng (phá thêm 40 HP thùng và bay tiếp). Người 1 nhấn `Q`, người 2 nhấn `Shift phải` để đổi loại; loại đạn hiện dưới thanh HP. Mọi xe cùng giới hạn và bot Khó/Địa ngục cũng biết đổi đạn.
- Âm thanh bắn, trúng đạn, nổ, nhặt vật phẩm được tổng hợp lúc chạy. Không có thiết bị âm thanh thì game vẫn chạy. Xe chớp trắng khi trúng đạn.
- Thùng đã vỡ hồi lại sau 25 giây nếu vị trí không bị xe chiếm.
- Trong 45 giây cuối mỗi hiệp, viền đỏ đánh dấu khu an toàn ở giữa; đứng ngoài chịu 5 HP mỗi giây.
- Menu `6` hiển thị 12 trận xếp hạng gần nhất, gồm người chơi, kết quả và điểm biến động. Dữ liệu lịch sử cùng nằm trong `ranking.db`.

### Kiểm tra tính năng mới

1. Chọn mục `2` → chọn từng bản đồ và kiểu xe → nhìn xe đổi ngoại hình, vị trí hoán đổi ở hiệp 2.
2. Vào trận, bấm `P`, quan sát thời gian đứng yên; bấm `P` để tiếp tục.
3. Nhấn `Q` hoặc `Shift phải` rồi bắn vào thùng để kiểm tra đạn xuyên; thử đạn Nổ gần mục tiêu.
4. Phá thùng rồi chờ 25 giây; chờ đồng hồ trận còn 45 giây để thấy khu nguy hiểm.
5. Kết thúc đủ các hiệp trong mục `3` rồi mở menu `5` xem điểm và menu `6` xem lịch sử. Thử rời trận giữa chừng bằng `Esc`: điểm không đổi.

## Font tiếng Việt

Game dùng font `assets/DejaVuSans.ttf` đi kèm để hiện dấu tiếng Việt giống nhau trên các máy Windows, không phụ thuộc font mặc định. Tệp `assets/FONT_LICENSE.txt` chứa giấy phép phân phối font. Khi chép dự án, hãy chép cả thư mục `assets`.
