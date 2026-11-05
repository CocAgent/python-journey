# 16 câu dự đoán — viết đáp án trước khi chạy

**Không mở [ANSWER-KEY.md](ANSWER-KEY.md) trước khi thử.**
Ghi câu trả lời, lý do, và một input tương tự để tự kiểm.

1. `print("12" + "3")` in gì? Nếu đổi thành `12 + 3`?
2. `bool("False")` cho `True` hay `False`? Tại sao?
3. Nếu `if score >= 5` đứng trước `elif score >= 8`, score=9 vào nhánh nào?
4. `"Python"[::-1]` là gì?
5. `"python pythonic".count("python")` bằng bao nhiêu? Có phải đếm **từ**?
6. Với `a=["An"]`, `b=a`, `b.append("Chi")`: biến `a` ra sao?
7. `type(("Cóc",)).__name__` và `type(("Cóc")).__name__`?
8. `list(range(1, 4))` gồm các số nào?
9. `break` khác `continue` như thế nào?
10. Hàm chỉ `print(10)` nhưng không `return`: caller nhận gì?
11. Với `data={"score":8}`, `data.get("level", "beginner")` trả gì?
12. `list(set(["b","a","b"]))` có bảo đảm giữ thứ tự `b,a` không?
13. Sau khi đọc CSV bằng `csv.DictReader`, giá trị điểm `"8"` là kiểu gì?
14. `json.loads("[]")` thành công có chứng minh schema yêu cầu dict hợp lệ không?
15. `except ValueError` có tự bắt một `TypeError` không?
16. Trong `try/except/else/finally`, `finally` có chạy khi `return`
    xảy ra trong `except` không? Có nên `return` trong `finally`?

**Sau khi tự giải:** đối chiếu
[đáp án có giải thích](ANSWER-KEY.md), sau đó làm
[ba lab thực hành](practice/README.md).
