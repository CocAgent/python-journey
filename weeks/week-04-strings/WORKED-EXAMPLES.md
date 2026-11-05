# Week 04 — Dự đoán chuỗi · chạy ví dụ · đọc lỗi · tự giải bài tương tự

> Sinh viên mới học Python · Python >=3.12 · Chạy offline bằng thư viện chuẩn.

**Mục tiêu:** dùng được `index/slice`, `strip/split/join/replace/find/count`,
`f-string` và regex nhỏ. **Không vội dùng regex** khi string methods đủ
giải quyết. Không cần viết class, web API, `pytest` hoặc cài gói bên ngoài.

## 0. Bắt đầu tại đúng thư mục

Mở terminal tại **gốc repository `python-journey/`**:

```bash
python --version
python weeks/week-04-strings/examples/04_predict_slice_and_find.py
python weeks/week-04-strings/examples/05_normalize_words_step_by_step.py
python weeks/week-04-strings/examples/06_regex_search_vs_fullmatch.py
```

Trên Windows có thể thay `python` bằng `py -3`. Các script này không
chờ `input()` và không truy cập mạng.

**Mỗi ví dụ thực hiện sáu bước:** (1) che đáp án, dự đoán; (2) chạy;
(3) so với dự đoán; (4) giải thích một dòng; (5) sửa **một giá trị**
và thử ca lỗi; (6) tự giải bài tương tự trong `practice/starter/`.

## 1. Ví dụ 04 — Index, slice, find và chuỗi rỗng

Cho `word = "Python"`. Trước khi chạy, tự điền cột dự đoán:

| Biểu thức | Dự đoán | Kết quả |
|---|---|---|
| `word[0]` | ... | `P` |
| `word[-1]` | ... | `n` |
| `word[:3]` | ... | `Pyt` |
| `word[::-1]` | ... | `nohtyP` |
| `word.find("th")` | ... | `2` |
| `word.find("Java")` | ... | `-1` |
| `word[:99]` | ... | `Python` |
| `word[99]` | ... | `IndexError` nếu thực thi |

**Tại sao `[:99]` không lỗi nhưng `[99]` lỗi?** Slice được phép
dừng ở cuối chuỗi, còn một chỉ số riêng lẻ phải tồn tại.

**Ca lỗi quan trọng:**

```python
word = ""
if word:
    print(word[0])
else:
    print("Chuỗi rỗng: không đọc được ký tự đầu")
```

Nếu gọi `word[0]` ngay, Python sẽ báo `IndexError`.

**Bài tương tự 01:** nhập một từ khóa, in ký tự đầu/cuối, chuỗi
đảo và độ dài. Khi input chỉ có khoảng trắng, thông báo lỗi
thay vì truy cập ký tự. Xem [Lab 01](practice/README.md).

## 2. Ví dụ 05 — `strip()`, `split()`, `join()`, `count()`

Input: `"  PYTHON    la   Python   "`.

```text
raw text có khoảng trắng thừa
         ↓ strip()
"PYTHON    la   Python"
         ↓ lower() + split()
["python", "la", "python"]
         ↓ " ".join(...)
"python la python"
         ↓ words.count("python")
2 từ "python"
```

Chạy `examples/05_normalize_words_step_by_step.py` rồi tìm dòng:

```text
Sau join: 'python la python'
Số từ: 3
Số từ 'python': 2
```

**Bẫy phổ biến:** `"python pythonic python".count("python")`
cho **3** vì nó đếm cả chuỗi con ở `pythonic`. Trong khi đó
`"python pythonic python".split().count("python")` cho **2**.
Đếm từ theo `split()` chỉ là cách đơn giản, **chưa xử lý dấu câu**:
`python,` và `python` là hai chuỗi khác nhau.

**Ví dụ không thay đổi dữ liệu ban đầu:**

```python
normalized = "python la python"
new_text = normalized.replace("python", "PY")
print(new_text)      # PY la PY
print(normalized)    # python la python
```

Chuỗi trong Python **immutable**: `replace()` trả về chuỗi mới,
không chỉnh biến `normalized` nếu không gán lại.

**Bài tương tự 02:** nhập một câu, chuẩn hóa khoảng trắng và
chữ hoa/thường, đếm **đúng từ** `python`. Có câu rỗng phải báo
`Câu không được rỗng`. Xem [Lab 02](practice/README.md).

## 3. Ví dụ 06 — `re.search` khác `re.fullmatch`

Định dạng học tập giả lập: **`EV-` + đúng 3 chữ số ASCII**. Đây
không phải chuẩn kiểm vé thật.

```python
import re

pattern = r"EV-[0-9]{3}"
print(re.search(pattern, "XEV-123") is not None)     # True
print(re.fullmatch(pattern, "XEV-123") is not None)  # False
print(re.fullmatch(pattern, "EV-123") is not None)   # True
```

| Input | `search` | `fullmatch` | Có chấp nhận mã hoàn chỉnh? |
|---|---|---|---|
| `EV-123` | Có | Có | Có |
| `EV-12` | Không | Không | Không |
| `EV-123X` | Có | Không | Không |
| `XEV-123` | Có | Không | Không |
| `ev-123` | Không | Không | Không |
| ` EV-123 ` | Có | Có sau `strip()` | Có sau `strip()` |

- `search`: tìm một đoạn con khớp ở bất kỳ vị trí nào.
- `findall`: trả danh sách các đoạn khớp, ví dụ `["EV-123", "EV-456"]`.
- `fullmatch`: yêu cầu **toàn bộ** chuỗi khớp.
- `r"..."`: raw string, giúp viết `\d`, `\b` ít nhầm ký tự escape.
- `[0-9]`: chỉ chữ số ASCII; `\d` có thể nhận một số chữ số Unicode
  khác. Ở ví dụ vé giả lập, ta **cố ý** chọn `[0-9]`.
- Khi không thấy kết quả, `re.search(...)` là `None`. Không
  gọi `.group()` khi chưa kiểm `None`.

**Bài tương tự 03:** viết form nhập một mã vé; chỉ chấp nhận
`EV-123`, `EV-000` ... theo đúng pattern. `EV-123X` phải
bị từ chối, không được thông qua chỉ vì `search` tìm thấy một đoạn.

## 4. Debug: chọn đúng công cụ cho từng lỗi

| Hiện tượng | Nguyên nhân | Em cần làm gì? |
|---|---|---|
| `IndexError` khi nhập rỗng | truy cập `s[0]` khi `s==""` | kiểm `if s:` trước |
| `find` trả `-1` | không có chuỗi con | kiểm `-1` trước khi dùng index |
| `"  Python  "` vẫn có khoảng trắng | chưa `strip()` hoặc chưa gán kết quả | `clean = raw.strip()` |
| Đếm `pythonic` thành `python` | dùng `str.count` cho chuỗi con | dùng `words.count("python")` nếu tách từ bằng dấu cách |
| `EV-123X` vẫn hợp lệ | dùng `re.search()` để kiểm toàn bộ mã | dùng `re.fullmatch()` |
| Có thể tìm `EV-１２３` | dùng `\d` với Unicode | dùng `[0-9]` nếu chỉ cho ASCII |
| `replace` không đổi biến gốc | string immutable | gán kết quả vào biến mới |

## 5. Tự làm bài tương tự — code chưa có đáp án

Đọc [practice/README.md](practice/README.md), sau đó sửa
`practice/starter/lab01_keyword.py`, `lab02_word_counter.py`,
`lab03_event_code.py`. Mỗi file có TODO riêng, không bắt buộc
định nghĩa hàm (nội dung hàm chuyên sâu thuộc Week 07).

Chạy từ **gốc repository**:

```bash
python weeks/week-04-strings/practice/checks/check_practice.py --starter
```

Trước khi sửa TODO: **FAIL là đúng**. Sau khi tự hoàn thành 3 lab:
`Week 04 student practice: PASS (3/3)`.

Chỉ khi đã tự làm và hiểu tại sao code đúng, đối chiếu:

```bash
python weeks/week-04-strings/practice/checks/check_practice.py --solutions
```

**PASS của `--solutions` không phải kết quả chấm code sinh viên.**

## 6. Chuyển kiến thức sang một đề tài mới

Chọn **một** ý tưởng để làm thêm (không tính thành bài bắt buộc):

- **Chuẩn hóa tên học viên:** `strip/split/join`, không xóa dấu tiếng Việt.
- **Tìm mã tài liệu:** `PJ-[0-9]{3}` từ đoạn văn bằng `findall`;
  giải thích vì sao tìm thấy đoạn con **không đồng nghĩa** toàn bộ
  nội dung hợp lệ.
- **Phân tích hashtag:** `split()`, `count()`, `replace()` và
  một trường hợp input chỉ chứa khoảng trắng.

Viết bảng nhỏ: **Input → Dự đoán → Actual → Vì sao → Một lỗi đã sửa**.
Không yêu cầu framework, file I/O hay phân tích ngôn ngữ tự nhiên
nâng cao ở Week04.

Tiếp theo: [mini-project Text Analyzer](mini-project/README.md)
và [bốn bài tập gốc](exercises/).
