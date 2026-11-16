# ĐỀ ÔN TẬP 01 — PYTHON CƠ BẢN (60 PHÚT)

Bộ thực hành này được **thiết kế mới từ cấu trúc đề mẫu CBPYTHON**:
5 câu × 2 điểm, mỗi câu 2 ý × 1 điểm; nộp 10 file `Cau1a.py` …
`Cau5b.py`. Đây là **đề ôn tập tự đánh giá**, không phải đề thi
chính thức hoặc thang điểm bắt buộc của Python Journey.

**Bắt đầu:** đọc [ĐỀ-01.md](DE-01.md), tự làm phần
`submissions_de1/`, chạy tự chấm, tự sửa lỗi, rồi chỉ sau đó
mới xem `solutions_de1/`.

## Sơ đồ thư mục

```text
de-01/
├── README.md                 # Bắt đầu ở đây
├── DE-01.md                  # 5 câu/10 ý, 60 phút
├── HUONG-DAN-SINH-VIEN.md   # Quy trình từng bước
├── VI-DU-MAU.md              # 2 ví dụ được giải thích, KHÁC bài thi
├── HINTS.md                  # Gợi ý 3 tầng, không chép lời giải
├── HUONG-DAN-GIANG-VIEN.md  # Phân bố điểm và giới hạn self-grade
├── test_de1.py               # 58 ca kiểm công khai
├── runner_de1.py             # Chạy từng ca trong process riêng
├── autograde_de1.py          # Tự chấm 10 ý trên thang /10
├── submissions_de1/         # 10 file STARTER có TODO (sinh viên sửa)
└── solutions_de1/           # 10 lời giải tham khảo tách biệt
```

## Lệnh tự kiểm từ gốc repository

```bash
python review/mock-exams/de-01/autograde_de1.py --student
python review/mock-exams/de-01/autograde_de1.py --reference
```

- `--student`: chấm **chính code sinh viên**. Lúc mới bắt đầu
  starter chứa `NotImplementedError`, nên điểm `0.00/10.00`
  là **đúng thiết kế**.
- `--reference`: kiểm 10 lời giải mẫu; kỳ vọng `10.00/10.00`.
  **Reference PASS không có nghĩa sinh viên đã làm bài.**
- `--verbose`: hiển thị tất cả ca kiểm; không sửa `test_de1.py`
  hay `autograde_de1.py` để tạo điểm giả.
- Dùng Python >=3.12; trên Windows có thể thử `py -3`
  khi `python` không có trong PATH. Không cần `pip`, API,
  Internet hay pytest cho việc làm đề.

## Học bằng cách dự đoán và kiểm chứng

1. Đọc yêu cầu, viết dự đoán đầu ra của **một test thường,
   một ca biên, một ca sai** trước khi code.
2. Hoàn thiện từng hàm trong file `submissions_de1/Cau*.py`.
   **Không đổi tên file/hàm/signature.**
3. Chạy tự chấm sau mỗi 1–2 ý, đọc thông báo FAIL để tìm nhánh
   hoặc kiểu dữ liệu chưa xử lý.
4. Sửa nguyên nhân, chạy lại ca cũ để làm regression.
5. Khi đã tự thử xong, mới đối chiếu lời giải và ghi minh chứng.
6. Hoàn thiện [mẫu báo cáo](HUONG-DAN-SINH-VIEN.md#nhật-ký-sửa-lỗi).

## Giới hạn quan trọng

Mã sinh viên được thực thi bằng subprocess với timeout.
Đây **không phải sandbox bảo mật**: chỉ chạy mã chính mình
hoặc mã đã đáng tin; giảng viên phải dùng sandbox/cơ chế tách
quyền khi nhận code không tin cậy từ nguồn bên ngoài.

Các ví dụ và đáp án được công khai vì mục đích **ôn tập**;
không dùng điểm tự chấm làm chứng cứ chấm thi chính thức.
Bộ này không thay [đề chính](../../../weeks/week-09-midterm-project/README.md)
hoặc [SYLLABUS.md](../../../SYLLABUS.md).
