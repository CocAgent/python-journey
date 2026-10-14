# Mini Project Tuần 02: Thẻ sinh viên tự động 🪪

Chào mừng bạn đến với dự án thực hành của tuần này! Sau khi hoàn thành 3 bài tập cơ bản, chúng ta sẽ vận dụng các "món đồ" trong chiếc ba lô Python để tạo một chương trình in thẻ sinh viên chuyên nghiệp.

##  Mục tiêu
Vận dụng tổng hợp các kiến thức đã học trong tuần 02:
- Khai báo và đặt tên biến chuẩn `snake_case` (**ex01_variables**).
- Chuyển đổi kiểu dữ liệu từ chuỗi sang số để tính toán (**ex02_type_conversion**).
- Nhận input từ người dùng và trình bày kết quả bằng `f-string` (**ex03_input_calc**).

##  Yêu cầu
1. **Nhập dữ liệu**: Sử dụng hàm `input()` để lấy các thông tin: Họ tên, MSSV, Ngành học, và Năm nhập học.
2. **Xử lý dữ liệu**:
   - Ép kiểu (convert) Năm nhập học từ chuỗi sang số nguyên (`int`).
   - Tính toán **Năm tốt nghiệp** dự kiến (Năm nhập học + 4).
   - (Nâng cao) Sử dụng các phương thức chuỗi như `.upper()` cho họ tên hoặc `.title()` cho ngành học để dữ liệu trông chuyên nghiệp hơn.
3. **Hiển thị**: In ra chiếc thẻ có khung viền (border) đẹp mắt, sử dụng `f-string` để chèn các biến vào đúng vị trí.

##  Gợi ý kỹ thuật
- Đặt tên biến rõ ràng, dễ hiểu: `ho_ten`, `mssv`, `nam_nhap_hoc`, `nam_tot_nghiep`.
- Nhớ rằng dữ liệu từ `input()` luôn là kiểu `str`, bạn cần chuyển đổi trước khi làm phép toán cộng.
- Sử dụng `f-string` (`f"..."`) để code sạch và dễ đọc nhất khi in kết quả.

##  Ví dụ output
```
╔════════════════════════════╗
║    THẺ SINH VIÊN           ║
║----------------------------║
║ Họ tên:  Nguyễn Trung Tín  ║
║ MSSV:    2124110028        ║
║ Ngành:   Công nghệ TT      ║
║ Khóa:    2024 - 2027       ║
╚════════════════════════════╝
```

## Nộp bài
Hoàn thành code và commit lên GitHub với message: `"Complete mini-project week 02"`
