# Week 03 — Bộ bài tương tự: tự viết `if/elif/else` và kiểm logic

**Bài tập bổ sung, không thay ba bài gốc trong `exercises/`.**
Thực hành sau [3 ví dụ có giải thích](../WORKED-EXAMPLES.md).
Chỉ cần Python >=3.12, không cần pip, pytest, LLM hay Internet.

## Làm thế nào để học mà không chép lời giải?

1. Chạy một ví dụ ở `examples/04–06` và dự đoán output trước.
2. Đọc yêu cầu trong `practice/starter/labNN_*.py`, xác định ít nhất
   một input hợp lệ, một input biên và một input sai.
3. Chạy starter (sẽ in `TODO`), tự thêm `if/elif/else` theo hướng dẫn.
4. Chạy lại với **hai input khác nhau**, đọc `stdout` và giải thích nhánh nào chạy.
5. Chạy máy tự kiểm `--starter`. **Ban đầu FAIL là đúng thiết kế.**
6. Chỉ mở `practice/solutions/` khi đã tự thử và ghi một bug được sửa.

## Lab 01 — Xếp loại điểm (thứ tự nhánh)

**Input:** một số nguyên từ 0 đến 10 ở terminal.

| Input | Kết quả mong đợi |
|---|---|
| 4 | `Cần luyện tập` |
| 5 | `Đạt` |
| 7 | `Đạt` |
| 8 hoặc 10 | `Giỏi` |
| 11, -1, abc | `Điểm không hợp lệ` |

```bash
python weeks/week-03-conditionals/practice/starter/lab01_score.py
```

Hãy nhập `8` rồi nhấn Enter. Câu hỏi: tại sao `score >= 8`
phải đứng trước `score >= 5`?

## Lab 02 — Điều kiện vào cửa (boolean)

**Input theo thứ tự:** tuổi (0..120), có vé (`y/n`),
cửa đã đóng (`y/n`). Đây chỉ là **quy tắc giả lập**.

| Tuổi | Có vé? | Cửa đóng? | Kết quả |
|---:|---|---|---|
| 18 | y | n | `Được vào` |
| 17 | y | n | `Không được vào` |
| 18 | n | n | `Không được vào` |
| 18 | y | y | `Không được vào` |
| abc | y | n | `Dữ liệu không hợp lệ` |
| 18 | x | n | `Dữ liệu không hợp lệ` |

```bash
python weeks/week-03-conditionals/practice/starter/lab02_entry.py
```

Nhập `18`, Enter, `y`, Enter, `n`, Enter.
Không dùng `bool("n")` để hiểu người dùng trả lời “không”.

## Lab 03 — Ưu tiên miễn phí giao hàng (guard + and/or)

**Input:** tổng tiền VND không âm, có là thành viên (`y/n`),
có chọn giao nhanh (`y/n`).

Các quy tắc chỉ phục vụ bài học:

- **Miễn phí** nếu tổng từ **200.000 VND**, **hoặc** thành viên có
  tổng từ **100.000 VND**.
- Nếu chưa đủ miễn phí: giao nhanh **50.000 VND**, giao thường
  **30.000 VND**.
- Dữ liệu sai phải báo `Dữ liệu không hợp lệ` và **không in phí**.

| Tổng | Thành viên | Giao nhanh | Phí mong đợi |
|---:|---|---|---:|
| 0 | n | n | 30.000 |
| 0 | n | y | 50.000 |
| 99.999 | y | n | 30.000 |
| 100.000 | y | n | 0 |
| 199.999 | n | y | 50.000 |
| 200.000 | n | y | 0 |

```bash
python weeks/week-03-conditionals/practice/starter/lab03_shipping.py
```

**Hỏi trước khi làm:** tại sao xét giao nhanh trước miễn phí sẽ làm
đơn đủ ưu đãi vẫn bị tính tiền? Dùng ngoặc cho logic
`(amount >= 200_000) or (is_member and amount >= 100_000)`.

## Tự kiểm bài do chính em viết

Chạy ở **gốc repo**:

```bash
python weeks/week-03-conditionals/practice/checks/check_practice.py --starter
```

Máy chạy **nhiều case thật** cho mỗi bài, không chỉ xem file có tồn tại.
Sau khi hoàn thiện ba lab:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Week 03 student practice: PASS (3/3)
```

Nếu gặp FAIL, xem *Input=... expected... actual...* của lab đó,
dự đoán nhánh chạy sai và sửa **starter**, không sửa checker.

Sau khi tự làm xong, xem `practice/solutions/` và kiểm riêng:

```bash
python weeks/week-03-conditionals/practice/checks/check_practice.py --solutions
```

**PASS của `--solutions` không chứng minh sinh viên đã giải xong starter.**

## Ghi bằng chứng học tập

```text
Bài số:
Input thường -> Dự đoán -> Kết quả thực tế:
Input biên -> Dự đoán -> Kết quả thực tế:
Input sai -> Lỗi được từ chối ra sao:
Nhánh nào đã chạy? Vì sao?
Một bug logic em đã sửa:
Commit / ảnh terminal (nếu giảng viên yêu cầu):
```

Vòng học: **Dự đoán → Chạy → Giải thích → Tự sửa → Kiểm chứng**.
Không thêm rubric hoặc quota file, hàm hay framework cho Week03.
