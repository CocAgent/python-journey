# Bài nộp Week 02 — Trương Gia Hiên

Trương Gia Hiên · MSSV: 2125110165 · Lớp: CCQ2511E

Bài nộp riêng cho PR #254, theo cách tách bài tại [quy định submissions](../README.md). Nền giáo trình: `d6192585ff13b9f204e1d441898ddd1d86b472ae`.

- `exercises/`: ba bài tập gốc, gồm TODO bắt buộc và thử thách.
- `practice/starter/`: ba lab Profile, Shop, Ticket đã điền.
- `mini-project/starter.py`: bản sao mini-project có sẵn để chạy với dữ liệu sinh viên; giữ nguyên code của giáo trình.
- Tuổi 18 và điểm 8.0 trong bài biến là dữ liệu minh họa.

Giữ nguyên code/comment có sẵn trong các bản sao; thêm lời giải dưới TODO. Các file dùng chung, rubric, checker và test ngoài thư mục bài nộp được giữ nguyên.

## Tự kiểm ba bài tập gốc

Chạy từ thư mục gốc repository bằng Python 3.12+, sau khi đã đọc và tin cậy code:

```powershell
$env:PYTHONUTF8 = '1'
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --audit-tests
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student --submission weeks/week-02-variables-types/submissions/2125110165 --acknowledge-local-code
```

Kết quả tự kiểm đã chạy: **10/10**, 10 TODO bắt buộc và 24 bộ input động. Thử thách, lab và mini-project nằm ngoài điểm /10; điểm chính thức chờ giảng viên đánh giá.

## Chạy các bài bổ sung

```powershell
python weeks/week-02-variables-types/submissions/2125110165/practice/starter/lab01_profile.py
python weeks/week-02-variables-types/submissions/2125110165/practice/starter/lab02_shop.py
python weeks/week-02-variables-types/submissions/2125110165/practice/starter/lab03_ticket.py
python weeks/week-02-variables-types/submissions/2125110165/mini-project/starter.py
```

Lab Ticket: thử `Lan`, `2` để có 24,000 VND; thử `abc`, `0`, `-1` để kiểm từ chối số vé sai. Thẻ sinh viên: nhập Trương Gia Hiên, 2125110165, IT, 2025; thử lại với năm `abc`.

Các dòng thông báo TODO có sẵn trong lab được giữ nguyên theo yêu cầu bảo toàn code gốc. Bộ tự kiểm ba lab và các lần chạy hợp lệ/không hợp lệ đã được kiểm tra ở local. HTML/JSON từ máy chấm được lưu riêng trên máy, không đưa vào bài nộp. Không tự chạy code bài nộp trong CI của giáo trình.
