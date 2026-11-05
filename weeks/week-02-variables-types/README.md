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
5. Chạy [official solution check](checks/README.md).
6. Hoàn thành [Thẻ sinh viên](mini-project/README.md).

## Evidence

- output `Week 02 solution checks: PASS`;
- một ví dụ chứng minh kiểu trả về của `input()`;
- mini-project chạy với input hợp lệ và từ chối năm không phải số;
- commit và một ghi chú về lỗi conversion bạn đã quan sát.
