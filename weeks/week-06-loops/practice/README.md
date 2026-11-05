# Week 06 — Ba bài tương tự: tự viết, tự đoán, tự kiểm

**Bắt đầu sau khi đọc [ba ví dụ có giải thích](../WORKED-EXAMPLES.md).**
Bộ này **không thay** bài tập gốc trong `exercises/`, machine check
gốc, hoặc mini-project `Iteration Report`.

## Quy trình thực hành

1. Đọc ví dụ 04–06, dự đoán output **trước** khi chạy.
2. Chạy ví dụ, xác định số lượt lặp, điều kiện dừng, nhánh nào bị bỏ.
3. Mở file tương ứng trong `practice/starter/`, tự làm TODO.
4. Chạy file starter (Lab 02 yêu cầu nhập một số 0..5).
5. Thử ca thường, ca biên, ca lỗi; ghi đầu ra.
6. Chạy `--starter` và sửa code cho đến khi đạt PASS (3/3).
7. Chỉ sau khi tự làm, xem `practice/solutions/`.

## Lab 01 — Báo cáo điểm đã đánh số

File: `starter/lab01_numbered_scores.py`. Cho 3 bạn và 3 điểm:

```python
names = ["An", "Bình", "Chi"]
scores = [8, 9, 7]
```

Em cần dùng `zip(..., strict=True)` và
`enumerate(..., start=1)` để in:

```text
1. An: 8
2. Bình: 9
3. Chi: 7
Tổng điểm: 24
```

**Tự hỏi:** vì sao dùng `strict=True`? Nếu có 3 tên nhưng chỉ
2 điểm, ta có nên âm thầm bỏ mất bạn Chi không?

## Lab 02 — Đếm ngược an toàn bằng while

File: `starter/lab02_safe_countdown.py`. Nhập số nguyên từ 0 đến 5.

| Input | Output cuối cần thấy |
|---|---|
| `3` | `Còn: 3`, `Còn: 2`, `Còn: 1`, `Kết thúc` |
| `0` | chỉ `Kết thúc` |
| `5` | lần lượt 5,4,3,2,1 rồi `Kết thúc` |
| `abc`, `-1`, `6`, rỗng | chỉ `Dữ liệu không hợp lệ` |

**Không thử chạy một vòng `while` không có điều kiện dừng**:
hãy chỉ ra dòng nào làm `remaining > 0` thành `False`.

## Lab 03 — Lọc số, `break/continue` và bình phương chẵn

File: `starter/lab03_filter_squares.py`.

Lặp `range(1,11)`, bỏ bội số 3 bằng `continue`;
dừng sau 8 bằng `break`; bình phương các số chẵn đã chọn
bằng một comprehension đơn giản.

```text
Đã chọn: [1, 2, 4, 5, 7, 8]
Bình phương chẵn: [4, 16, 64]
```

**Tự hỏi:** vì sao 3, 6, 9, 10 không xuất hiện trong list?
Nếu đổi điều kiện `break`, output nào thay đổi?

## Chạy tự kiểm từ repo root

```bash
# Kiểm code sinh viên — trước khi làm TODO có chủ đích FAIL
python weeks/week-06-loops/practice/checks/check_practice.py --starter

# Kiểm lời giải mẫu — dùng trong CI, KHÔNG chấm bài sinh viên
python weeks/week-06-loops/practice/checks/check_practice.py --solutions
```

Checker chạy **nhiều input cho Lab 02**, kể cả 0, 1, 3, 5, -1
và chữ. Nếu FAIL, đọc output mong đợi/thực tế, sửa **file starter**,
không sửa checker. Kết quả đúng sau khi làm xong:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Week 06 student practice: PASS (3/3)
```

**Lưu ý học thuật:** checker so đầu ra và không thể chứng minh
mọi cách triển khai đều đúng. Sinh viên cần giải thích dòng
`for/while/break/continue/zip` mình đã dùng và thử biến đổi
một dữ liệu mới.

## Báo cáo tự học ngắn

```text
Bài:
Dự đoán số lượt lặp:
Điều kiện dừng:
Input thường → expected → actual:
Input biên / sai → expected → actual:
Một lỗi đã sửa:
Nếu dữ liệu đổi, chương trình còn đúng không? Vì sao?
```

Không đòi hỏi viết function nâng cao (Week07), `pytest`
(Week12) hoặc thư viện ngoài.
