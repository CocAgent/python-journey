# Hướng dẫn giảng viên — chấm tự luyện **exercises/ Week 02**

## Nguồn đề và phạm vi duy nhất

Không dùng đề mới 5 câu / 10 ý. Bộ chấm dựa vào chính ba file gốc:
- `exercises/ex01_variables.py`: TODO 1–3; TODO 4 **Thử thách**, không chấm.
- `exercises/ex02_type_conversion.py`: TODO 1–4; TODO 5 **Thử thách**, không chấm.
- `exercises/ex03_input_calc.py`: TODO 1–3; TODO 4 **Thử thách**, không chấm.

**Không** đọc hay tính điểm các file `practice/`, `mini-project/`, `solutions/` hoặc checker reference của giáo trình. Bản mini-project `starter.py` có mã sẵn nên PASS không được coi là thành tích cá nhân.

## Rubric 10 điểm *tự luyện* (công khai)

| File gốc | Tiêu chí bắt buộc | Điểm |
|---|---|---:|
| ex01 | Bốn biến và type(), hoán đổi, augmented assignment | 3,00 |
| ex02 | Chuyển "42", int(pi), sáu bool(), BMI từ input | 3,50 |
| ex03 | Bốn phép tính, diện tích/chu vi, giảm giá | 3,50 |
| **Tổng** | **3 + 4 + 3 TODO có sẵn** | **10,00** |

Các TODO được nhận diện bằng dòng `# TODO N` **vốn đã có**. Không thay thế tên hàm, không chuyển chương trình thành kiểu return như đề mock-exam (vì học viên đang ở Week 02). Các phần bắt buộc trong từng TODO được chạy riêng với stdin mẫu; điểm phần nhập số đánh giá bằng hai bộ giá trị, hỗ trợ điểm một phần. Phần kiểm AST giúp kiểm `type()`, `int()`, phép toán và thao tác gán. Điểm trên máy chỉ là **ước lượng công khai**, có thể nhận nhầm hoặc không nhận diện được cách viết đúng; giảng viên phải phản biện khi có khiếu nại.

## Phiếu chấm HTML theo TODO

Mở [`TODO-GRADING.html`](TODO-GRADING.html) bằng trình duyệt. Trang có 5 tab:

- **00 · Tự động chấm:** dán hoặc chọn 3 file `exercises/` rồi bấm chấm. Trang chạy bản chuyển của
  `check_one()`/`grade()` trong `autograde_w02.py` bằng Python 3 trong trình duyệt (Pyodide, cần Internet lần
  đầu để tải). Rubric và 24 bộ input được nhúng từ `rubric.json` và `tests/cases_*.json`; nếu sửa các file này,
  cần nhúng lại. Mã chạy trong WebAssembly của trình duyệt, không đọc được file trên máy. Có thể nạp
  `reports/week02-result.json` thay cho việc chấm trong trình duyệt. Nút **▶ Chạy cả file** chạy từng file
  như `python <file>` với dữ liệu `input()` tự nhập và hiện màn hình Terminal, kể cả traceback.
- **01–03:** mỗi TODO có kết quả máy (PASS/RETRY/REVIEW), code của TODO đó, bảng từng bộ input và output,
  checklist, ô điểm giảng viên và ghi chú. TODO thử thách được chạy thử với một input mẫu nhưng không tính điểm.
- **04 · Tổng kết:** bảng điểm máy và điểm giảng viên, nhận xét chung, xuất JSON hoặc in PDF.

Điểm máy có thể tự điền vào ô điểm giảng viên làm điểm khởi đầu; giảng viên phải rà lại trước khi chốt.

## Hành trình sinh viên và quy trình phản biện

`student_journey.py --student` chạy cùng rubric `grade()`, sinh báo cáo HTML tự chứa ở `.learner-output/week02-journey.html`. Trang có ba chặng, chỉ số TODO, điểm /10 và ba gợi ý mở dần cho TODO cần sửa. Mọi gợi ý chỉ phục vụ tự học, **không làm thay đổi điểm**. Báo cáo không đưa stdout, biến cá nhân hoặc mã bài vào HTML/JSON.

Với mã thay thế đúng nhưng checker không chấp nhận, giảng viên xem code và output thủ công. **Không lấy kết quả AutoGrade làm điểm cuối kỳ**. Không tự chạy bài học viên chưa tin cậy trên VPS, GitHub Actions có secrets hoặc máy tính giảng viên; phải có sandbox đúng nghĩa nếu tổ chức chấm tập trung.

## Kiểm toán toàn bộ tập test tách riêng

- Dữ liệu nguồn: [`tests/cases_ex01_variables.json`](tests/cases_ex01_variables.json), [`tests/cases_ex02_type_conversion.json`](tests/cases_ex02_type_conversion.json), [`tests/cases_ex03_input_calc.json`](tests/cases_ex03_input_calc.json); 10 tiêu chí, 24 bộ stdin.
- Kiểm thử độc lập: `tests/test_ex01_variables.py`, `tests/test_ex02_type_conversion.py`, `tests/test_ex03_input_calc.py`; kiểm toán tổng: `tests/test_complete_test_suite.py`.
- Chạy `grader.py --audit-tests` trước (chỉ xác thực metadata/rubric, không chạy bài); chạy `python -m pytest -q weeks/week-02-variables-types/assessment/core-exercises/tests/` trong môi trường bảo trì (chỉ fixture mã tin cậy), rồi chạy regression toàn repository.
- Sau khi test suite PASS, nếu đã xác nhận bài sinh viên **thực sự tin cậy**, chạy `grader.py --student --submission "[STUDENT_DIR]" --acknowledge-local-code`. Nếu mã nộp chưa tin cậy, **BLOCKED_EXECUTION** cho đến khi có sandbox thực sự.
- Phải xem kết quả theo 10 TODO, trường hợp sai/đúng/giá trị biên, lỗi nhận diện false positive/false negative; không đánh đồng việc bộ test PASS với việc sinh viên đạt điểm chính thức.
- [Prompt đầy đủ cho Codex/Antigravity](AGENT-ASSESSMENT-PROMPT.md) mô tả kiểm toán **cả tập test** trước khi chấm.

## Kiểm chuẩn

```bash
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --reference
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student
```

`--reference` chấm **fixtures/reference/** tin cậy, dự kiến 10/10. File exercises ở `main` chưa làm, dự kiến 0/10; đây chỉ là trạng thái trước khi học. **Không đưa mã sinh viên chưa tin cậy vào CI hoặc chạy trên máy có secrets.** Maintainer CI chỉ chạy fixture giáo viên/blank tạm, không chạy bài thu thập từ học viên.

## Giới hạn kiểm chứng

- Bộ chấm chia theo TODO và yêu cầu **giữ lại các dòng `# TODO N`** để xác định đúng đoạn mã. Sinh viên thay tên hoặc chuyển tất cả mã sang nơi khác có thể gây RETRY dù đúng; cần chấm thủ công.
- Bài 02 TODO 4 tự kiểm thứ tự nhập chiều cao trước, cân nặng sau. Bài 03 TODO 1–3 nhận dữ liệu theo thứ tự các TODO tương ứng. Đầu ra có thể in kèm nhãn, checker tìm số chứ không bắt định dạng máy cứng.
- `ex01` TODO3 không có con số tăng/giảm trong đề; checker chỉ kiểm các toán tử + thao tác in, không tự tạo đáp số duy nhất.
- `official_score` trong báo cáo JSON luôn `null`. Không tự đưa 10 điểm này vào điểm cuối kỳ.
- Subprocess, timeout và cwd tạm **không phải sandbox**, không cô lập quyền đọc tệp/network hoặc chống mã độc. Chỉ dùng mã đã tin cậy, không chạy trên VPS production hoặc CI có secrets.

## Human gate trước merge

Cần CI Python 3.12/3.14 PASS, verify_course PASS, pytest + Ruff PASS. Giữ Draft PR để rà soát độc lập độ bao phủ các TODO, sau đó mới quyết định merge. Không chỉnh sửa bài tập gốc khi thử bộ chấm.
