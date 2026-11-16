# Gợi ý ôn tập theo ba mức

Chỉ đọc gợi ý tiếp theo khi đã tự thử.

| Ý | Ý tưởng | Gợi ý cú pháp |
|---|---|---|
| 1a | Đếm chữ số thuộc 0,3,6,9 | `str(n)`, `char in "0369"` |
| 1b | Cộng dần các phân số | `for k in range(1,n+1)`, `1/k` |
| 2a | Kiểm chữ hoa ở từng ký tự | `char.isupper()` |
| 2b | Chuẩn hóa trước khi đối xứng | `isalnum()`, `casefold()`, `[::-1]` |
| 3a | Bỏ 0, chỉ đếm chẵn trước 0 | vòng for, `break`, kiểm sentinel |
| 3b | Đếm target, dừng ở 0 | `value == target` trước dừng |
| 4a | Validation trước khi tạo dict | `.strip()`, `type(year) is int` |
| 4b | Không sửa sách gốc | `seen=set()`, `book.copy()` |
| 5a | Thuộc tính, constructor và method | `class`, `__init__`, `self` |
| 5b | Tái sử dụng class từ file 5a | `from Cau5a import DienThoai` |

Kiểm tra rằng hàm thật sự `return`, đầu vào sai bị
từ chối bằng `ValueError`, dữ liệu nguồn không bị
thay đổi và class có đúng 5 thuộc tính. Nếu FAIL,
đọc thông báo từ `--student --verbose`, không sửa
file kiểm để làm tăng điểm giả.
