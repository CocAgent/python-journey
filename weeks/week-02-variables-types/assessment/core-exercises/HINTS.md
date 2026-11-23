# Gợi ý theo đúng TODO — ba bài exercises Week 02

Chỉ đọc gợi ý sau khi đã tự thử. Mỗi dòng dưới đây tương ứng **một TODO bắt buộc đang có**, không phải câu hỏi mới.

| Bài / TODO | Gợi ý |
|---|---|
| ex01 TODO 1 | Tạo `ten` (str), `tuoi` (int), `diem_tb` (float), `dang_hoc` (bool); in giá trị **và `type()` từng biến** |
| ex01 TODO 2 | Gán `a=10`, `b=20`. Python cho phép đổi chỗ bằng `a, b = b, a` mà không cần biến tạm |
| ex01 TODO 3 | Bắt đầu `x=100`. Chọn các số tăng/giảm đơn giản để thử `+=`, `-=`, `*=`, `//=` và in `x` sau mỗi bước |
| ex02 TODO 1 | `so_text="42"` là chuỗi; hãy dùng `int(so_text)` trước khi cộng 8 |
| ex02 TODO 2 | `int(3.14159)` là 3, không phải làm tròn lên 4 |
| ex02 TODO 3 | `bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])` lần lượt là False, True, False, True, False, True |
| ex02 TODO 4 | Nhập **chiều cao (m) rồi cân nặng (kg)**; đổi sang `float`; BMI = kg / m², in một chữ số thập phân |
| ex03 TODO 1 | Nhập **hai số**, dùng 4 phép toán `+`, `-`, `*`, `/` và in từng kết quả |
| ex03 TODO 2 | Nhập **bán kính**, diện tích = `3.14159*r*r`, chu vi = `2*3.14159*r` |
| ex03 TODO 3 | Nhập **giá gốc** và **phần trăm giảm**; giá sau giảm = `gia_goc*(1-phan_tram/100)` |

## Khi máy báo RETRY

1. Đối chiếu **đúng TODO** và file mà máy in ra.
2. Tìm `SyntaxError`, `EOFError`, sai định dạng số hoặc dữ liệu trống.
3. Chạy file riêng, ghi stdout, so sánh với kết quả toán học.
4. Chạy lại `--student --verbose` sau khi lưu mã. Không sửa grader hoặc rubric để tạo PASS giả.
5. Nếu đã đúng theo đề nhưng checker vẫn không nhận diện, giữ mã + output để giảng viên xem.

Các TODO ghi **(Thử thách)** không được chấm. `practice/` và `mini-project/` cũng không nằm trong điểm này.
