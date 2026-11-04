# Gợi ý triển khai lớp và tự chấm — Đề ôn tập 01

Bộ đề được viết lại từ **cấu trúc** của thư mục đề mẫu:
5 câu, 2 ý mỗi câu, 60 phút, có submissions và autograder.
Không sao chép nguyên văn đề mẫu và không sửa bất kỳ file
nào trong thư mục Drive nguồn.

## Phân bổ 10 điểm

| Câu | Chủ đề | Điểm |
|---|---|---|
| 1a, 1b | biến, kiểu, chuỗi | 2 |
| 2a, 2b | vòng lặp, điều kiện | 2 |
| 3a, 3b | list/methods/snapshot | 2 |
| 4a, 4b | tuple/index/operations | 2 |
| 5a, 5b | dictionary/frequency/filter | 2 |
| **Tổng** | 10 ý × 1 | **10** |

**Autograder:** chấm tỷ lệ ca đúng ở từng ý (tối đa 1 điểm),
tổng 10 điểm. 58 ca kiểm **công khai**, nên đây là
**tự đánh giá**, không phải chấm thi bảo mật hoặc chống gian lận.
Mỗi ca được chạy trong subprocess riêng, timeout 4 giây
để ngăn vòng lặp vô hạn thông thường; **không phải sandbox**.

## Nghiệm thu tài liệu

```bash
python review/mock-exams/de-01/autograde_de1.py --reference
python review/mock-exams/de-01/autograde_de1.py --student
```

Kỳ vọng `--reference` **10.00/10.00**,
`--student` ban đầu **0.00/10.00** vì tất cả TODO trống.
Nếu nộp bài riêng, giữ tên các hàm và file; tránh đổi
quy ước giao tiếp khiến grader không gọi được.

### Giới hạn an toàn

Không chạy mã không đáng tin trên máy chủ thật chỉ vì
đã có timeout. Đối với bài nộp từ ngoài, dùng container/VM
cô lập không mạng, filesystem tạm, giới hạn CPU/memory
và tài khoản không có quyền với dữ liệu thật.

Nên yêu cầu sinh viên **giải thích thuật toán, chạy test
mới chưa công bố và mô tả một bug** để chấm năng lực,
không chỉ nhìn điểm tự động công khai.

Không thay `SYLLABUS.md`, `FINAL_PROJECT.md`,
rubric chính thức hoặc điểm các tuần học.
