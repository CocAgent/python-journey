# Python Journey — Cổng tự kiểm sinh viên Week 01–15

> Đây là hướng dẫn tự luyện tại máy cá nhân, **không** phải nền tảng chấm bài tập trung. Mã sinh viên chỉ được chạy trên máy của chính em hoặc môi trường sandbox thật được giảng viên quản lý.

## Hướng dẫn bắt đầu

Tải toàn bộ [Python Journey](https://github.com/CocAgent/python-journey), mở thư mục gốc trong VS Code, kiểm tra `python --version` (>=3.12). Nếu chưa quen terminal, đọc [hướng dẫn Week 01](../weeks/week-01-hello-python/assessment/STUDENT-GUIDE.md). Với các tuần cần `pytest`, làm theo [SETUP.md](../SETUP.md).

**Xem hướng dẫn của một tuần mà không chạy code sinh viên:**

```bash
python -m assessment guide --week 02
```

**Week 01 chấm 11 tiêu chí với tối đa 5 điểm máy:**

```bash
python -m assessment grade --week 01 --acknowledge-local-code
```

**Week 02–08, 10–14 có checker bài sinh viên; không quy đổi thành điểm:**

```bash
python -m assessment selfcheck --week 02 --acknowledge-local-code
python -m assessment selfcheck --week 02 --acknowledge-local-code --json-out .learner-output/week02.json
```

**Week 09** dùng rubric dự án và giảng viên duyệt; **Week 15** chỉ có checker readiness cơ học cần `--project` trỏ đúng thư mục capstone.

## Chọn đúng tuần và đúng checker

| Tuần | Nội dung | Lệnh AutoGrade | Phạm vi máy kiểm |
|---|---|---|---|
| [01](../weeks/week-01-hello-python/assessment/STUDENT-GUIDE.md) | Hello Python | `grade --week 01` | 11 tiêu chí, 5 điểm tự động |
| [02](../weeks/week-02-variables-types/assessment/STUDENT-GUIDE.md) | Biến và kiểu | `selfcheck --week 02` | Practice starter |
| [03](../weeks/week-03-conditionals/assessment/STUDENT-GUIDE.md) | Điều kiện | `selfcheck --week 03` | Practice starter |
| [04](../weeks/week-04-strings/assessment/STUDENT-GUIDE.md) | Chuỗi | `selfcheck --week 04` | Practice starter |
| [05](../weeks/week-05-lists-tuples/assessment/STUDENT-GUIDE.md) | List và tuple | `selfcheck --week 05` | Practice starter |
| [06](../weeks/week-06-loops/assessment/STUDENT-GUIDE.md) | Vòng lặp | `selfcheck --week 06` | Practice starter |
| [07](../weeks/week-07-functions/assessment/STUDENT-GUIDE.md) | Hàm | `selfcheck --week 07` | Practice starter |
| [08](../weeks/week-08-dicts-sets/assessment/STUDENT-GUIDE.md) | Dict và set | `selfcheck --week 08` | Practice starter |
| [09](../weeks/week-09-midterm-project/assessment/STUDENT-GUIDE.md) | Dự án giữa kỳ | `guide --week 09` | Rubric + demo, không có checker chung |
| [10](../weeks/week-10-files-io/assessment/STUDENT-GUIDE.md) | Files/CSV/JSON | `selfcheck --week 10` | Practice starter |
| [11](../weeks/week-11-exceptions/assessment/STUDENT-GUIDE.md) | Ngoại lệ | `selfcheck --week 11` | Practice starter |
| [12](../weeks/week-12-testing-pytest/assessment/STUDENT-GUIDE.md) | Kiểm thử với pytest | `selfcheck --week 12` | Bốn test học viên + mutation |
| [13](../weeks/week-13-modules-cli-api/assessment/STUDENT-GUIDE.md) | Module, CLI, API giả lập | `selfcheck --week 13` | Bốn lab starter |
| [14](../weeks/week-14-oop-essentials/assessment/STUDENT-GUIDE.md) | OOP | `selfcheck --week 14` | Bốn bài exercises |
| [15](../weeks/week-15-capstone-project/assessment/STUDENT-GUIDE.md) | Capstone | `selfcheck --week 15 --project ...` | Readiness, không chấm điểm |

## Phân biệt các loại kết quả

- **Bài sinh viên:** `--starter`, `check_student.py`, `check_student_tests.py` hoặc `selfcheck` gọi trực tiếp checker sinh viên hiện có. PASS chỉ cho biết phần kiểm đã đạt.
- **Bài giáo trình:** `--solutions`, `check_solutions.py`, `check_week.py` hay CI reference PASS không chứng minh em làm xong.
- **Điểm:** Week 01 tự chấm 5 điểm máy + 5 điểm giảng viên. Week 02–15 chưa có điểm số AutoGrade thống nhất; kết quả JSON trả `auto_score: null`, `official_score: null`, riêng Week 09 không có máy tự kiểm chung.
- **Phạm vi:** các lab `practice/starter/` nhiều tuần là **bổ sung**, không thay bài `exercises/` gốc hay mini-project. Week 12/14 có checker sinh viên trực tiếp bài exercises; Week 15 chỉ readiness, không thay yêu cầu của `FINAL_PROJECT.md`.
- **An toàn:** checker có thể import/chạy code sinh viên; timeout/subprocess không phải sandbox. Không tự động chạy bài nộp chưa tin cậy trên CI có secrets hay server production.

## Ghi minh chứng

Dùng [mẫu minh chứng chung](EVIDENCE-TEMPLATE.md) để ghi input, output thực tế, lỗi và cách sửa, tên checker, phạm vi chưa kiểm, câu trả lời tự giải thích và Git commit. Week 09/15 có mẫu riêng tại tuần. Nếu bài làm đúng nhưng checker FAIL, ghi lại input + code + expected/actual và nhờ giảng viên phản biện; không sửa checker để đạt giả.
