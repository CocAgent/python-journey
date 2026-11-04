# Hướng dẫn giảng viên — Đề ôn tập thực hành 90 phút

**Mục đích:** hỗ trợ tự luyện và thảo luận giải thuật,
không xác nhận điểm thi chính thức. Đề có **5 câu × 2
điểm**, tổng 10. Hai ý mỗi câu, mỗi ý 1 điểm tối đa.

Phạm vi được xác định từ đề mẫu 90 phút trong bộ
*Tests Python 2026*: số và vòng lặp, chuỗi, list,
dictionary, OOP. Các câu và dữ liệu ở đây đã được
thiết kế lại, không cần sử dụng đề mẫu để làm bài.

## Tổ chức lớp

- Phát đề và thư mục `submissions_de1/`; yêu cầu
  sinh viên dự đoán input/output trước khi viết.
- Sinh viên làm trên máy cá nhân, tự chấm bằng `--student`.
- Giảng viên kiểm năng lực giải thích và thử bổ sung
  một ca chưa có trong bộ công khai.
- `--reference` chỉ kiểm lời giải mẫu; không chấm
  bài sinh viên.

## Chấm thử

```bash
python review/mock-exams/de-90-phut-01/autograde_de1.py --reference
python review/mock-exams/de-90-phut-01/autograde_de1.py --student
```

Lời giải mẫu kỳ vọng `10.00/10.00` trên **78 ca**
công khai; starter TODO ban đầu `0.00/10.00`.
Máy chấm chia tỷ lệ trong từng ý (1 điểm/ý).
Điểm này không phản ánh độc lập học thuật hoặc
phân tích độ phức tạp của bài nộp.

**Hạn chế:** child process + timeout chỉ là kiểm tra
tiện dụng, không phải sandbox. Không dùng trên máy
có bí mật/quyền cao với bài nộp không tin cậy.
Khi chấm bài từ ngoài, phải có cô lập filesystem,
network, CPU/RAM và quyền truy cập, có quy trình
đánh giá thủ công khi tranh chấp.

Giữ bí mật thông tin người học và không commit
bài nộp riêng vào repo công khai. Nội dung tự luyện
không điều chỉnh `SYLLABUS.md` hay rubric chính thức.
