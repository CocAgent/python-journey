# Minh chứng học tập Tuần 01 — sinh viên tự điền

- Python version (`python --version`, `py --version` hoặc `python3 --version`): Python 3.14.5
- Git version: git version 2.51.0.windows.1
- Terminal (PowerShell/cmd/macOS/Linux): C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe
- Python interpreter path (quan sát từ `import sys; print(sys.executable)`):
- Branch học tập / commit SHA:

| Hoạt động | Lệnh đã chạy | Output mong đợi | Output thực tế |
|---|---|---|---|
| REPL: `2 + 3` | | `5` | |
| Bài `ex01_hello.py` | python weeks/week-01-hello-python/exercises/ex01_hello.py | lời chào + khung + sở thích | |
| Bài `ex02_calculator.py` | python weeks/week-01-hello-python/exercises/ex02_calculator.py | phép tính đúng | 3024, 45000, 153.94, 14, 2 |
| Mini-project cơ bản | python weeks/week-01-hello-python/mini-project/starter_basic.py | khung có chữ Xin Chào! ở giữa và thẳng hàng | |

- Một lỗi đã gặp/thử tạo có chủ ý: W01.MESSAGE vẫn báo RETRY dù làm đúng
- Dòng/loại lỗi: Có thể do mã hóa dấu tiếng việt
- Cách sửa và kết quả sau khi chạy lại: 
+ Thêm dòng lệnh: 
import sys
sys.stdout.reconfigure(encoding="utf-8")
+ Kết quả: Ghi trạng thái PASS thực tế sau khi kiểm tra lại
- Điều còn chưa làm hoặc hạn chế:
- AI hỗ trợ gì (nếu có) và em xác minh bằng cách nào?
+ ChatGPT đã giúp giải thích cú pháp Python, cách sử dụng round(), cách đọc AutoGrade, phân tích lỗi và đề xuất phương án khắc phục. Tự chỉnh sửa, chạy chương trình và đối chiếu kết quả.
## Tự chấm AutoGrade Week 01 (chỉ 5 điểm thực hành)

Xem [hướng dẫn cho sinh viên](assessment/STUDENT-GUIDE.md) và **chạy đúng mã của em**, không lấy kết quả `--mode reference`.

```bash
python -m assessment grade --week 01 --acknowledge-local-code
```

- Chế độ hiển thị: STUDENT
- Điểm máy sau lần kiểm cuối: 5.00 / 5.00
- Số tiêu chí PASS: 11 / 11
- Mã tiêu chí RETRY cần cải thiện (nếu có): Không có
- Tệp đã sửa để khắc phục RETRY:
- Bằng chứng trước và sau khi sửa (lệnh, stdout, lỗi thực tế):
- Nếu đã xuất `.learner-output/week01.json`, tên báo cáo cục bộ: .learner-output/week01.json
- Giải thích của em vì sao kết quả đúng (không chỉ ghi PASS):

**Tự đối chiếu 5 điểm chờ giảng viên duyệt:** môi trường/Terminal/REPL (2), lỗi và cách sửa (1), Git commit/hướng dẫn chạy/evidence (2). Em có thể ghi mức tự đánh giá nhưng không tự gán điểm chính thức.

**Không đưa mật khẩu, token, bài của người khác hoặc dữ liệu nhạy cảm vào
minh chứng.** Chỉ đánh dấu hoàn thành khi đã thực sự chạy bài mình viết.
