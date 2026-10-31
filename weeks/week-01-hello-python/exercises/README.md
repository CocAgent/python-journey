# Bài tập Tuần 01 — yêu cầu và tự đối chiếu

**Cốt lõi:** `ex01_hello.py` và `ex02_calculator.py`. Chỉ cần
`print()`, phép toán, string và comment. Không cần hàm, vòng lặp hay
`pytest`. `ex03_input.py` là **bài mở rộng Tuần 02**.

## Bài 01 — `print()` và hình chữ nhật

Chạy `python weeks/week-01-hello-python/exercises/ex01_hello.py`.
Sinh viên phải tự viết lệnh in:

1. `Hello, World!`
2. Tên bản thân trên dòng riêng.
3. Ba dòng về sở thích.
4. Khung hình chữ nhật 5 × 4:

```text
*****
*   *
*   *
*****
```

Thử thách tên bằng ASCII art là tùy chọn. File starter không in
“hoàn thành” mặc định vì phần TODO vẫn đang chờ sinh viên.

## Bài 02 — phép tính

Chạy `python weeks/week-01-hello-python/exercises/ex02_calculator.py`.
Không chỉ chép đáp số: hãy **viết biểu thức tính** rồi dùng `print()`.

| Biểu thức | Kết quả mong đợi |
|---|---:|
| `2024 + 1000` | `3024` |
| `150000 - 35000 * 3` | `45000` VNĐ |
| `3.14159 * 7 ** 2` | `153.94` khi làm tròn 2 chữ số |
| `100 // 7` | `14` viên/người |
| `100 % 7` | `2` viên còn lại |
| `37 * 9 / 5 + 32` (tự chọn) | `98.6` °F |

## Bài 03 — `input()` (tự chọn)

`input()`, chuyển kiểu bằng `int()`/`float()` được dạy ở Tuần 02.
Không trừ điểm Tuần 01 nếu chưa làm bài này. Không yêu cầu `try/except`
cho đầu vào sai vào thời điểm này.

## Tự kiểm tra và nộp

Chạy lại từng file, đối chiếu từng đầu ra, thay một con số để giải thích
phép toán. Điền [mẫu minh chứng](../evidence-template.md), ghi một lỗi đã
sửa và commit SHA. **`checks/check_week.py` chỉ kiểm tra giáo trình,
không chấm bài của bạn.**

| Tiêu chí tham khảo | Điểm |
|---|---:|
| Nhận diện Python, terminal và REPL | 2 |
| Bài 01: in đúng, khung có khoảng trắng chính xác | 2 |
| Bài 02: biểu thức số học và kết quả | 2 |
| Đọc và sửa một lỗi, có minh chứng | 1 |
| Mini-project thẻ ASCII tĩnh | 1 |
| Git commit, hướng dẫn chạy, evidence | 2 |
| **Tổng** | **10** |

Rubric dành cho giáo viên; không dùng kết quả test tham chiếu làm điểm tự động.
