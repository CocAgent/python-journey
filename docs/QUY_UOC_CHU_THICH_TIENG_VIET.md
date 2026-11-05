# Quy ước chú thích Python bằng tiếng Việt

> Áp dụng cho tài liệu học, ví dụ, starter và code mẫu. Giữ nguyên cú pháp Python, tên API và thông báo lỗi của thư viện.

## Nguyên tắc

1. Chú thích giải thích **vì sao** chọn cách xử lý, điều kiện biên hoặc một sai lầm dễ mắc; không kể lại lệnh đã quá rõ.
2. Docstring nói rõ mục đích, đầu vào/đầu ra và trường hợp phát sinh lỗi (khi cần).
3. Mỗi khối comment ngắn gọn, dễ đọc; tiếng Việt có dấu và mã hóa UTF-8.
4. Tên biến/hàm ưu tiên `snake_case` không dấu, phản ánh nghiệp vụ; thuật ngữ `list`, `dict`, `pytest`, `assert`, `return` có thể giữ nguyên.
5. Không chú thích thay cho việc đặt tên tốt, cũng không đưa đáp án đầy đủ vào file starter có bài tập.

## Ví dụ nên tránh

```python
tong = a + b  # Cộng a với b
print(tong)  # In tổng
```

Hai comment trên chỉ đọc lại code, không giúp người mới suy luận thêm.

## Ví dụ khuyến khích

```python
def tinh_diem_trung_binh(diem: list[float]) -> float:
    """Trả về điểm trung bình; từ chối danh sách rỗng."""
    # Danh sách rỗng không có mẫu số hợp lệ; báo lỗi giúp người gọi xử lý rõ ràng.
    if not diem:
        raise ValueError("Cần ít nhất một điểm")

    return sum(diem) / len(diem)
```

**Giải thích cho sinh viên:** `raise` cho biết không thể tính trung bình khi thiếu dữ liệu. Không tự ý trả `0` vì dễ nhầm “chưa có điểm” với “điểm trung bình bằng 0”.

## Cấu trúc gợi ý cho một file bài tập

- Docstring đầu file: tên bài, mục tiêu, kết quả mong đợi.
- TODO: việc sinh viên phải hoàn thành; không đưa sẵn lời giải.
- Ví dụ chạy mẫu: ít nhất một trường hợp thông thường.
- Một trường hợp biên: rỗng, bằng 0, giá trị ngoài khoảng hoặc sai định dạng.
- Lệnh kiểm chứng: câu lệnh cụ thể, chỉ rõ nó kiểm tra lời giải mẫu hay bài sinh viên.

**Không áp dụng máy móc quy tắc “mọi dòng phải có comment”**: quá nhiều chú thích sẽ gây nhiễu nội dung bài học.
