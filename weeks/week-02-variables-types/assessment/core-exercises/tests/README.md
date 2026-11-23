# Tập test độc lập cho ba bài tập gốc — Week 02

Đây là **bộ test công khai, chỉ phục vụ tự luyện**. Ba file JSON là **nguồn dữ liệu test** cho `autograde_w02.py`; ba file `test_ex*.py` kiểm tra độc lập độ chính xác của cả grader lẫn từng bài. Không tạo đề mới, không chạy `practice/` hay mini-project.

| Bài tập gốc | Tập dữ liệu | Test kiểm chứng | Tiêu chí | Bộ input động |
|---|---|---|---:|---:|
| `ex01_variables.py` | `cases_ex01_variables.json` | `test_ex01_variables.py` | 3 | 0 (kiểm biến/AST) |
| `ex02_type_conversion.py` | `cases_ex02_type_conversion.json` | `test_ex02_type_conversion.py` | 4 | 6 (BMI) |
| `ex03_input_calc.py` | `cases_ex03_input_calc.json` | `test_ex03_input_calc.py` | 3 | 18 (4 phép tính, hình tròn, giảm giá) |
| **Tổng** | **3 file JSON** | **3 file pytest** | **10** | **24** |

Các TODO không có stdin cũng có **kiểm tra AST/runtime riêng**, được mô tả trong từng file Python và `rubric.json`. Vì vậy 24 là **số bộ input động**, không phải tổng số kiểm tra.

## Dành cho sinh viên (không cần pytest)

Đứng tại gốc repository:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student
```

Kết quả lưu trong `assessment/core-exercises/reports/` theo hai định dạng HTML/JSON và không được commit. Lệnh legacy `student_journey.py --student` vẫn hoạt động.

## Dành cho Codex/Antigravity và maintainer

```bash
# Kiểm toán ĐẦY ĐỦ rubric ↔ 3 tập dữ liệu, không thực thi mã học viên
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --audit-tests

# Chạy đủ 3 file test độc lập (yêu cầu pytest trong môi trường bảo trì)
python -m pytest -q weeks/week-02-variables-types/assessment/core-exercises/tests/

# Kiểm regression toàn bộ giáo trình
python -m pytest -q tests/
```

Nghiệm thu đủ: 3 exercises → 10 TODO → 10 điểm, 24 input động, fixture giảng viên 10/10, starter 0/10, sai/đáp án cứng không đạt sai, lời giải hợp lệ dạng khác có cơ chế REVIEW, không sửa file bài gốc. Không suy ra điểm học phần; `official_score=null`.

**Giới hạn an toàn:** Chỉ chạy test CI trên **fixture maintainer tin cậy**, không import hoặc chạy bài nộp bên ngoài. Subprocess, timeout, `python -I` không phải sandbox; phải có runner cô lập trước khi tổ chức chấm tập trung.
