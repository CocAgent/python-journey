# Đề cương khóa học Python Journey

> **15 tuần** · **7–10 giờ/tuần** · **Python >= 3.12** · Beginner → reliable Python programming

## Nguồn chân lý

- `SYLLABUS.md` = curriculum 15 tuần.
- `FINAL_PROJECT.md` = yêu cầu và rubric capstone.
- `README.md` = overview/navigation.
- `PROGRESS.md` = learner checklist.

---

## Chuẩn đầu ra toàn khóa

Sau 15 tuần, người học có thể:

1. viết chương trình Python nhỏ đúng và dễ đọc;
2. phân rã bài toán bằng hàm và module;
3. lựa chọn cấu trúc dữ liệu Python phù hợp;
4. xử lý text, file, CSV và JSON;
5. đọc traceback, xử lý exception và debug có phương pháp;
6. viết test bằng `pytest` cho logic chính và edge cases;
7. gọi HTTP API cơ bản và xử lý JSON response;
8. sử dụng type hints ở mức nền tảng;
9. dùng OOP khi class/composition thực sự giúp mô hình rõ hơn;
10. dùng Git/GitHub để lưu lịch sử phát triển;
11. hoàn thành, test, document và bảo vệ một capstone.

Learning loop xuyên khóa:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

---

# Giai đoạn 1 — Khởi đầu

## Tuần 01 — Environment · REPL · Terminal · Git/GitHub · Hello Python

### Learning outcomes
- Cài và nhận diện đúng Python >= 3.12.
- Chạy lệnh trong terminal.
- Dùng Python REPL và chạy file `.py`.
- Sử dụng `print()`, comment, biểu thức số học cơ bản.
- Biết repository, commit, push ở mức nhập môn.
- Hình thành thói quen đọc lỗi thay vì bỏ qua lỗi.

### Sản phẩm
Một chương trình Python nhỏ chạy được từ terminal và có commit đầu tiên.

---

## Tuần 02 — Variables · Types · Input/Output

### Learning outcomes
- Khai báo và đặt tên biến rõ nghĩa.
- Phân biệt `int`, `float`, `str`, `bool`.
- Dùng `input()`, `type()`, type conversion.
- Nhận biết lỗi chuyển kiểu phổ biến.
- Tách input, processing và output ở mức đơn giản.

### Sản phẩm
Ứng dụng nhập dữ liệu và tính toán có kiểm tra đầu vào cơ bản.

---

## Tuần 03 — Conditionals · Boolean · Input validation

### Learning outcomes
- Dùng `if/elif/else`.
- Dùng toán tử so sánh và `and/or/not`.
- Hiểu truthy/falsy ở mức nhập môn.
- Kiểm tra input trước khi xử lý.
- Viết các nhánh điều kiện dễ đọc.

### Sản phẩm
Chương trình ra quyết định và từ chối input không hợp lệ.

---

# Giai đoạn 2 — Dữ liệu & tư duy chương trình

## Tuần 04 — Strings · Text processing · Regex mini-lab

### Learning outcomes
- Indexing, slicing và string methods.
- `strip`, `split`, `join`, `replace`, `find`.
- f-string.
- Ưu tiên string methods khi đủ dùng.
- Làm quen `re.search()` / `re.fullmatch()` và pattern cơ bản.
- Nhận biết khi regex thực sự hữu ích.

### Sản phẩm
Text Analyzer + regex mini-lab.

---

## Tuần 05 — Lists · Tuples · Mutability · Unpacking

### Learning outcomes
- CRUD trên list.
- Indexing/slicing.
- Tuple và immutability.
- Unpacking.
- Hiểu khác biệt mutable/immutable.
- Dùng list comprehension ở mức rõ ràng, không lạm dụng.

### Sản phẩm
Ứng dụng quản lý dữ liệu tuần tự.

---

## Tuần 06 — Loops · enumerate · zip · comprehensions

### Learning outcomes
- `for`, `while`, `break`, `continue`.
- Dùng `enumerate()` thay cho quản lý index thủ công khi phù hợp.
- Dùng `zip()` để duyệt song song.
- Nested loop khi thực sự cần.
- Comprehension đơn giản, dễ đọc.

### Sản phẩm
Bài toán lặp trên dữ liệu có cấu trúc.

---

## Tuần 07 — Functions · Decomposition · Scope · Type hints

### Learning outcomes
- `def`, `return`, parameters, default arguments.
- Scope local/global.
- Docstring cơ bản.
- Chia một bài toán lớn thành các hàm nhỏ có trách nhiệm rõ.
- Type hints cơ bản cho parameter và return value.
- Hiểu: **type annotation là contract/documentation/tooling aid, không phải runtime validation**.

### Sản phẩm
Utility Toolkit gồm nhiều hàm nhỏ, có contract rõ.

---

## Tuần 08 — Dict · Set · Nested data · Data modeling

### Learning outcomes
- `dict`, `get`, `items`, `keys`, `values`.
- Nested dict/list.
- `set` và các phép toán tập hợp.
- Chọn cấu trúc dữ liệu dựa trên bài toán.
- Mô hình hóa dữ liệu đơn giản trước khi nghĩ đến class.

### Sản phẩm
Word/Data Counter hoặc ứng dụng dữ liệu nhỏ.

---

# Tuần 09 — Midterm Project 🏆

Tổng hợp W01–W08.

### Yêu cầu
- bài toán rõ;
- dùng hàm để phân rã;
- cấu trúc dữ liệu phù hợp;
- input validation;
- README ngắn;
- Git history có ý nghĩa;
- demo và giải thích được code.

---

# Giai đoạn 3 — Viết chương trình đáng tin cậy

## Tuần 10 — File · pathlib · CSV · JSON

### Learning outcomes
- Đọc/ghi text với context manager.
- Dùng `pathlib.Path`.
- Đọc/ghi CSV bằng module `csv`.
- Serialize/deserialize JSON.
- Xử lý file chưa tồn tại hoặc dữ liệu lỗi ở mức phù hợp.

### Sản phẩm
Ứng dụng có data persistence.

---

## Tuần 11 — Exceptions · Tracebacks · Debugging · Defensive coding

### Learning outcomes
- `try/except/else/finally`, `raise`.
- Các exception phổ biến.
- Đọc traceback từ dưới lên.
- Xác định failing line.
- Tái hiện bug.
- Tạo minimal failing input.
- Sửa rồi chạy lại.
- Không dùng bare `except:` để che lỗi.

### Debugging loop
```text
Reproduce → Read traceback → Isolate → Fix → Re-test
```

### Sản phẩm
Một chương trình được harden bằng xử lý lỗi và debugging có bằng chứng.

---

## Tuần 12 — Testing with pytest

### Learning outcomes
- Hiểu mục đích của automated test.
- `assert`.
- Cấu trúc test function trong `pytest`.
- Arrange → Act → Assert.
- Normal case.
- Boundary/edge case.
- Invalid input.
- Đọc test failure.
- Sửa implementation rồi chạy test lại.

### Không thuộc phạm vi
- mocking nâng cao;
- integration-test architecture;
- property-based testing chuyên sâu.

### Sản phẩm
Một module logic có test suite cơ bản.

---

## Tuần 13 — Modules · Packages · Dependencies · CLI · API/HTTP

### Learning outcomes
- `import`, module tự viết, `__name__ == "__main__"`.
- Package ở mức nhập môn.
- `venv` và `python -m pip`.
- Hiểu dependency declaration và vai trò của `pyproject.toml`.
- CLI arguments ở mức cơ bản (`sys.argv` hoặc `argparse` nhập môn).
- HTTP GET.
- Status code.
- JSON response.
- Timeout/network error ở mức nhập môn.
- Validate dữ liệu nhận từ API.

### Sản phẩm
Một CLI nhỏ hoặc API client dùng public endpoint không cần secret.

---

## Tuần 14 — OOP Essentials · Composition · Basic inheritance

### Learning outcomes
- Class, object, `__init__`, `self`.
- Instance attributes và methods.
- `__str__`.
- Nhận biết khi class có lợi hơn dict/functions.
- Composition trước inheritance.
- Inheritance cơ bản khi có quan hệ “is-a” tự nhiên.

### Không thuộc phạm vi
- inheritance hierarchy phức tạp;
- design patterns;
- metaclass/descriptors;
- advanced decorators;
- architecture chuyên sâu.

### Sản phẩm
Một mô hình nhỏ dùng class khi bài toán thực sự cần.

---

# Tuần 15 — Capstone Project 🎓

Yêu cầu chính thức: [`FINAL_PROJECT.md`](FINAL_PROJECT.md).

Capstone phải chứng minh:

- chức năng đúng;
- phân rã hợp lý;
- xử lý lỗi;
- tests có ý nghĩa;
- README;
- Git history;
- khả năng giải thích code và quyết định thiết kế.

---

# Đánh giá

| Thành phần | Tỷ trọng |
|---|:---:|
| Bài tập/self-check hàng tuần | 30% |
| Mini-projects | 20% |
| Midterm Project | 20% |
| Capstone Project | 30% |
| **Tổng** | **100%** |

Rubric chi tiết capstone chỉ nằm trong `FINAL_PROJECT.md`.

---

# Ranh giới với Python Mastery

Python Journey:

> **Can I program reliably in Python?**

Python Mastery:

> **Can I engineer good Python software?**

Để dành cho Mastery/chuyên sâu:

- advanced decorators;
- generators/iterators chuyên sâu;
- advanced typing/protocols;
- descriptors/metaclasses;
- advanced tests/mocking;
- concurrency/asyncio;
- design patterns;
- architecture;
- performance/profiling;
- packaging/publishing chuyên sâu.
