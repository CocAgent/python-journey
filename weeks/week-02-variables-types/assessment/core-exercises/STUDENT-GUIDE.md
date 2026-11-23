# Hướng dẫn sinh viên tự chấm ba bài tập có sẵn — Week 02

1. Tải toàn bộ [Python Journey](https://github.com/CocAgent/python-journey) bằng Git hoặc Code → Download ZIP. Mở thư mục gốc trong VS Code. Kiểm tra `python --version` (Python 3.12+); Windows có thể dùng `py`.
2. Đọc [README Week 02](../../README.md), `notes.md` và chính ba file `exercises/ex01_variables.py`, `ex02_type_conversion.py`, `ex03_input_calc.py`. **Sửa TODO ngay trong các file này**, không tạo bài thi mới.
3. Tự viết và chạy từng file, lưu `Ctrl+S`. Đối với bài 02: nhập chiều cao (m) rồi cân nặng (kg); bài 03: nhập hai số, bán kính, giá gốc và % giảm theo thứ tự TODO. Những thử thách nếu có có thể đọc thêm input phía sau.
4. Chạy máy chấm từ **gốc repository**:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student
```

5. Đọc `PASS` hoặc `RETRY` theo tên TODO gốc, xem điểm và lý do. Khi `RETRY`, kiểm tra lỗi cú pháp, input, kiểu dữ liệu, output, phép toán; sửa bài mình viết rồi chạy lại. Mã thoát `1` nghĩa là còn tiêu chí chưa được nhận diện, không phải lỗi cài đặt.
6. Lưu báo cáo JSON để theo dõi tiến bộ:

```bash
python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student --json-out .learner-output/week02-core.json
```

7. Điền [phiếu minh chứng](EVIDENCE-TEMPLATE.md): một input bình thường, một trường hợp biên, lỗi đã sửa, output thực tế, điểm máy/10 và một đoạn giải thích vì sao đúng.

## Điểm và phạm vi công bằng

Chỉ các TODO bắt buộc của ba bài gốc được tính điểm. TODO có ghi **(Thử thách)** là tự chọn, **không trừ điểm**. Mini-project `mini-project/starter.py` có code chạy sẵn; kết quả PASS của nó **không chứng minh sinh viên đã tự làm**, nên chỉ kiểm riêng qua demo/giải thích. Bài lab `practice/starter/` đã có checker khác, không cộng trùng điểm.

Khi cách giải của em đúng nhưng chấm máy báo `RETRY`, hãy nộp mã và kết quả chạy cho giảng viên phản biện. Máy dựa trên dấu hiệu AST/stdout và dữ liệu thử, không thể xác nhận mọi lời giải hợp lệ. **Đừng đổi grader/rubric hoặc chép fixture để lấy PASS giả.**

## Bảo mật

Chỉ chạy mã em tự viết hoặc đã kiểm tra tin cậy; subprocess/timeout không cách ly an toàn mã độc. Không chấm bài từ người lạ trên VPS hoặc máy chứa dữ liệu nhạy cảm.
