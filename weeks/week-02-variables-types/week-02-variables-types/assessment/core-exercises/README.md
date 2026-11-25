# Tự chấm Week 02 — bám ba bài tập gốc, không tạo đề mới

> **BẮT ĐẦU DÀNH CHO SINH VIÊN:** Đọc [START-HERE.md](START-HERE.md), hoàn thành ba file `exercises/` gốc rồi chạy một lệnh để có [báo cáo HTML hành trình](student_journey.py) **ngoại tuyến**:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/student_journey.py --student
```

File kết quả: `.learner-output/week02-journey.html` (mở bằng trình duyệt). Hiện ba chặng, mức tiến bộ và gợi ý 1–3 theo từng TODO chưa đạt. Không cần cài thư viện ngoài hoặc tải bài lên Internet. Lệnh `autograde_w02.py --student` bên dưới **vẫn hoạt động** cho người muốn xem kết quả terminal/JSON.


Bộ chấm này dùng **đúng các TODO đã có** trong:
- [Bài 01 — Biến](../../exercises/ex01_variables.py)
- [Bài 02 — Chuyển kiểu](../../exercises/ex02_type_conversion.py)
- [Bài 03 — Input và máy tính](../../exercises/ex03_input_calc.py)

Không tạo lại cấu trúc 5 câu × 10 ý. Rubric phân bổ 10 **điểm tự luyện** cho các TODO bắt buộc của **ba bài gốc**; phần thử thách ghi trong file là tùy chọn. [Mini-project thẻ sinh viên](../../mini-project/README.md) đã có mã chạy sẵn nên chỉ xem như minh chứng/demo, **không cộng điểm tự động từ starter có sẵn**.

## Nội dung và điểm

| Bài gốc | Nội dung thực tế từ TODO | Điểm |
|---|---|---:|
| `ex01_variables.py` | 4 biến + `type()`; hoán đổi hai biến; bốn phép gán tăng cường | 3,0 |
| `ex02_type_conversion.py` | chuỗi "42" → int + 8; `int(pi)`; 6 giá trị bool; BMI từ input | 3,5 |
| `ex03_input_calc.py` | tổng/hiệu/tích/thương; diện tích/chu vi hình tròn; giá sau giảm | 3,5 |
| **Tổng** | **Bám nguyên đề và thứ tự TODO** | **10,0** |

Máy đọc mã AST và chạy các file sinh viên với input mẫu khác nhau; các tiêu chí có thể cần người dạy xem xét khi cách viết hoặc trình bày khác mẫu. **Điểm tự động không phải điểm chính thức**.

## Tự chấm bằng bộ test tách riêng

Hệ thống nay chia tách đúng như thư mục Drive mẫu: **`grader.py`** là cửa vào chấm; **[`tests/`](tests/README.md)** là tập test độc lập từng bài gồm 3 file JSON (24 bộ input động, cộng kiểm tra AST/runtime cho 6 TODO không nhận stdin) và 3 file `test_ex*.py`; **[`reports/`](reports/README.md)** lưu HTML/JSON cục bộ, được Git bỏ qua.

```bash
# Sinh viên chấm đúng ba file bài tập gốc; không cần cài pytest
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student

# Agent/giảng viên KIỂM TRA TÍNH TOÀN VẸN CỦA TOÀN BỘ TEST, không thực thi code sinh viên
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --audit-tests

# Maintainer: chạy 3 bộ kiểm từng bài và kiểm toán đầy đủ (yêu cầu pytest)
python -m pytest -q weeks/week-02-variables-types/assessment/core-exercises/tests/
```

Kết quả sinh viên: `reports/week02-journey.html` và `reports/week02-result.json`. Đọc [prompt Antigravity/Codex kiểm toán toàn bộ tập test](AGENT-ASSESSMENT-PROMPT.md) trước khi chấm bài được gửi từ ngoài. **Chỉ chạy mã tin cậy tại máy cá nhân**; không có sandbox. Các lệnh `student_journey.py --student` và `autograde_w02.py --student` cũ vẫn hoạt động.

## Cách dùng — từ gốc `python-journey`

```bash
# Chấm ba file BÀI GỐC sinh viên tự sửa
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student

# Xem chi tiết mỗi tiêu chí
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student --verbose

# Báo cáo máy đọc, chỉ lưu cục bộ
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student --json-out .learner-output/week02-core.json

# Kiểm máy chấm bằng bộ code fixture riêng, KHÔNG phải bài sinh viên
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --reference
```

Đọc [Hướng dẫn sinh viên](STUDENT-GUIDE.md), [mẫu minh chứng](EVIDENCE-TEMPLATE.md), [gợi ý](HINTS.md) và [hướng dẫn giảng viên](TEACHER-GUIDE.md).

### Giới hạn bắt buộc

- **Không sửa đề** trong `exercises/`, không thêm cách nộp riêng hoặc đặt tên hàm mới. Student mode đọc thẳng file gốc.
- Để kiểm đầy đủ bài 02, máy thử stdin **chiều cao, cân nặng** rồi (nếu có) số giây thử thách; bài 03 thử stdin theo thứ tự **2 số, bán kính, giá, % giảm** rồi (nếu có) VND và tỷ giá. Nếu bài làm nhập thứ tự khác hoặc xuất định dạng khác nhưng đúng về toán, **đánh giá thủ công**.
- Rubric công khai, điểm sơ bộ: không xác định tác giả/chống gian lận, không thay `checks/check_solutions.py` là bộ kiểm bài mẫu.
- Subprocess/timeout/`python -I` **không phải sandbox**. Chỉ chạy mã bạn tự viết hoặc tin cậy trên máy cá nhân; không chạy bài nộp người lạ trên máy giảng viên, CI có secrets hay production.
