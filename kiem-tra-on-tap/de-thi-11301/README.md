# Đề thi ôn tập Python — Mã đề 11301

**Môn:** Lập trình Python  
**Thời gian:** 90 phút  
**Tổng điểm:** 10 điểm  
**Hình thức:** Thực hành

Thư mục này được xây dựng từ đề thi và đáp án mã đề 11301 do người học cung cấp. Mỗi câu được tách thành một file Python để dễ luyện tập và kiểm tra độc lập.

## Cấu trúc

| File | Nội dung | Điểm |
|---|---|---:|
| [cau-1-so-nguyen.py](cau-1-so-nguyen.py) | Kiểm tra số nguyên, đếm chữ số lẻ, tính tổng S | 2.0 |
| [cau-2-xu-ly-chuoi.py](cau-2-xu-ly-chuoi.py) | Chữ hoa, chuỗi đối xứng, tổng chữ số | 2.0 |
| [cau-3-list.py](cau-3-list.py) | Nhập danh sách, tổng số dương chẵn, đếm phần tử | 2.0 |
| [cau-4-dictionary.py](cau-4-dictionary.py) | Quản lý sách bằng dictionary và xóa theo mã | 2.0 |
| [cau-5-oop-dienthoai.py](cau-5-oop-dienthoai.py) | Class DienThoai, khởi tạo và hiển thị đối tượng | 2.0 |

## Cách ôn tập đề xuất

1. Đọc yêu cầu của một câu trong file tương ứng.
2. Tự viết lời giải trước, không nhìn phần code tham khảo.
3. Chạy chương trình và thử thêm dữ liệu khác.
4. Đối chiếu với code tham khảo, tự giải thích được từng dòng.
5. Khi đã hiểu, đóng phần tham khảo và tự làm lại trong 90 phút.

## Cách chạy trên Windows

Mở Terminal tại thư mục repository:

```powershell
py kiem-tra-on-tap/de-thi-11301/cau-1-so-nguyen.py
py kiem-tra-on-tap/de-thi-11301/cau-2-xu-ly-chuoi.py
py kiem-tra-on-tap/de-thi-11301/cau-3-list.py
py kiem-tra-on-tap/de-thi-11301/cau-4-dictionary.py
py kiem-tra-on-tap/de-thi-11301/cau-5-oop-dienthoai.py
```

Nếu máy dùng lệnh `python` thay cho `py`, có thể đổi lệnh tương ứng.

## Lưu ý về đáp án

- Câu 3(b) được hiểu là tổng các số **dương chẵn**, đúng theo phần đáp án đọc được trong PDF.
- Câu 1(c): bản PDF bị lỗi nhận dạng ở biểu thức in trên đề. Phần đáp án thể hiện công thức `S = 1/2 + 1/4 + ... + 1/(2n)`; file tham khảo bám theo công thức trong đáp án.
- Đây là code tham khảo để ôn tập. Khi thi, cần tự viết lại và kiểm tra dữ liệu nhập.

---
**Python Journey · Learn · Build · Test · Debug · Improve**

## Bộ điền đáp án và chấm tự động

Nếu muốn tự làm từng ý rồi xem điểm ngay, mở thư mục [bo_cham_diem](bo_cham_diem/):

- [bai_lam.py](bo_cham_diem/bai_lam.py): nơi bạn tự viết đáp án cho 1a, 1b, 1c... 5b.
- [cham_diem.py](bo_cham_diem/cham_diem.py): chạy test và tính điểm từng ý trên tổng 10 điểm.
- [README hướng dẫn](bo_cham_diem/README.md): cách chạy trong VS Code.

Lệnh chạy từ thư mục gốc repository:

```powershell
py kiem-tra-on-tap/de-thi-11301/bo_cham_diem/cham_diem.py
```
