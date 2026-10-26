# Tuần 15: Dự án cuối khóa 🎓

Tuần 15 là capstone: xây dựng chương trình có chức năng thực tế, lưu dữ liệu, kiểm thử và tài liệu. Đọc yêu cầu chính thức tại [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## Dự án mẫu: Expense Tracker

Ứng dụng quản lý thu/chi trên terminal:
- Thêm khoản thu và khoản chi.
- Xem danh sách giao dịch.
- Tính tổng thu, tổng chi và số dư.
- Lọc giao dịch theo danh mục.
- Lưu/đọc dữ liệu JSON.
- Kiểm tra input và xử lý dữ liệu lỗi cơ bản.

## Cấu trúc

- [main.py](main.py): logic ứng dụng và giao diện terminal.
- `data/transactions.json`: dữ liệu được tạo khi lưu lần đầu.
- [tests/test_main.py](tests/test_main.py): kiểm thử tự động bằng `unittest`.
- [AI_USAGE.md](AI_USAGE.md): mẫu khai báo hỗ trợ AI cần chỉnh lại trung thực.

## Chạy chương trình

Từ thư mục gốc repository:

```bash
python weeks/week-15-capstone-project/main.py
```

Trên Windows, có thể dùng `py` thay cho `python`.

## Chạy test

```bash
python -m unittest discover -s weeks/week-15-capstone-project/tests -v
```

Test bao gồm thêm giao dịch, từ chối dữ liệu sai, tổng thu/chi, lọc danh mục và lưu/đọc JSON. Hãy xem kết quả chạy thực tế trước khi đánh dấu hoàn thành.

## Checklist trước khi nộp

- [ ] Chạy chương trình và tự thử các chức năng.
- [ ] Chạy test và đọc kết quả.
- [ ] Giải thích được các hàm chính.
- [ ] Đọc [FINAL_PROJECT.md](../../FINAL_PROJECT.md) và đối chiếu rubric.
- [ ] Chỉnh [AI_USAGE.md](AI_USAGE.md) đúng với quá trình làm bài thực tế.
- [ ] Commit tiến độ lên GitHub.

> Đây là project mẫu tham khảo. Hãy tự chạy, hiểu và cải tiến trước khi dùng làm bài nộp.
