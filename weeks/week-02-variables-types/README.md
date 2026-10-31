# Tuần 02 — Variables · Types · Input/Output

Tuần này bạn đặt tên cho dữ liệu, nhận input dạng text, chuyển kiểu có chủ đích
và tạo output rõ bằng f-string.

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
