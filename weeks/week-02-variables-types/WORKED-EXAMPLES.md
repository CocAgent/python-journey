# Week 02 — Dự đoán trước · chạy thử · tìm lỗi · làm bài tương tự

Mục tiêu: học được **vì sao Python cho ra kết quả**, thay vì chỉ sao chép
một đoạn code. Tài liệu dành cho người mới học, dùng Python >=3.12,
không có phụ thuộc bên ngoài, không gọi mạng.

## Bước 0 — Chuẩn bị máy

Mở terminal tại thư mục gốc `python-journey` (thư mục chứa `weeks/`).
Nếu chưa cài Python, dùng [SETUP.md](../../SETUP.md).

```bash
python --version
python weeks/week-02-variables-types/examples/04_predict_types.py
python weeks/week-02-variables-types/examples/05_conversion_trace.py
python weeks/week-02-variables-types/examples/06_fstring_ticket.py
```

Nếu Windows dùng `py -3` thay vì `python`, hãy thay tương ứng
trong các lệnh. **Không nhập dấu `$` hoặc `>` trước câu lệnh.**

## Cách học một ví dụ

1. Đọc đoạn gán biến và tự **dự đoán output**, chưa chạy.
2. Ghi câu trả lời: giá trị nào là `str`, `int`, `float`, `bool`?
3. Chạy script và so kết quả với dự đoán.
4. Đọc lời giải thích: Python thực hiện điều gì ở mỗi dòng?
5. Thay **một** đầu vào, dự đoán kết quả mới, thử chạy.
6. Chuyển sang bài **tương tự nhưng khác dữ liệu** ở `practice/starter`.

**Quy tắc:** lỗi không phải điểm trừ khi đang học; phải mô tả được
nguyên nhân và cách kiểm chứng sửa lỗi. Không sửa `solutions/` để
làm cho bài mình PASS.

## Ví dụ 04 — Vì sao "12" + "3" không bằng 15?

Trước khi chạy, hãy điền cột **Dự đoán của em** trên giấy:

| Biểu thức | Dự đoán của em | Kết quả để đối chiếu |
|---|---|---|
| `"12" + "3"` | ... | `"123"` (ghép chuỗi) |
| `12 + 3` | ... | `15` (cộng số) |
| `type("12").__name__` | ... | `str` |
| `type(12).__name__` | ... | `int` |
| `bool("False")` | ... | `True` vì chuỗi có ký tự |
| `bool("")` | ... | `False` vì chuỗi rỗng |
| `5 / 2` | ... | `2.5` |
| `5 // 2` | ... | `2` |

```bash
python weeks/week-02-variables-types/examples/04_predict_types.py
```

**Giải thích dòng quan trọng:**

```python
number_text = "12"      # str: dữ liệu văn bản
number = 12             # int: dữ liệu số
print(number_text + "3")  # "123" — không phải phép cộng số
print(number + 3)         # 15
```

`bool("False")` **không đọc nghĩa tiếng Anh** của từ False;
nó chỉ xem chuỗi có rỗng hay không. `bool` thật dùng `True` hoặc
`False` không có dấu nháy.

**Biến đổi tương tự:** thử `"7" + "5"`, sau đó `int("7") + 5`.
Giải thích vì sao kết quả khác nhau. Dùng [Lab 01](practice/README.md)
để tự chuyển tuổi dạng text thành số.

## Ví dụ 05 — Vì sao phải chuyển kiểu trước khi tính tiền?

```text
quantity_text = "3" (str)
           ↓ .isdigit() — có gồm chữ số?
           ↓ int("3")
quantity = 3 (int)
           ↓ quantity * 25_000
total = 75000 (int)
           ↓ f"{total:,}"
"75,000" để hiển thị
```

```bash
python weeks/week-02-variables-types/examples/05_conversion_trace.py
```

**Output đáng chú ý:**

```text
Input đang là: str
Đầu vào: '3'
Số lượng đã đổi kiểu: int
Thành tiền: 75,000 VND
Ví dụ sai 'ba': không chuyển được sang int
Ví dụ sai '0': số lượng phải lớn hơn 0
```

`str` và `int` là kiểu dữ liệu; `isdigit()` là kiểm tra
đơn giản cho văn bản chữ số. `int("ba")` sẽ tạo `ValueError`
nếu cố chuyển trực tiếp. Với số lượng, `0` vẫn chuyển được thành
số nguyên nhưng **không phải số lượng mua hợp lệ** trong bài này.

**Tự thử có kiểm soát:** đổi `quantity_text` thành `"5"`
(rồi dự đoán `125,000 VND`), đổi thành `"0"` (không tính
thành tiền), cuối cùng `"ba"` (từ chối trước khi `int()`).
Hàm `if` ở đây chỉ là ví dụ giới thiệu; Week03 mới học
đầy đủ điều kiện.

**Biến đổi tương tự:** [Lab 02](practice/README.md) dùng cùng
ý tưởng nhưng yêu cầu sinh viên tự viết, không copy lệnh print.
VND được giữ bằng **số nguyên đồng** để tránh lỗi làm tròn
không cần thiết.

## Ví dụ 06 — Từ tên và số vé đến phiếu giá

```python
name_text = "  An  "    # có khoảng trắng đầu/cuối
ticket_count_text = "2" # str từ input giả lập
unit_price_vnd = 12_000  # int
name = name_text.strip() # "An"
ticket_count = int(ticket_count_text) # 2
total = ticket_count * unit_price_vnd  # 24000
print(f"Vé của {name}: {ticket_count} × {unit_price_vnd:,} = {total:,} VND")
```

```bash
python weeks/week-02-variables-types/examples/06_fstring_ticket.py
```

Các dòng cuối cần thấy:

```text
Vé của An: 2 × 12,000 = 24,000 VND
Tình huống sai: 'hai' không phải số vé hợp lệ
```

`f"...{total:,}..."` chỉ định dạng **hiển thị** có dấu phân
cách hàng nghìn, không thay đổi `total` trong bộ nhớ.
Ví dụ này dùng biến sẵn có; bài tương tự mới yêu cầu nhập
từ bàn phím bằng `input()`.

**Tự thử:** đổi `ticket_count_text` thành `"3"` (→ 36,000 VND).
Nếu đổi thành `"hai"`, nhánh thành công không được chạy.

## Khi chương trình báo lỗi: đọc cho đúng loại

Đây là **ví dụ lỗi để nhận biết** — không chép nguyên các dòng sai
vào file bài nộp rồi mong chúng chạy thành công.

| Câu lệnh sai / input lỗi | Điều xảy ra | Cách xử lý ở Week02 |
|---|---|---|
| `"12" + 3` | `TypeError`: không ghép str với int | `int("12") + 3` để tính số |
| `int("ba")` | `ValueError`: không đổi được text | kiểm input text trước khi chuyển |
| `"7" * 3` | `"777"`, không phải 21 | `int("7") * 3` |
| `bool("False")` | `True`, không phải False | phân biệt chuỗi và bool |
| `int("3.5")` | `ValueError` | dùng `float("3.5")` nếu số thập phân hợp lệ |
| `input()` rồi `+ 1` | `TypeError` nếu cộng str với int | `int(input(...))` sau khi kiểm |

**Chưa cần try/except nâng cao ở Week02**; học xử lý exception hệ thống
ở Week11. Với các bài tập, dùng `strip()`, `isdigit()` và
`if` đơn giản (xem trước Week03), sau đó dùng `int()`.

## Bài tương tự — học thật bằng cách tự viết

Mở [practice/README.md](practice/README.md). Ba lab dùng dữ liệu khác
các ví dụ mẫu:

| Lab tự làm | Em phải tự thực hiện | Một kết quả cần đạt |
|---|---|---|
| 01 — Profile | biến, type, conversion | `Tuổi năm sau: 19` |
| 02 — Shop | `int()`, multiplication, `f-string` | `Thành tiền: 75,000 VND` |
| 03 — Vé | `input()`, kiểm chữ số, tính hóa đơn | `Lan: 2 vé, tổng 24,000 VND` |

Từ **gốc repository**, thử bộ kiểm code sinh viên:

```bash
python weeks/week-02-variables-types/practice/checks/check_practice.py --starter
```

Lúc chưa làm TODO, máy sẽ báo `FAIL (0/3)` — đó là **đúng
thiết kế**. Sau khi tự viết, chạy lại cho đến khi đạt
`Week 02 student practice: PASS (3/3)`.

Khi đã làm xong mới đối chiếu lời giải (không chấm bài sinh viên):

```bash
python weeks/week-02-variables-types/practice/checks/check_practice.py --solutions
```

## Tự trả lời trước khi hoàn thành

- Vì sao `"3" + "2"` cho kết quả khác `int("3") + 2`?
- `input()` trả kiểu gì, dù em nhập `20`?
- `.strip()` làm gì với `"  An  "`?
- `.isdigit()` kiểm được điều gì và **chưa đủ** để kiểm gì?
- Điểm khác nhau giữa `print()`, kết quả tính toán và định dạng f-string?
- Bằng chứng của em là **đã tự sửa TODO**, hay chỉ chạy `--solutions`?

Sau đó xem [mini-project Thẻ sinh viên](mini-project/README.md),
viết một ghi chú **Input → Xử lý → Output**, một lỗi em đã kiểm
và một cách cải thiện. Không có rubric mới; không yêu cầu pytest
hoặc framework tại Week02.
