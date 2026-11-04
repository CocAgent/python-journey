# Bộ làm bài và chấm điểm — đề 11301

Thư mục này minh họa **Package – Module – Function**:

- **Package:** thư mục `bo_cham_diem/` (có `__init__.py`).
- **Module:** `bai_lam.py` và `cham_diem.py`.
- **Function:** các hàm như `hop_le_n()`, `dem_chu_so_le()`, `tinh_s()`...

## Cách làm

1. Chỉ điền lời giải trong `bai_lam.py`.
2. Giữ nguyên tên hàm và tham số để chương trình chấm gọi được.
3. Không sửa `cham_diem.py`; đây là module chạy test.

## Chạy chấm điểm trên Windows

Tại thư mục gốc repository, mở Terminal và chạy:

```powershell
py kiem-tra-on-tap/de-thi-11301/bo_cham_diem/cham_diem.py
```

Nếu Terminal đang ở ngay trong thư mục `bo_cham_diem`, chạy:

```powershell
py cham_diem.py
```

Kết quả hiển thị điểm từng ý (1a, 1b, 1c, 2a...) và tổng điểm /10. Mỗi ý có
nhiều test nhỏ; điểm được chia theo tỷ lệ test đúng.

## Quy ước theo đề đã cung cấp

- Câu 1(c): dùng công thức theo đáp án đọc được: `1/2 + 1/4 + ... + 1/(2*n)`.
- Câu 3(b): tính tổng các số **dương chẵn**.
- Câu 3(a): dùng function nhận danh sách làm dữ liệu đầu vào để kiểm thử tự động;
  số 0 là dấu kết thúc và không được đưa vào danh sách kết quả.
- Câu 4(a): truyền `nam_hien_tai` vào hàm để kiểm tra năm xuất bản và giúp test ổn định.

Lưu ý: đây là bộ test tự luyện, không đảm bảo bao quát mọi cách chấm của giảng viên.
