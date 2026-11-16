# Quy trình ôn tập 60 phút cho sinh viên

**5 phút — chuẩn bị:** mở terminal tại repo `python-journey`,
đọc đề và kiểm Python >=3.12. Không cần `pip install`.
Dùng VS Code, IDLE hoặc trình soạn thảo bất kỳ.

**10 phút — dự đoán:** đánh dấu kiểu dữ liệu vào/ra, viết
ít nhất một input bình thường và một input sai cho mỗi câu.

**35 phút — code:** sửa từng file `submissions_de1/Cau*.py`,
không sửa tên hàm hoặc phần `autograde`. Phần `raise
NotImplementedError` là TODO phải thay bằng code thật.

**10 phút — chạy và sửa lỗi:** chạy lệnh:

```bash
python review/mock-exams/de-01/autograde_de1.py --student
```

Đọc từng dòng `FAIL`, sửa bài và chạy lại. Có thể
thêm `--verbose` để xem cả ca PASS; khi đã tự
làm và sửa mới so `--reference`.

## Trên Windows

```powershell
cd D:\Projects\python-journey
py -3 review\mock-exams\de-01\autograde_de1.py --student
```

Đường dẫn trên chỉ là ví dụ. Nếu chưa có repo,
tải ZIP từ GitHub rồi giải nén ở thư mục riêng.
Xem [hướng dẫn làm việc qua máy từ xa](../../REMOTE-DESKTOP-SETUP.md).
Không tải đề từ một phiên Remote Desktop không đáng tin.

## Nhật ký sửa lỗi

```text
Mã sinh viên (tự điền):
Ý bài:
Input mình dự đoán:
Kết quả mình nhận:
Vì sao sai:
Một thay đổi đã sửa:
Chạy lại input cũ có PASS?
Điểm tự kiểm sau khi tự sửa (/10):
```

## Nộp bài

Chỉ nộp **10 file `Cau1a.py` … `Cau5b.py`** từ
`submissions_de1/` (hoặc zip thư mục đó), không nộp đáp án
`solutions_de1/`, không nộp `__pycache__`, token hoặc
thông tin cá nhân không cần thiết. Nếu giảng viên yêu cầu
ảnh kết quả máy kiểm, đảm bảo ảnh không chứa thông tin nhạy cảm.

**Lưu ý:** điểm tự chấm công khai không phải điểm thi chính thức.
