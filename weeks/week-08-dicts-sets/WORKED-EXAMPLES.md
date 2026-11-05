# Week 08 — Dict, Set và Nested Data: dự đoán → chạy → giải thích → vận dụng

**Mục tiêu:** sinh viên tự chọn đúng cấu trúc dữ liệu và có thể giải thích
vì sao chương trình cho kết quả đó, thay vì sao chép một ví dụ có sẵn.
Các bài mới chỉ dùng Python >=3.12, chạy offline, không cần package hay API.

## 0. Bắt đầu tại repository root

Mở terminal tại thư mục chứa `weeks/`. Trên Windows có thể thay
`python` bằng `py -3`.

```bash
python weeks/week-08-dicts-sets/examples/06_predict_dict_get_copy.py
python weeks/week-08-dicts-sets/examples/07_predict_set_and_order.py
python weeks/week-08-dicts-sets/examples/08_nested_state_validated.py
```

Với **mỗi** ví dụ, hãy thực hiện: (1) che kết quả rồi **dự đoán**;
(2) chạy; (3) so sánh; (4) giải thích dòng tạo ra kết quả;
(5) thay **một** dữ liệu rồi thử lỗi; (6) tự viết một bài tương tự ở
[practice/README.md](practice/README.md). Dùng Undo để phục hồi code mẫu.

## 1. Ví dụ 06 — Dict, .get(), membership, frequency và copy

```python
student = {"name": "An", "score": 8}
print("name" in student)
print("An" in student)
print(student.get("level", "beginner"))
```

| Biểu thức | Em dự đoán | Kết quả và nguyên nhân |
|---|---|---|
| `"name" in student` | … | `True`: `in` kiểm **key** |
| `"An" in student` | … | `False`: value không phải key |
| `student.get("level", "beginner")` | … | `"beginner"`: key tùy chọn vắng mặt |
| `student["id"]` | … | `KeyError` nếu gọi trực tiếp |
| `student.get("id", 0)` | … | `0`, nhưng **không có nghĩa ID hợp lệ** |

**Quy tắc thiết kế:** dùng `dict[key]` khi key bắt buộc
đã được kiểm, dùng `.get(key, default)` khi field thực sự
tùy chọn. Nếu `id` bắt buộc, `id` thiếu phải được báo,
không gán `0` để chương trình trông như đang thành công.

Bản sao dict phẳng:

```python
snapshot = student.copy()
student["score"] = 9
print(snapshot["score"])  # 8
print(student["score"])   # 9
```

`copy()` tạo bản sao **một lớp**: đủ khi value là số/chuỗi;
với nested list/dict, bản sao vẫn có thể chia sẻ value mutable.
Đừng coi shallow copy là deep copy.

Đếm từ bằng `.get`:

```python
counts = {}
for word in "Python python dict".lower().split():
    counts[word] = counts.get(word, 0) + 1
# {"python": 2, "dict": 1}
```

`.split()` trong bài nhập môn chỉ tách theo whitespace;
không phải bộ tách từ tiếng Việt, và không loại dấu câu.

**Tự thử:** thay một `python` bằng `set`, dự đoán dict
tần suất mới. Sau đó làm [Lab 01 — word frequency và cập nhật
điểm trên dict copy](practice/README.md).

## 2. Ví dụ 07 — Set là tập phần tử duy nhất, KHÔNG phải list có thứ tự

```python
a = {"loop", "dict", "set"}
b = {"dict", "function"}
```

| Câu hỏi | Dự đoán | Kết quả |
|---|---|---|
| `a | b` | … | `dict, function, loop, set` (tập hợp) |
| `a & b` | … | chỉ `dict` |
| `a - b` | … | `loop, set` |
| `type(set()).__name__` | … | `set` |
| `type({}).__name__` | … | `dict` |
| `len(set(["a","a","b"]))` | … | `2` |

Một `set` **không giữ số lần xuất hiện**. Vì vậy `set("aab")`
không giúp đếm chữ `a` có 2 lần, và **không đủ để kiểm anagram**.
Dùng dict tần suất hoặc so sánh chuỗi sau sắp xếp nếu cần
biết số lượng xuất hiện.

**Không dựa vào thứ tự hiển thị của set.** Trong ví dụ,
trước khi in kết quả phép toán tập hợp ta dùng `sorted(...)`
để output dễ dự đoán. Nếu yêu cầu là "lọc trùng nhưng giữ thứ tự
gặp đầu tiên", dùng một `list` kết quả và một `set` để kiểm:

```python
seen = set()
result = []
for item in ["python", "git", "python", "dict"]:
    if item not in seen:
        seen.add(item)
        result.append(item)
# result == ["python", "git", "dict"]
```

**Tự thử:** đổi list đầu vào thành `["a", "a", "b", "a"]`
rồi dự đoán. Làm [Lab 03 — phép tập hợp và giữ thứ tự](practice/README.md).

## 3. Ví dụ 08 — Nested State phải kiểm trước khi quyết định

Mô hình Bot này **chỉ để học Python**, không mô tả giao diện
hoặc runtime chính thức của VuaCóc:

```text
COURSE TEACHING MODEL
NOT VUACOC PRODUCTION CONTRACT
```

Schema giả lập:

```python
state = {
    "bot": {
        "position": 1,             # key bắt buộc, int 0..4
        "goal": 4,                 # key bắt buộc, int 0..4
        "opponent_position": 3,    # optional, int 0..4
    }
}
```

Đường đi dữ liệu:

```text
state["bot"] → kiểm bot là dict
             → kiểm position / goal có key, là int thật, trong 0..4
             → kiểm opponent_position nếu có
             → ưu tiên đã đến goal hoặc đối thủ ở gần -> wait
             → còn lại: left / right hướng tới goal
             → tạo dòng giải thích bằng field đã đọc
```

| State của bot | Em dự đoán | Kết quả |
|---|---|---|
| `position=1, goal=4, opponent=3` | … | `right` |
| `position=4, goal=4` | … | `wait` |
| `position=3, goal=0` | … | `left` |
| thiếu `position` | … | `State không hợp lệ` |
| `position=True` | … | `State không hợp lệ` |

**Bẫy quan trọng:** trong Python, `bool` là một loại `int`,
vì thế `isinstance(True, int)` là True. Khi schema yêu cầu
**số nguyên không phải Boolean**, ví dụ dùng `type(x) is int`.
Type hint cũng không tự xác thực input lúc chạy.

**Field thiếu và field sai khác nhau:** optional field vắng mặt có
thể hợp lệ; **field có mặt nhưng sai kiểu** cần được từ chối.
`dict.get("position", 0)` không thể thay bước xác nhận
key bắt buộc khi state đến từ nguồn bên ngoài.

**Tự thử:** đổi `position` từ 1 thành 4, rồi thành `True`;
dự đoán trước khi chạy và giải thích nhánh nào có hiệu lực.
[Lab 04 — mô hình state độc lập](practice/README.md) có
validation, decision function và explanation. Invalid được phân
biệt rõ với "wait" bình thường.

## 4. Bốn bài tự viết — KHÔNG sao chép ví dụ mẫu

| Lab | Bài toán mới | Kiến thức cần vận dụng |
|---|---|---|
| 01 | Đếm tần suất từ và cập nhật điểm không sửa dict gốc | `get`, `items`, `copy` |
| 02 | Tạo báo cáo điểm từ nested learner data | `dict` + `list`, mandatory/optional |
| 03 | So sánh nhóm kỹ năng và lọc trùng giữ thứ tự | `set` operations + list |
| 04 | State → validate → action → explanation | structured dict, set allowed actions |

Bắt đầu từ [practice/README.md](practice/README.md). Bốn starter chứa
TODO; lời giải nằm riêng. **Checker gọi chính function**, kiểm return,
input thường/biên/sai, không cho in sẵn kết quả để tạo PASS.

```bash
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --starter
```

Trước khi làm TODO, `FAIL (0/4)` là **đúng thiết kế**.
Sau khi tự hoàn thành phải đạt `PASS (4/4)`. Chỉ sau đó
mới đối chiếu đáp án tham khảo:

```bash
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --solutions
```

**PASS của lời giải tham khảo không chứng minh bài sinh viên đã làm.**

## 5. Khi sai, tìm nguyên nhân chứ không sửa máy kiểm

| Hiện tượng | Nguyên nhân có thể có | Hướng xử lý |
|---|---|---|
| `KeyError` | gọi `data["required"]` trước khi kiểm key | kiểm key bắt buộc, rồi đọc |
| Không tìm được value qua `in dict` | `in` kiểm key, không kiểm value | cân nhắc `values()` |
| Điểm gốc thay đổi sau update | cập nhật dict caller trực tiếp | `copy()` trước khi sửa |
| `len(set(...))` đếm thiếu | set đã loại trùng | dùng dict tần suất |
| Output set thay thứ tự giữa các lần | set không có thứ tự ổn định | chỉ `sorted` khi cần trình bày |
| List lọc trùng không giữ thứ tự | `list(set(...))` | kết hợp `seen set` và `result list` |
| Truy cập nested field thất bại | thiếu tầng hoặc sai kiểu | kiểm từ tầng ngoài vào trong |
| State sai vẫn báo action thành công | optional default che missing required | validate và giải thích invalid |
| `True` được nhận là vị trí 1 | bool là subtype của int | `type(value) is int` khi cần |

## 6. Chuyển giao trước dự án giữa khóa Week 09

Tự chọn một trong ba bài mở rộng: **quản lý bài tập của lớp**
(nested dict), **bảng kỹ năng học viên** (set + dict) hoặc
**bộ quyết định bot offline** (course-local). Thiết kế model
trước, nêu rõ **key bắt buộc**, **key tùy chọn**, một danh sách
cần giữ thứ tự và một tập hợp cần uniqueness.

Ghi bằng chứng:

```text
Input:
Dự đoán:
Kết quả thực:
Dict, list, set được chọn vì:
Một key thiếu và cách báo lỗi:
Một dữ liệu sai kiểu và cách từ chối:
Một bug đã sửa:
Em đã kiểm chứng kết quả bằng input nào khác:
```

Tiếp tục [Decision Dashboard](mini-project/README.md) hoặc
[State + Heuristic Bot Journey](../../projects/vuacoc-bot-journey/milestones/w08-state-and-heuristic.md).
Không thay curriculum, rubric, hoặc yêu cầu sản xuất.
