# Week 07 — Functions: đoán giá trị trả về → chạy → debug → tự viết hàm mới

Sổ tay cho người học đã hoàn thành Week 01–06. Tuần này chúng ta không
chỉ quan sát **đầu ra được in**, mà còn kiểm tra **dữ liệu trả về từ hàm**,
tính độc lập của các lời gọi và cách dùng lại những hàm nhỏ.

Python >=3.12; không cần Internet, LLM, `pip install` hay `pytest`.
Đây là phần luyện thêm, không thay 4 bài gốc hoặc Utility Toolkit.

## Bước 0 — chạy từ đúng thư mục

Mở terminal tại thư mục gốc `python-journey/`:

```bash
python --version
python weeks/week-07-functions/examples/06_predict_return_and_default.py
python weeks/week-07-functions/examples/07_scope_and_decomposition_trace.py
python weeks/week-07-functions/examples/08_type_hints_and_decision.py
```

Nếu Windows không nhận `python`, thử `py -3`.

Với mỗi ví dụ: **che đáp án → dự đoán → chạy → đối chiếu →
giải thích → thay một dữ liệu → làm lab tương tự → tự kiểm**.
Lệnh mẫu cho lab nằm ở [practice/README.md](practice/README.md).

## Ví dụ 06 — Hàm `print()` khác hàm `return` như thế nào?

Hãy dự đoán kết quả của hai hàm:

```python
def show_price(price: int, quantity: int) -> None:
    print(f"show_price in: {price * quantity:,} VND")

def calculate_price(price: int, quantity: int, fee: int = 0) -> int:
    return price * quantity + fee

printed_result = show_price(12_000, 2)
subtotal = calculate_price(12_000, 2)
```

| Biểu thức | Dự đoán của em | Kết quả |
|---|---|---|
| `show_price(12_000, 2)` | … | in `24,000 VND`, **trả về None** |
| `printed_result` | … | `None` |
| `subtotal` | … | số nguyên `24000` |
| `calculate_price(12_000, 2, 5_000)` | … | `29000` |
| `first_positive([-2,0,7,9])` | … | `7` (return sớm) |
| `first_positive([-2,0])` | … | `None` |

**Giải thích:** `print` chỉ ghi thông tin ra terminal. Hàm
không có `return` sẽ trả `None` cho caller; không thể dùng
đầu ra `print` làm số để tính tiếp. `return` đưa kết quả
về nơi gọi và **kết thúc lần gọi hàm đó** ngay khi chạy.
`fee=0` là **tham số mặc định**: caller có thể bỏ qua hoặc
cung cấp fee riêng.

**Tự thử:** đổi `quantity` từ 2 thành 3, đoán cả giá
trước và sau phí. Đổi `first_positive` thành list rỗng.
Không sửa lời giải ở `practice/solutions/` khi thử.

**Lab tương tự 01:** tự viết `calculate_total(price, quantity,
shipping=0)` để **return số VND**, kiểm số lượng và phí không
âm; chương trình phải từ chối `quantity=0`. Xem
[Lab 01](practice/README.md).

## Ví dụ 07 — Chia một bài toán: validate → calculate → format

```text
price=20_000, quantity=2, shipping=5_000
                   ↓
   validate_order(price, quantity)
                   ↓
   subtotal(price, quantity) = 40_000
                   ↓
   with_shipping(40_000, 5_000) = 45_000
                   ↓
  build_receipt() -> "Thanh toán: 45,000 VND"
                   ↓
  main() quyết định print chuỗi đó
```

Code gốc nằm trong `examples/07_scope_and_decomposition_trace.py`.

| Input | Giá trị trả về cần quan sát |
|---|---|
| `build_receipt(20_000,2,5_000)` | `Thanh toán: 45,000 VND` |
| `build_receipt(20_000,0)` | `Đơn hàng không hợp lệ` |
| `build_receipt(20_000,2,-1)` | `Đơn hàng không hợp lệ` |
| `input_price` trước/sau | vẫn là `20000` |

**Vì sao tách hàm?** Có thể kiểm riêng `validate_order`,
`subtotal` và `with_shipping`; khi lỗi, không phải dò
một khối code dài. Biến `amount`, `final` trong hàm
là **local** và không vô tình thay đổi `input_price`
ở caller. Thay dữ liệu qua **parameter/return**, không
dùng một global mutable ẩn.

**Tự thử:** đổi shipping thành 0 và đoán giá sau cùng.
Đổi quantity thành -1 để kiểm nhánh từ chối. Vẽ đường
đi của dữ liệu đến chuỗi cuối cùng.

**Lab tương tự 02:** thay tính phí bằng tính giảm giá. Tự
định nghĩa `is_valid_order`, `calculate_subtotal` và
`calculate_final` có tham số mặc định `percent=0`.
Làm tròn xuống đến số nguyên VND là **quy ước của bài học**,
không phải quy tắc hóa đơn/tài chính sản xuất.

**Lab tương tự 03:** các hàm `add_note`, `count_notes`,
`search_notes` phải nhận list ghi chú **qua parameter**.
`add_note` có quyền sửa list caller vì đó là contract
của hàm; hai hàm đọc/tìm thì không được sửa nó.
Tránh một biến `NOTES` global dùng chung cho mọi người.

## Ví dụ 08 — Type hints KHÔNG tự kiểm kiểu lúc chạy

```python
def repeat_text(text: str, times: int) -> str:
    return text * times

repeat_text("Py", 2)     # "PyPy"
repeat_text("Py", True)  # "Py" vẫn chạy ở runtime
```

`bool` trong Python là một nhánh của `int`, vì thế
`"Py" * True` có thể chạy. **Annotation `times: int`
không chặn input sai**. Type checkers có thể cảnh báo,
nhưng Python không tự thực hiện bước validation.

Khi dữ liệu ảnh hưởng một quyết định, kiểm tường minh:

```python
def is_valid_minutes(minutes: object) -> bool:
    return (
        isinstance(minutes, int)
        and not isinstance(minutes, bool)
        and 0 <= minutes <= 60
    )
```

Tài liệu dùng `type(value) is int` trong lời giải lab để minh
họa cách từ chối `True` rõ ràng; với đối tượng phức tạp và
kế thừa kiểu, quy tắc runtime cần được thiết kế theo contract.

**Decision function mẫu (CHỈ ĐỂ HỌC, không phải VuaCóc production):**

```python
def decide_study_action(minutes: int, confused: bool) -> str:
    if minutes == 0:
        return "stop"
    if confused:
        return "review"
    return "practice"
```

| minutes | confused | action dự đoán |
|---:|---|---|
| 0 | True | `stop` — quy tắc hết giờ ưu tiên |
| 15 | True | `review` |
| 15 | False | `practice` |

**Quan trọng:** hàm `decide_study_action` demo ở trên
**chưa có runtime guard**. Nó chỉ minh họa thứ tự nhánh.
Ở bài tự luyện, em phải **viết validation trước decision**
để từ chối `minutes=61`, `minutes=True` và
`confused="False"`.

**Lab tương tự 04:** viết `choose_study_action` với
3 giá trị action trên. Input giống nhau phải luôn
cho ra kết quả giống nhau (deterministic); không tự
gọi mạng, thay đổi state hay “học” một chiến lược.

## Khi gặp lỗi, hãy xác định tầng gây ra lỗi

| Hiện tượng | Nguyên nhân cần kiểm | Cách sửa |
|---|---|---|
| Hàm in đúng nhưng caller nhận `None` | dùng `print` thay `return` | trả giá trị bằng `return` |
| Gọi hàm bị `TypeError` | thiếu argument bắt buộc, kiểu/toán tử không hợp lệ | xem signature và input |
| Hàm chỉ chạy nhánh đầu | `return` kết thúc lần gọi | kiểm lại thứ tự điều kiện |
| Kết quả thay đổi theo lượt gọi trước | hàm dùng global state ẩn | truyền dữ liệu qua parameter |
| Type hints khai `int` nhưng nhận `True` | annotation không kiểm runtime | thêm validation tường minh |
| Hóa đơn đúng nhưng copy logic ở nhiều hàm | thiếu decomposition | cho hàm lớn gọi hàm nhỏ |
| List ghi chú không đổi | hàm sửa bản copy thay vì list caller | đọc contract có yêu cầu mutation? |
| Chạy file thấy `NotImplementedError` | starter còn TODO | tự viết code, không sửa checker |

## Tự kiểm bằng hàm thật, không chỉ nhìn terminal

Từ gốc `python-journey/`:

```bash
python weeks/week-07-functions/practice/checks/check_practice.py --starter
```

Trước khi làm TODO, `FAIL (0/4)` là **đúng thiết kế**.
Checker sẽ **import và gọi trực tiếp hàm**, thử nhiều giá trị
thường/biên/sai, kiểm `return` và phân biệt nơi hàm
có thể thay đổi dữ liệu. Một bài chỉ `print` kết quả
mong đợi không đủ để PASS.

Sau khi tự làm, mới mở lời giải và kiểm riêng:

```bash
python weeks/week-07-functions/practice/checks/check_practice.py --solutions
```

**PASS của solutions không phải điểm của bài sinh viên.**

## Bài biến đổi tự chọn và bằng chứng học tập

Chọn một miền mới như **quản lý sách mượn**, **tính vé
tham quan** hoặc **chọn hành động cho Bot mô phỏng offline**.
Thiết kế ít nhất 2 hàm nhỏ với contract và một hàm ghép.
Với Bot, chỉ mô phỏng quyết định thuần Python:
không gọi đây là agent tự chủ hoặc contract production VuaCóc.

Ghi ngắn vào nhật ký:

```text
Tên hàm và contract (input -> output):
Dự đoán kết quả:
Kết quả thật:
Dữ liệu sai và cách từ chối:
Một lỗi phát hiện:
Caller có nhận giá trị hay chỉ thấy print?
Hàm có phụ thuộc global không?
Tôi đã thử dữ liệu mới nào?
```

Tiếp tục với [Personal Utility Toolkit](mini-project/README.md)
hoặc [Function Bot course-local](../../projects/vuacoc-bot-journey/milestones/w07-function-bot.md)
khi đã hiểu `return` và decomposition. Không thay bài
bắt buộc, syllabus hoặc rubric Week 07.
