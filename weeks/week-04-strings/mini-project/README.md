# Mini-project — Text Analyzer

Chuẩn hóa một đoạn text và tạo thống kê có thể nhìn thấy.

## Yêu cầu

- dùng `strip`, `lower`, `split`, `join`;
- đếm ký tự, từ và số lần một keyword xuất hiện;
- dùng regex để trích simple course codes như `PJ-101`;
- xử lý text rỗng;
- không đọc file ở Week 04.

```bash
python weeks/week-04-strings/mini-project/starter.py
```

## Trước mini-project — luyện một bài nhỏ hơn

Nếu vẫn nhầm `split()` với `count()` hoặc `search()` với
`fullmatch()`, học [ba ví dụ mới](../WORKED-EXAMPLES.md)
và tự làm [3 bài tương tự](../practice/README.md) trước khi
quay lại Text Analyzer. Tại Text Analyzer, hãy ghi rõ
`normalized.count("python")` đếm **chuỗi con**, không tự đếm
“từ python” chính xác. Trường hợp `pythonic` cho thấy sự khác biệt.
Regex `PJ-[0-9]{3}`/pattern khác chỉ dùng cho minh họa, không
là bộ xác thực mã sản xuất.
