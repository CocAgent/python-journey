# Week 08 — Bài tự luyện Dict · Set · Nested Data · Heuristic

**Sinh viên bắt đầu tại [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md).**
Bộ này bổ sung cho bốn bài chính trong `exercises/` và
mini-project `Decision Dashboard`; không thay lời giải, rubric,
hoặc milestone VuaCóc.

## Phương pháp thực hành

1. Dự đoán kết quả ba ví dụ 06–08 trên giấy.
2. Chạy ví dụ và giải thích **vì sao** key/field được nhận hoặc từ chối.
3. Đọc docstring và TODO của từng file trong `practice/starter/`.
4. Viết code **vào chính hàm starter**, đừng sửa checker hoặc xem lời giải ngay.
5. Với mỗi hàm, thử một input thường, một input rỗng/thiếu và một input sai.
6. Chạy `--starter` rồi điều tra lab FAIL.
7. Sau khi tự làm, mới đối chiếu `practice/solutions/`.

## Lab 01 — Frequency + Update trên bản sao

`starter/lab01_dict_frequency.py`

Hai hàm:

```python
count_words(text: str) -> dict[str, int]
update_score(scores: dict[str, int], topic: str, score: int) -> dict[str, int]
```

- `count_words("Python python dict")` → `{"python":2,"dict":1}`.
- Chuỗi chỉ có khoảng trắng → `{}`.
- `update_score({"dict":7}, "dict", 9)` → `{"dict":9}`,
  nhưng dict đầu vào vẫn giữ `{"dict":7}`.
- Điểm -1, 11 hoặc `True` → `ValueError`.

Hỏi: `counts.get(word,0)+1` giúp trường hợp từ chưa tồn tại ra sao?
Vì sao thay trực tiếp `scores["dict"]` vi phạm contract?

## Lab 02 — Nested Learner Report

`starter/lab02_nested_learner.py`

```python
learner = {
    "name": "An",
    "scores": [8, 9, 7],
    "progress": {"week": 8},
}
```

`summarize_learner(learner)` phải trả:

```text
An: trung bình 8.0, tuần 8
```

`progress` là **tùy chọn**: khi vắng mặt hoặc có dict rỗng,
in `tuần chưa rõ`. Nhưng nếu có mặt mà sai kiểu, hoặc week
không phải int 1..15, báo `Dữ liệu không hợp lệ`. `name`
và `scores` là bắt buộc; scores rỗng, chứa bool, hoặc ngoài
0..10 đều không hợp lệ. **Không sửa learner của caller**.

Hỏi: vì sao `learner.get("scores", [])` không đủ để xác nhận
schema? Khi nào `.get` thích hợp?

## Lab 03 — Set operations + List giữ thứ tự

`starter/lab03_set_skills.py`

```python
compare_skills({"dict", "set"}, {"set", "loop"})
```

Trả dict với **4 key**:

```text
common      = {"set"}
only_first  = {"dict"}
only_second = {"loop"}
all         = {"dict", "set", "loop"}
```

`unique_in_order(["python","git","python","dict","git"])`
→ `["python","git","dict"]`. List nguồn không thay đổi,
và hai set rỗng không gây lỗi.

Hỏi: tại sao không dùng `list(set(items))` khi cần giữ thứ tự
xuất hiện đầu tiên?

## Lab 04 — Model State + Guard + Heuristic

`starter/lab04_state_decision.py`, **TEACHING MODEL ONLY**.

Các hàm:

```python
validate_state(state: dict[str, object]) -> bool
choose_action(state: dict[str, object]) -> str
explain_decision(state: dict[str, object]) -> str
```

`position` và `goal` bắt buộc, kiểu **int thật**
trong phạm vi `0..4`; `opponent_position` tùy chọn,
nhưng nếu có phải là int trong `0..4`.

| Input | Action | Explanation |
|---|---|---|
| `position=1, goal=4, opponent=3` | right | `position=1, goal=4, action=right` |
| `position=4, goal=4` | wait | `position=4, goal=4, action=wait` |
| `position=3, goal=0` | left | `position=3, goal=0, action=left` |
| `position=2, goal=4, opponent=3` | wait | đối thủ ở gần, action=wait |
| thiếu goal, position=True, opponent sai kiểu | wait fallback | `State không hợp lệ` |

**Điểm quan trọng:** khi dữ liệu sai, `choose_action` trả
`"wait"` an toàn, nhưng `explain_decision` phải phân biệt
trường hợp sai với wait bình thường. Không tự gán "wait"
là kết quả thành công từ input hỏng. Không dùng API thực,
không gọi agent tự chủ hoặc VuaCóc production.

## Chạy từ repository root

```bash
# Kiểm CHÍNH hàm đang viết trong practice/starter
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --starter

# Chỉ để đối chiếu reference sau khi hoàn tất
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --solutions
```

Checker import module không chạy main demo, gọi hàm với nhiều
input và kiểm `return`, types, set/list order, snapshot và
invalid fallback. **Starter chưa hoàn thiện sẽ báo FAIL (0/4)**.

Sau khi hoàn thành, mong đợi:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Lab 04: PASS
Week 08 student practice: PASS (4/4)
```

`--solutions` PASS chỉ nghĩa **đáp án mẫu đúng**. Nó không
chấm bài trong `starter/`.

## Nhật ký học tập / chuyển bài toán mới

Hãy chọn một bài quản lý sách, nhóm kỹ năng lớp hoặc state
course-local. Ghi ngắn:

```text
Em muốn mô hình hóa điều gì:
Vì sao dùng dict / list / set:
Key bắt buộc và key tùy chọn:
Em dự đoán:
Em chạy và quan sát:
Một input rỗng/thiếu:
Một input sai kiểu:
Một bug em đã sửa:
```

Không yêu cầu class, JSON/file I/O, `pytest`, framework
hoặc dịch vụ bên ngoài ở Week08.