# Đề ôn tập tổng hợp Python — 90 phút

**Đề thực hành tự luyện** theo định dạng 90 phút, gồm **5 câu × 2 điểm**
và **10 ý × 1 điểm**. Nội dung lấy cảm hứng từ cấu trúc đề thực hành
Python cơ bản trong thư mục *Tests Python 2026*, nhưng câu hỏi và
dữ liệu mẫu ở đây được thiết kế lại cho quá trình ôn tập.

Bộ 60 phút ở [../de-01/](../de-01/) là bài khởi động **tự chọn**;
**bộ 90 phút này là bài ôn tập tổng hợp được khuyến nghị**.

## Học liệu

| Tệp/thư mục | Vai trò |
|---|---|
| [DE-90-PHUT.md](DE-90-PHUT.md) | Đề thi thử đầy đủ, contract input/output |
| [STUDENT-GUIDE.md](STUDENT-GUIDE.md) | Các bước chuẩn bị, thời gian, nộp bài |
| [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md) | Ví dụ đã giải thích bằng **bài toán khác** |
| [HINTS.md](HINTS.md) | Gợi ý theo mức độ |
| [TEACHER-GUIDE.md](TEACHER-GUIDE.md) | Thang điểm, quy trình nghiệm thu và giới hạn |
| `submissions_de1/Cau1a.py`…`Cau5b.py` | 10 file sinh viên tự điền TODO |
| `solutions_de1/` | Lời giải tham khảo, xem sau khi tự giải |
| `test_de1.py` | **78 trường hợp kiểm thử công khai** |
| `runner_de1.py`, `autograde_de1.py` | Chạy mỗi ca trong process riêng; chấm thử /10 |

## Phạm vi kiến thức

| Câu | Nội dung | Điểm |
|---|---|---:|
| 1 | Số nguyên, chữ số, vòng lặp và tổng phân số | 2 |
| 2 | Chuỗi, ký tự viết hoa, đối xứng | 2 |
| 3 | Danh sách số nguyên có tín hiệu kết thúc `0` | 2 |
| 4 | Dictionary quản lý sách và sao chép dữ liệu | 2 |
| 5 | OOP: lớp `DienThoai`, thuộc tính, phương thức, tạo đối tượng | 2 |

## Lưu ý về trình độ và nguồn mã thực hành

Câu 5 sử dụng **lập trình hướng đối tượng (OOP)**; trong Python Journey,
kiến thức này được học sâu hơn ở **Week 14**. Nếu đang ôn tập
Week 01–11, sinh viên nên làm Câu 1–4 trước, đọc ví dụ
`class` trong [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md)
rồi mới hoàn thành Câu 5. Đây là đề tự luyện mở rộng,
**không phải điều kiện hoàn thành Week 11**.

Để lập trình và tự chấm, cần các file Python thực trong
[thư mục `submissions_de1/`](submissions_de1/) trên GitHub.
Bản Google Docs trên Drive chỉ dùng để **đọc hoặc sao chép mã**,
không thể trực tiếp chạy như file `.py`. Người học có thể tải
repository bằng **Code → Download ZIP** rồi giải nén,
hoặc sử dụng `git clone`.

## Chạy từ thư mục gốc `python-journey`

```bash
python review/mock-exams/de-90-phut-01/autograde_de1.py --student
python review/mock-exams/de-90-phut-01/autograde_de1.py --reference
```

**Khi chưa làm TODO:** `--student` dự kiến `0.00/10.00`.
**Reference hoàn chỉnh:** `--reference` dự kiến
`10.00/10.00` với 78/78 ca PASS. Điểm tự kiểm được
chia theo số ca vượt qua ở mỗi ý, tối đa 1 điểm/ý.

Đây là **điểm tự học, không phải điểm thi chính thức**.
Chế độ reference không đánh giá code của sinh viên.
Không sửa file test/grader để tăng điểm giả.

**Yêu cầu:** Python >=3.12, thư viện chuẩn; không cần Internet,
framework hay `pytest` đối với sinh viên. Chỉ chạy code tự viết hoặc
đáng tin cậy: subprocess timeout **không phải sandbox**.

Vòng học: dự đoán → viết → chạy → phân tích FAIL → sửa →
kiểm tra lại → giải thích.
