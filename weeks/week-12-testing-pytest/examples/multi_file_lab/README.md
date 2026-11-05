# Thực hành kiểm thử chương trình có nhiều tệp

Chương trình mô phỏng một đơn hàng nhỏ. Đây là **ví dụ giảng viên**, không phải bài nộp đã hoàn thành của sinh viên.

| Tệp | Trách nhiệm | Ví dụ lỗi cần phát hiện |
|---|---|---|
| `pricing.py` | Kiểm tra số lượng và tính tổng | Cộng nhầm thành tiền; chấp nhận số lượng âm |
| `storage.py` | Đọc/ghi JSON | Trả về dữ liệu rỗng; không nhận diện JSON hỏng |
| `service.py` | Kết nối tính tiền và lưu tệp | Làm mất đơn giá; không lưu đơn hàng |
| `test_multi_file_lab.py` | Test từng module và luồng tích hợp | Kiểm tra kết quả cụ thể, tệp thực sự tồn tại |

## Chạy ở thư mục gốc repository

```bash
python -m pytest weeks/week-12-testing-pytest/examples/test_multi_file_lab.py -q
python weeks/week-12-testing-pytest/checks/check_multi_file_faults.py
```

Lệnh đầu phải PASS với chương trình đúng. Lệnh thứ hai tạo **sáu lỗi cố ý trên bản sao tạm** của ba tệp Python, lần lượt chạy lại pytest và đếm các lỗi bị phát hiện. Không có thao tác nào sửa file bài học gốc.

## Câu hỏi để sinh viên tự trả lời

1. Nếu chỉ test `pricing.py`, liệu bạn có phát hiện được `service.py` quên lưu tệp không?
2. Vì sao cần dùng `tmp_path` để kiểm tra chức năng lưu tệp?
3. Khi JSON bị hỏng, cần kiểm tra *loại lỗi* và *thông báo lỗi* thế nào?
4. Test PASS trên chương trình đúng có đủ để khẳng định test có chất lượng không?

**Tự mở rộng:** thử thêm `quantity=0`, `unit_price=0` và mô tả kết quả mong đợi trước khi chạy.

Ghi nhớ: sáu lỗi cố ý là minh họa về khả năng phát hiện lỗi, **không phải bằng chứng chương trình đã hết lỗi**.
