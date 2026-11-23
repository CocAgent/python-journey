# Tuần 02 — Variables · Types · Input/Output

> **Sinh viên:** [Hướng dẫn tự kiểm, đọc PASS/RETRY, lưu minh chứng Week 02](assessment/STUDENT-GUIDE.md). Checker chỉ kiểm đúng phạm vi bài sinh viên (nhiều tuần là practice/starter); không tự chuyển PASS thành điểm học phần. Xem thêm [cổng tự kiểm toàn khóa](../../assessment/STUDENT-PORTAL.md).

Tuần này bạn đặt tên cho dữ liệu, nhận input dạng text, chuyển kiểu có chủ đích
và tạo output rõ bằng f-string.

## Ví dụ bài nộp sinh viên được tách đúng vị trí

[**Mẫu tích hợp có kiểm soát từ PR #251**](submissions/pr-251/README.md): lưu ba file bài làm nguyên gốc trong `submissions/pr-251/exercises/`, **không ghi đè các TODO giáo trình**, không chạy bài chưa tin cậy trong CI, và không coi đó là đáp án chuẩn. [Quy tắc thư mục bài nộp](submissions/README.md).

## Bộ chấm Week 02 với test tách riêng

**Sinh viên (chỉ cần Python):**

```bash
python weeks/week-02-variables-types/assessment/core-exercises/grader.py --student
```

Báo cáo HTML/JSON trong `assessment/core-exercises/reports/`. Nguồn test được tổ chức trong [`assessment/core-exercises/tests/`](assessment/core-exercises/tests/README.md), nhưng sinh viên không cần cài `pytest`. [Hướng dẫn tải và thực hành](assessment/core-exercises/START-HERE.md).

## Bắt đầu hành trình tự luyện Week 02

**[Tải và tự học theo hướng dẫn 5 bước](assessment/core-exercises/START-HERE.md)**. Hoàn thành 3 file `exercises/` gốc, rồi chạy:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/student_journey.py --student
```

Mở báo cáo `.learner-output/week02-journey.html` trong trình duyệt để thấy ba chặng, tiến độ và gợi ý từ dễ đến cụ thể. Mọi đánh giá là **điểm tự luyện /10**, không phải điểm chính thức.

## Chấm tự động đúng **ba bài tập gốc trong exercises/**

**[Mở bộ chấm Week 02 theo TODO có sẵn](assessment/core-exercises/README.md)** — 3 file gốc, 10 TODO bắt buộc, tối đa 10 điểm **tự luyện**. Các mục `(Thử thách)`, `practice/` và `mini-project/` **không tính vào điểm bộ này**.

```bash
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student
```

Bộ tự kiểm `python -m assessment selfcheck --week 02` ở phần hướng dẫn khác **chỉ chạy lab `practice/starter/`**, không tính điểm này. Điểm tự luyện không thay rubric và đánh giá của giảng viên.

## Outcomes

- dùng biến với tên `snake_case`;
- phân biệt `int`, `float`, `str`, `bool` và quan sát bằng `type()`;
- hiểu `input()` luôn trả `str`;
- dùng explicit conversion trước khi tính toán;
- biết conversion có thể fail với text không phù hợp;
- tách input → processing → output ở mức đơn giản.

## Learning path

Story mở đầu tùy chọn: [Cóc và Dế mở chiếc ba lô Python](../../assets/Story-02-Biến%20và%20chuỗi.md).

```text
README → notes → examples → exercises → hints
       → machine check → mini-project → evidence
```

1. Đọc [`notes.md`](notes.md).
2. Chạy các file trong [`examples/`](examples/).
3. Làm ba bài trong [`exercises/`](exercises/).
4. Chỉ mở [`hints.md`](hints.md) sau khi tự thử.
5. Xem [ví dụ dự đoán và giải thích lỗi](WORKED-EXAMPLES.md), rồi tự làm [bài tương tự](practice/README.md).
6. Chạy [official solution check](checks/README.md).
7. Hoàn thành [Thẻ sinh viên](mini-project/README.md).

## Dự đoán trước khi chạy — 3 ví dụ có giải thích

Mở [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md) để học theo vòng:
**Dự đoán → Chạy → So sánh → Giải thích lỗi → Thay input → Tự làm bài tương tự**.

| Ví dụ mới | Nội dung quan sát | Câu hỏi |
|---|---|---|
| `04_predict_types.py` | `"12" + "3"` khác `12 + 3`; `bool("False")` | Vì sao một kết quả là 123, một kết quả là 15? |
| `05_conversion_trace.py` | `"3"` → `int` → `75,000 VND` | Vì sao `"ba"` và `"0"` phải từ chối? |
| `06_fstring_ticket.py` | `strip()`, `int()`, hóa đơn với f-string | Khi đổi số vé từ 2 lên 3, output là gì? |

Từ **repository root**, chạy:

```bash
python weeks/week-02-variables-types/examples/04_predict_types.py
python weeks/week-02-variables-types/examples/05_conversion_trace.py
python weeks/week-02-variables-types/examples/06_fstring_ticket.py
```

Tiếp theo, tự làm [**3 bài tương tự**](practice/README.md) trên
thông tin cá nhân, đơn hàng và vé. Mỗi bài có TODO, ví dụ input/output,
trường hợp sai và checker riêng:

```bash
python weeks/week-02-variables-types/practice/checks/check_practice.py --starter
```

**Starter chưa sửa → FAIL có chủ đích**. Chỉ `--starter` mới kiểm bài em;
`--solutions` chỉ kiểm lời giải tham khảo, không chứng minh đã làm bài.

## Evidence

- output `Week 02 solution checks: PASS`;
- một ví dụ chứng minh kiểu trả về của `input()`;
- mini-project chạy với input hợp lệ và từ chối năm không phải số;
- commit và một ghi chú về lỗi conversion bạn đã quan sát.
