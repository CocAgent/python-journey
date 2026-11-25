# Bài làm Week 02 — buivannam

Bài làm ba file `exercises/` Tuần 02 được tách vào đây để giảng viên phản biện, **không ghi đè TODO gốc**
trong [`exercises/`](../../exercises/). Đây không phải đáp án chuẩn hay điểm chính thức. Xem
[quy tắc thư mục bài nộp](../README.md).

## Tệp bài làm

| Tệp | Git blob SHA | Nội dung |
|---|---|---|
| [`ex01_variables.py`](exercises/ex01_variables.py) | `c86084b19707fbb9c376026bda9e7ab4f1d468bf` | TODO 1–3 và thử thách TODO 4 |
| [`ex02_type_conversion.py`](exercises/ex02_type_conversion.py) | `e35039624373065f8a097838a756fd0f7433dddb` | TODO 1–4 và thử thách TODO 5 |
| [`ex03_input_calc.py`](exercises/ex03_input_calc.py) | `fbf6f2a54c750f89f5285d738118f26aa1c283e9` | TODO 1–3 và thử thách TODO 4 |

Các dòng `# TODO N` được giữ nguyên để bộ chấm tách đúng từng phần. Thứ tự nhập theo đề: bài 02 nhập chiều
cao, cân nặng rồi số giây; bài 03 nhập 2 số, bán kính, giá gốc, % giảm, rồi số tiền VNĐ và tỷ giá.

## Kết quả tự kiểm tại máy sinh viên

- `autograde_w02.py --student`: **10.00/10 điểm tự luyện** (10/10 TODO bắt buộc PASS). Thử thách không tính điểm.
- `practice/checks/check_practice.py --starter`: 3/3 PASS trên bản làm tại máy; bài practice không đưa vào thư mục này.
- Trên Windows, bộ chấm cần stdout UTF-8 (ví dụ bật tùy chọn UTF-8 của Windows); nếu không, chữ tiếng Việt
  trong `print()` gây `UnicodeEncodeError` và bị chấm RETRY dù code đúng.

`official_score=null`. Giảng viên có thể dán ba tệp vào
[`TODO-GRADING.html`](../../assessment/core-exercises/TODO-GRADING.html) để chấm lại từng TODO.
