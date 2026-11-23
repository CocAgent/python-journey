# Ví dụ xử lý PR #251 — giữ đúng bài làm Week 02, không làm hỏng giáo trình

**Nguồn công khai:** [PR #251 — Thanh Quý Weeks 2](https://github.com/CocAgent/python-journey/pull/251), fork `thanhquycoder/python-journey`, head SHA `929ab0c31ba4f66ea85551aa6639cb81f803992b`.

## Điều được chọn để làm mẫu tích hợp

Chỉ sao chép **nguyên ba file Week 02** nằm trong `exercises/` của fork vào **`submissions/pr-251/exercises/`**:

| Tệp sinh viên | Git blob SHA trong PR gốc |
|---|---|
| `ex01_variables.py` | `bd360047cfcfd7b85834c9dd597db5e14b981850` |
| `ex02_type_conversion.py` | `41b184b7b3dd78db381e6ba46caaccc0c5fc5f42` |
| `ex03_input_calc.py` | `916b1f50137dfd4295d7caa8bb37843b6c01f988` |

Các file trong thư mục này được kiểm tra **SHA blob trùng tuyệt đối** với file nguồn tại head PR. Bản gốc của `weeks/week-02-variables-types/exercises/` trên `main` được giữ nguyên để sinh viên khác còn TODO chưa giải.

## Những nội dung KHÔNG được nhập từ PR #251

PR gốc thay đổi **635 file** (603 xóa, 14 sửa, 18 thêm) và có xung đột trên nhánh chính. Không nhập:

- Hàng trăm file giáo trình bị xóa, `README.md`/chương trình học ở root.
- Các file Week 01; lời giải ghi đè `exercises/` chung Week 02, `practice/starter/`, `mini-project/starter.py`.
- Các bản sao cũ/đã lạc hậu của `assessment/core-exercises/`, `rubric.json`, `grader.py`, `tests/` đã có trong `main`.
- File sinh `__pycache__/*.pyc`, các `html/*.json` / `html/*.html` là kết quả từ máy sinh viên, và `index.html` trỏ đến trang riêng.
 
## Cách đánh giá đúng phạm vi (không dùng làm lời giải chuẩn)

Bước **audit test suite** (không chạy bất kỳ bài sinh viên nào):

```bash
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --audit-tests
```

Nếu và chỉ nếu có môi trường **cách ly thực sự**, hoặc mã đã được kiểm tra và tin cậy tại máy cá nhân, người phản biện có thể thực hiện:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student --submission weeks/week-02-variables-types/submissions/pr-251 --acknowledge-local-code
```

Lệnh trên thực thi code được chỉ định; `subprocess` của grader **không phải sandbox**. **Không chạy mã PR chưa tin cậy trên GitHub Actions, production VPS hoặc máy có bí mật**. Báo cáo HTML/JSON chỉ tạo ở local và không phải điểm học phần.

Trạng thái bản mẫu: **chỉ kiểm tra cấu trúc, đối chiếu SHA và cách đặt đúng vị trí; chưa thực thi để chấm điểm**. `official_score=null`; các TODO thử thách không cộng điểm.

Đây là **ví dụ tích hợp có kiểm soát**, không phải PR #251 đã được merge và cũng không phải phán quyết sư phạm về khả năng của tác giả.
