# Week 11 — Đọc traceback → tái hiện → sửa nguyên nhân → thử lại

**Bài học bổ sung** cho chương Exceptions, Tracebacks & Debugging.
Giữ nguyên exercises và mini-project chính. Không cần mạng,
thư viện bên ngoài hay đăng nhập; Python >=3.12.

## Khởi động từ gốc repository

```bash
python weeks/week-11-exceptions/examples/05_predict_traceback_regression.py
python weeks/week-11-exceptions/examples/06_predict_specific_exceptions.py
python weeks/week-11-exceptions/examples/07_predict_else_finally.py
```

Mỗi ví dụ: **Dự đoán → Chạy → Giải thích → Tái hiện bug
với input nhỏ nhất → Sửa → Regression test → Bài tương tự**.

## Ví dụ 05 — Một bug tính khoảng cách

Một phiên bản lỗi dùng `goal - start` thay vì
`abs(goal - start)`. Với `start=4, goal=1`,
chương trình trả `-3` thay vì khoảng cách `3`.
Đây là **lỗi logic**: Python không nhất thiết ném exception.

| Bước debug | Câu hỏi | Bằng chứng |
|---|---|---|
| Reproduce | Input nhỏ nhất tạo lỗi là gì? | `(4,1)` |
| Read | Có traceback không? | Không — kết quả logic sai |
| Isolate | Dòng tính nào sai? | `goal-start` |
| Fix | Phép tính đúng? | `abs(goal-start)` |
| Re-test | Còn đúng với `(1,4)`? | Cả hai chiều đều là 3 |

Ví dụ còn cố ý bắt `ValueError` từ `int("bad")` để chỉ
ra exception **type**, **message** và thao tác gây lỗi.
Khi xem traceback thật, đọc **dòng cuối trước**, sau đó
ngược lên frame trong code của em.

**Bài tương tự:** tạo một regression nhỏ cho bộ tính tiền hoặc
khoảng cách khác; thử input đảo chiều trước và sau fix.

## Ví dụ 06 — Chỉ bắt những lỗi có thể xử lý

`read_score(path)` minh họa ba tình huống:

| Input | Dự đoán | Kết quả |
|---|---|---|
| File chưa tồn tại | … | `None` do `FileNotFoundError` được xử lý |
| File chứa `8` | … | `8` |
| File chứa `eight` | … | `None` do `ValueError` chuyển kiểu |
| File chứa `11` | … | `None` do ngoài 0..10 |
| Lỗi lập trình khác | … | **Không che**, cần sửa bug |

Ở bài này, **hàm có contract trả None cho missing/invalid score**,
khác Lab 01 Week 10 vốn chủ động để file thiếu ném lỗi.
Không có chính sách duy nhất cho mọi hàm: cách xử lý phải dựa
vào **contract** đã công bố.

Không dùng `except Exception: pass` hay bare `except:`
để chương trình trông như "ổn". Nếu truyền sai đối tượng
đường dẫn khiến `AttributeError`, đó thường là lỗi cần nhìn
thấy, không phải score sai có thể bỏ qua.

**Bài tương tự:** [Lab 01 — `safe_int`](practice/README.md)
và [Lab 02 — Đọc file điểm](practice/README.md).

## Ví dụ 07 — `else` và `finally` chạy khi nào?

```python
try:
    number = int(raw)
except ValueError:
    audit.append("except")
    return None
else:
    audit.append("else")
    return "right" if number > 0 else "wait"
finally:
    audit.append("finally")
```

| `raw` | `return` | `audit` |
|---|---|---|
| `"2"` | `right` | `["else","finally"]` |
| `"bad"` | `None` | `["except","finally"]` |
| `None` (sai kiểu) | `TypeError` tiếp tục nổi lên | `["finally"]` |

`else` chỉ chạy nếu **try không raise exception**.
`finally` chạy kể cả khi đã có `return` hoặc exception
chưa xử lý. Tránh `return` trong `finally` vì có thể
che exception/giá trị return trước đó.

**Bài tương tự:** [Lab 04 — Ghi nhật ký chuyển đổi
bất kể thành công hay lỗi](practice/README.md).

## Bốn bài tự viết với bộ tự kiểm gọi hàm

| Lab | Input/Output | Lỗi sinh viên phải xử lý |
|---|---|---|
| 01 | `safe_int(raw)` → int hoặc None | Catch `ValueError`, để `TypeError` nổi rõ |
| 02 | `read_score(path)` → 0..10 hoặc None | File thiếu, chữ không phải số, out-of-range |
| 03 | `validate_action(action)` → action hoặc `ValueError` | Error message chứa input sai |
| 04 | `valid_score(raw,audit)` → int/None | `except/else/finally`, audit có đúng thứ tự |

Từ gốc repository:

```bash
python weeks/week-11-exceptions/practice/checks/check_practice.py --starter
python weeks/week-11-exceptions/practice/checks/check_practice.py --solutions
```

**Chưa làm TODO → `--starter` phải FAIL (0/4)**.
`--solutions` chỉ kiểm đáp án tham khảo. Máy kiểm thử
lỗi cụ thể và đường đi không có exception. Sinh viên
không cần học pytest trước Week 12.

## Debugging notebook — evidence thay cho đoán mò

Ghi cho mỗi bug ít nhất một bộ evidence:

```text
1. Minimal failing input:
2. Expected result:
3. Observed result / exception type:
4. Failing operation:
5. Root cause:
6. Minimal fix:
7. Regression: cùng input cũ + input đảo chiều / biên:
8. Vì sao không dùng broad except:
```

Dự án Bot local: **strategy loss** (bot chơi yếu nhưng đúng
contract) khác **software defect** (crash, illegal action,
malformed replay). Bộ lab này không kết nối VuaCóc production,
và không che failure của local arena.

**Chuyển giao sang Week 12:** giữ lại input lỗi nhỏ nhất
làm một testcase pytest. Không thay rubric hoặc bài tập gốc.
