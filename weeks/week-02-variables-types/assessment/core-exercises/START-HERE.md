# Bắt đầu tại đây — Hành trình Python Week 02 🎒

**Dành cho sinh viên mới học:** đây là phần **tự luyện** trên máy cá nhân, không cần tài khoản, Internet hay cài thêm thư viện Python. Em chỉ sửa **ba bài tập gốc**, không cần tạo đề thi mới.

## 1. Tải giáo trình và mở đúng thư mục

1. Mở [CocAgent/python-journey](https://github.com/CocAgent/python-journey).
2. Chọn **Code → Download ZIP** (hoặc `git clone`). Giải nén toàn bộ ZIP.
3. Mở **thư mục gốc `python-journey`** bằng VS Code (File → Open Folder).
4. Vào **Terminal → New Terminal**; chạy `python --version` để kiểm tra **Python 3.12+**. Trên Windows nếu `python` không có, thử `py --version` và dùng `py` trong lệnh bên dưới.

> Nếu đang dùng bản thử nghiệm trong Draft PR, mở nhánh tương ứng trên GitHub rồi chọn **Code → Download ZIP** ở chính nhánh đó; bản main có thể chưa có nâng cấp mới.

## 2. Hoàn thành ba bài tập có sẵn

Trong `weeks/week-02-variables-types/exercises/`, sửa các TODO bắt buộc:

- **Chặng 01 — Chiếc ba lô biến:** `ex01_variables.py` — TODO 1–3.
- **Chặng 02 — Phép thuật chuyển kiểu:** `ex02_type_conversion.py` — TODO 1–4.
- **Chặng 03 — Xưởng máy tính mini:** `ex03_input_calc.py` — TODO 1–3.

Em nên đọc [notes](../../notes.md), chạy ví dụ và tự thử từng bài trước. **Giữ nguyên dòng `# TODO 1`, `# TODO 2`, ...** để máy nhận diện các đoạn cần chấm. Các TODO ghi **Thử thách** được tự chọn, không trừ điểm. Không sửa máy chấm, rubric hoặc file fixture.

## 3. Chạy một lệnh để nhận phản hồi

**Cách mới — dùng bộ test tách riêng** (khuyến nghị):

```bash
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student
```

Kết quả ở `weeks/week-02-variables-types/assessment/core-exercises/reports/week02-journey.html` và `week02-result.json`. Đây là kết quả **tự luyện**; các file sinh ra không được commit.

Nếu giáo trình đang dùng lệnh `student_journey.py --student`, lệnh cũ ở dưới vẫn hợp lệ; chỉ khác nơi lưu HTML. **Không cần pytest** khi chỉ tự luyện.

Mở Terminal tại **thư mục gốc `python-journey`**, chạy:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/student_journey.py --student
```

Windows có thể dùng:

```powershell
py weeks/week-02-variables-types/assessment/core-exercises/student_journey.py --student
```

Máy sẽ báo chặng nào đạt, TODO nào cần thử lại, và ghi file:

`.learner-output/week02-journey.html` (không tính khoảng trắng bên ngoài).

**Mở `.learner-output/week02-journey.html` bằng Chrome, Edge hoặc Firefox.**
Đọc từng chặng và bấm **Gợi ý mức 1 → 2 → 3** chỉ khi cần. Sửa code của mình rồi chạy lại cùng lệnh để cập nhật báo cáo.

Nếu Terminal trả **exit code 1**, thông thường chỉ có nghĩa còn TODO chưa đạt; vẫn mở báo cáo HTML bình thường. Không cần cài `pytest` để tự luyện.

## 4. Hiểu đúng điểm và tự bảo vệ dữ liệu

- **Điểm /10 chỉ là điểm tự luyện**, không phải điểm cuối kỳ. Bảng có 10 TODO bắt buộc (3+4+3), phân bổ **3 / 3,5 / 3,5 điểm** theo ba bài; không cộng hai lần `practice/` hay `mini-project/`.
- Báo cáo HTML/JSON lưu **trên máy cá nhân**, không có chức năng gửi dữ liệu qua Internet và không đưa mã nguồn hay output cá nhân vào báo cáo. **Không đăng công khai báo cáo, mã bài hoặc tên riêng trong bài** khi chưa kiểm tra.
- Nếu cách giải đúng nhưng máy không nhận diện, ghi lại mã, input/output và nhờ giảng viên xem. Đừng đổi đáp án để qua test giả.
- Máy chấm **chạy mã Python của chính em**, subprocess không phải sandbox. Chỉ dùng code do em viết hoặc nguồn em thật sự tin cậy; không tải bài của người khác để chạy trên máy chứa dữ liệu quan trọng.
- **Không cần** chạy `--reference`: đó là chế độ kiểm bộ mẫu **của người bảo trì**, không phải bài của sinh viên.

## 5. Tự ghi nhận một điều mới học được

Sau khi chạy và sửa bài, ghi lại:
1. Một lỗi em đã gặp, lý do và cách em sửa.
2. Một dữ liệu đầu vào khác ví dụ mà bài của em vẫn tính đúng.
3. Em đã tự giải thích được sự khác biệt giữa `str`, `int`, `float` và `bool` chưa?

Dùng [phiếu minh chứng](EVIDENCE-TEMPLATE.md) nếu giảng viên yêu cầu nộp.

**Quan trọng:** `python -m assessment selfcheck --week 02` là **bộ kiểm lab practice riêng**, không phải lệnh tự chấm ba bài `exercises/` ở trang này.
