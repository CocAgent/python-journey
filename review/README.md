# Ôn tập Python Journey — Week 01–11

Bộ ôn tập **tự chọn**, dành cho sinh viên cần củng cố trước khi học
[Week 12 — pytest](../weeks/week-12-testing-pytest/) hoặc chuẩn bị
dự án tiếp theo. **Không thay nội dung chính, thang điểm, hoặc rubric**
trong [SYLLABUS.md](../SYLLABUS.md) và
[FINAL_PROJECT.md](../FINAL_PROJECT.md).

Nguồn ôn tập: **các tuần trong chính repository Python Journey**.
Không có tài liệu nào được đọc từ phiên Chrome Remote Desktop;
thư mục này **không chứa ID phiên, thông tin đăng nhập, hoặc dữ liệu
lấy từ màn hình/máy tính từ xa**.

## Học theo thứ tự

1. [Kế hoạch ôn tập theo bốn buổi](STUDY-PLAN.md) — xác định chỗ
   cần ôn và liên kết trực tiếp bài học từng tuần.
2. [16 câu dự đoán nhanh](QUICK-CHECK.md) — **trả lời trước khi**
   mở [đáp án giải thích](ANSWER-KEY.md).
3. [Ba bài thực hành tích hợp](practice/README.md) — tự hoàn thành
   hàm trong `practice/starter/`, không chép solutions.
4. Chạy máy kiểm để nhận PASS/FAIL **trên code của chính sinh viên**.
5. Ghi [bằng chứng học tập](EVIDENCE-TEMPLATE.md) và một lỗi đã sửa.

## Bài tích hợp

| Lab | Bài toán | Kiến thức |
|---|---|---|
| 01 — Gradebook | Tổng hợp danh sách học viên và điểm | Week 02–08: string, list, dict, set, vòng lặp, hàm |
| 02 — JSON Report | Lưu, đọc và xác thực báo cáo | Week 10: `pathlib`, JSON, UTF-8, schema |
| 03 — Debug & Exceptions | Khoảng cách đúng hai chiều, audit nhập điểm | Week 11: bug logic, `ValueError`, `finally` |

**Không sử dụng mạng, không đụng dữ liệu thật.** Bộ kiểm sử dụng
thư mục tạm để tạo file JSON và tự dọn sau khi hoàn thành.

## Chạy từ thư mục gốc `python-journey`

```bash
python --version

# Kiểm code sinh viên (TODO chưa hoàn thành => FAIL đúng thiết kế)
python review/practice/checks/check_review.py --starter

# Kiểm lời giải tham khảo, chỉ dùng sau khi tự làm
python review/practice/checks/check_review.py --solutions
```

Trên Windows, nếu `python` không nhận, thử `py -3` theo
[SETUP.md](../SETUP.md). Khi xong, `--starter` cần báo
`Review student: PASS (3/3)`. **Reference PASS không
chứng minh bài sinh viên đã hoàn thành.**

Nếu đang thao tác trên một máy qua Chrome Remote Desktop,
xem [hướng dẫn lấy folder bằng GitHub an toàn](REMOTE-DESKTOP-SETUP.md).
Không cần cấp quyền điều khiển máy cho người khác để làm bài.

## Tránh nhầm với bộ kiểm maintainer

- `review/practice/checks/check_review.py` là self-check cho
  bài tự làm, **không cần pytest**.
- CI của repository chỉ kiểm ví dụ/reference và bảo đảm starter
  chưa làm không thể báo PASS giả.
- Thang điểm/đầu ra chính nằm trong các tài liệu canonical của khóa,
  không phải trong thư mục ôn tập này.

Vòng học: **Learn → Build → Test → Debug → Improve → Commit → Prove**.

## Đề ôn tập tổng hợp 90 phút và bài luyện khởi động 60 phút

**Bộ đề 90 phút khuyến nghị:** [Đề tổng hợp 01 — 5 câu × 2 điểm](mock-exams/de-90-phut-01/README.md),
gồm số và vòng lặp, xử lý chuỗi, list với tín hiệu dừng, dictionary
quản lý sách và **OOP với lớp DienThoai**. Có 10 starter, 10 đáp án
riêng và 78 ca kiểm thử công khai; phù hợp ôn tập trước bài thực hành.

**Bộ 60 phút tự chọn:** [Đề luyện nhanh cơ bản](mock-exams/de-01/README.md)
dùng để củng cố trước khi thử đề tổng hợp dài hơn.

## Đề ôn tập theo mẫu 60 phút, có chấm tự động

Đã bổ sung [**Đề 01 — 5 câu / 10 ý / 60 phút**](mock-exams/de-01/README.md)
dựa trên cấu trúc bộ đề CBPYTHON người học đang tham khảo.
Bộ đề mới có **10 file starter**, 10 lời giải tách biệt, các ví dụ
có giải thích, **58 ca kiểm tự động công khai** và hướng dẫn nộp bài.
Luyện bằng `python review/mock-exams/de-01/autograde_de1.py --student`.
Điểm tự chấm không thay rubric chính thức của khóa học.
