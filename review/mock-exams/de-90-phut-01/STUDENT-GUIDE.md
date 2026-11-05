# Hướng dẫn sinh viên — thực hành 90 phút

Mở [đề 90 phút](DE-90-PHUT.md) trước và đọc yêu cầu từng hàm.
Không mở thư mục đáp án `solutions_de1/` ngay.

## Cần biết trước khi làm đề

- **File chạy được nằm trên GitHub:** `submissions_de1/Cau1a.py` đến
  `Cau5b.py`. Các Google Docs trong Drive chỉ để đọc và sao chép nội dung,
  không phải script Python thực thi trực tiếp.
- **Tải mã:** vào https://github.com/CocAgent/python-journey,
  chọn **Code → Download ZIP**, giải nén và mở terminal trong thư mục gốc;
  hoặc `git clone https://github.com/CocAgent/python-journey.git`.
- **Kiến thức OOP:** câu 5 cần kiến thức lớp và đối tượng (được học
  chuyên sâu tại Week 14). Sinh viên mới học đến Week 11 có thể
  hoàn thành Câu 1–4 rồi học ví dụ có hướng dẫn trước khi làm Câu 5.
- **Kết quả tự chấm:** chạy `--student` mới kiểm mã của sinh viên;
  `--reference` chỉ kiểm lời giải mẫu và không dùng để chấm bài nộp.

## Gợi ý phân phối thời gian

| Thời lượng | Công việc |
|---|---|
| 10 phút | Đọc đề, xác định kiểu input/output và dữ liệu sai |
| 20 phút | Câu 1 và Câu 2: vòng lặp, chuỗi |
| 20 phút | Câu 3 và Câu 4: list, dictionary |
| 25 phút | Câu 5: class, constructor, method và 2 object |
| 15 phút | Chạy kiểm, sửa FAIL, kiểm lại và ghi minh chứng |

Chỉ là gợi ý ôn tập; sinh viên có thể thay đổi thứ tự.

## Quy trình

1. Tải repository:
   https://github.com/CocAgent/python-journey
   hoặc clone `git clone https://github.com/CocAgent/python-journey.git`.
2. Mở terminal tại thư mục gốc `python-journey`, kiểm
   `python --version` (>=3.12).
3. Tìm `review/mock-exams/de-90-phut-01/submissions_de1/`;
   thực hiện TODO trong 10 file `Cau1a.py`…`Cau5b.py`.
4. Với mỗi hàm, dự đoán 1 input thường, 1 input biên,
   1 input sai trước khi chạy.
5. Chạy `python review/mock-exams/de-90-phut-01/autograde_de1.py --student`.
   Có thể thêm `--verbose` khi cần chẩn đoán.
6. Sửa lỗi trong starter; không sửa grader/test hoặc
   đổi tên function/class.
7. Chỉ khi tự làm, mới mở `solutions_de1/` và thử
   `--reference`. Reference PASS không phải điểm sinh viên.

## Nộp bài

Nộp 10 file Python trong `submissions_de1/` hoặc ZIP
thư mục đó theo hướng dẫn lớp; không nộp đáp án, file
`__pycache__`, token và dữ liệu cá nhân nhạy cảm.
Chỉ thực thi mã mình tự viết hoặc đã tin cậy.

## Báo cáo ngắn

```text
Ý bài:
Dự đoán:
Kết quả thực tế:
Một input biên / sai:
Bug phát hiện:
Cách sửa:
Lệnh kiểm bài sinh viên và điểm tự kiểm:
Điều tôi có thể giải thích với giảng viên:
```
