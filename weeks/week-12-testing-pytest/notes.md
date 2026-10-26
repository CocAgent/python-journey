# Bài giảng tuần 12 — Từ chạy thử đến kiểm thử có bằng chứng

## 1. Vì sao cần test?

Giả sử một bot phải đi về phía mục tiêu:

- ở vị trí 1, mục tiêu 4 → `"right"`;
- ở vị trí 4, mục tiêu 4 → `"wait"`;
- ở vị trí 4, mục tiêu 1 → `"left"`.

Nếu chỉ chạy thử trường hợp đầu tiên, chương trình **luôn** trả về `"right"` vẫn có vẻ đúng. Test cần kiểm tra các hành vi khác nhau.

**Test** là một chương trình nhỏ so sánh kết quả **thực tế** và kết quả **mong đợi**.

## 2. pytest tìm test như thế nào?

Trong các file bắt đầu bằng `test_` hoặc kết thúc bằng `_test.py`, pytest tìm hàm `test_*`. Ví dụ:

```python
def cong(a: int, b: int) -> int:
    return a + b


def test_cong_hai_so_duong() -> None:
    # Đây là phép kiểm tra có kết quả cụ thể: 2 + 3 phải bằng 5.
    assert cong(2, 3) == 5
```

Chạy ở thư mục dự án (sau khi cài `pytest`):

```bash
python -m pytest duong_dan_toi_file_test.py -q
```

`-q` hiển thị kết quả gọn. `python -m pytest` giúp sử dụng `pytest` trong đúng môi trường Python.

## 3. Ba bước: Chuẩn bị → Thực hiện → Kiểm tra

```python
from decision import choose_action


def test_bot_di_dung_huong() -> None:
    # Arrange — chuẩn bị dữ liệu đầu vào.
    position, goal = 1, 4

    # Act — gọi hành vi cần kiểm tra.
    action = choose_action(position, goal)

    # Assert — kết quả mong đợi phải cụ thể.
    assert action == "right"
```

Ví dụ trên nằm trong bài giảng: file bài tập của sinh viên cần **tự viết** các trường hợp của mình.

### Sai lầm thường gặp: phép kiểm tra quá yếu

```python
# Chưa đủ: nếu bot trả "left" khi phải đi "right", phép kiểm tra này vẫn PASS.
assert action in {"left", "right", "wait"}

# Mạnh hơn: kiểm tra đúng quyết định trong tình huống hiện tại.
assert action == "right"
```

Một test tốt phải có khả năng **thất bại khi chương trình có hành vi sai**.

## 4. Bốn nhóm tình huống cần biết

| Nhóm | Ví dụ | Điều cần xác nhận |
|---|---|---|
| Bình thường (normal) | Vị trí 1 → mục tiêu 4 | Đi phải |
| Biên (edge) | Đang ở đúng mục tiêu | Đứng yên |
| Không hợp lệ (invalid) | Số lượt bằng 0 | Báo `ValueError` |
| Hồi quy (regression) | Vị trí 4 → mục tiêu 1 | Đi trái, không lặp lại lỗi cũ |

Với đầu vào sai, ta thường cần kiểm tra **exception**, không phải một kết quả trả về thông thường:

```python
import pytest

from decision import validate_turn


def test_luot_khong_hop_le() -> None:
    # Lượt chơi bằng 0 trái với quy tắc "lượt bắt đầu từ 1".
    with pytest.raises(ValueError):
        validate_turn(0)
```

Nếu chương trình im lặng chấp nhận 0, test phải FAIL.

## 5. Một test chạy với nhiều bộ dữ liệu

Không cần sao chép cùng một hàm test ba lần. `@pytest.mark.parametrize` chạy test trên từng hàng dữ liệu:

```python
import pytest


@pytest.mark.parametrize(
    ("a", "b", "ket_qua"),
    [(2, 3, 5), (0, 0, 0), (-2, 2, 0)],
)
def test_cong_nhieu_truong_hop(a: int, b: int, ket_qua: int) -> None:
    # Mỗi hàng là một tình huống độc lập, có kết quả kỳ vọng rõ.
    assert a + b == ket_qua
```

Xem [ví dụ tính thành tiền](examples/test_order_total.py) để thấy thêm `pytest.raises`.

## 6. Hiểu vì sao một test thất bại

Khi gặp `FAILED`, đọc theo thứ tự:

1. **Tên test**: hành vi nào đang được kiểm chứng?
2. **Expected và actual**: kết quả mong đợi khác thực tế ở đâu?
3. **Traceback**: dòng nào xảy ra lỗi?
4. **Đầu vào nhỏ nhất**: bạn tái hiện lại lỗi như thế nào?
5. **Nguyên nhân → sửa → chạy lại**: thay đổi ít nhất có thể, rồi kiểm chứng.

Đừng sửa `assert` cho khớp với hành vi sai khi chưa kiểm tra yêu cầu.

## 7. Vì sao test cũng có thể sai?

Test là code nên cũng có lỗi. Ví dụ, kiểm tra `action in LOCAL_ACTIONS` chỉ xác nhận hành động hợp lệ về **tên**, không xác nhận hướng di chuyển đúng.

Cách tự kiểm chứng rất trực quan:

- chạy test với chương trình đúng → phải PASS;
- thử chương trình cố ý sai một quyết định → ít nhất một test phải FAIL;
- nếu vẫn PASS → bộ test chưa bảo vệ đúng hành vi đó.

Công cụ [check_student_tests.py](checks/check_student_tests.py) tự tạo bốn lỗi có chủ đích để minh họa phương pháp này. Công cụ không sửa file của sinh viên.

## 8. Test độc lập và file tạm

Không để test sau phụ thuộc vào thứ tự test trước. Khi kiểm tra thao tác lưu file, dùng fixture `tmp_path`:

```python
def test_luu_ghi_chu(tmp_path) -> None:
    tep = tmp_path / "ghi_chu.txt"
    tep.write_text("xin chào", encoding="utf-8")
    assert tep.read_text(encoding="utf-8") == "xin chào"
```

`tmp_path` giúp mỗi test làm việc trên thư mục tạm riêng, không ghi dữ liệu vào repository.

## 9. Những gì **chưa cần** ở tuần 12

Chưa học mocking nâng cao, property-based testing chuyên sâu, kiểm thử API tích hợp hoặc đo coverage theo phần trăm. Trước hết, hãy viết được một test rõ ràng, biết nó phát hiện lỗi gì và có thể giải thích vì sao.

## 10. Công cụ AI dùng đúng cách

Có thể hỏi: *"Tôi đã viết test cho bot đi phải. Hãy gợi ý hai trường hợp biên nhưng đừng viết lời giải."* Sau đó tự bổ sung phép kiểm tra và thử lỗi. Không dùng AI tạo ra toàn bộ test mà không đọc, không chạy hoặc không hiểu.

**Vòng lặp học tập:** Dự đoán → Viết test → Chạy → Đọc lỗi → Sửa → Thử lại.
