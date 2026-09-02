# Week 08 — Dictionaries, Sets và Data Modeling

Week 07 giúp ta đặt behavior trong function. Week 08 tập trung vào data mà
function nhận: dữ liệu có cấu trúc giúp code diễn đạt đúng bài toán hơn.

## 1. Vì sao cần `dict`?

Một list phù hợp khi vị trí mang ý nghĩa. Một `dict` phù hợp khi mỗi giá trị có
một tên rõ ràng:

```python
student = {"name": "An", "score": 8.5, "active": True}
```

Các key `name`, `score`, `active` làm data tự mô tả tốt hơn `["An", 8.5, True]`.

## 2. Tạo, đọc và cập nhật

```python
student = {"name": "An", "score": 8.5}
print(student["name"])
print(student.get("level", "beginner"))

student["score"] = 9.0
student["city"] = "Đà Nẵng"
```

`data[key]` phù hợp khi key bắt buộc phải có. `data.get(key, default)` phù hợp
khi key là tùy chọn hoặc cần một safe default rõ nghĩa.

## 3. Duyệt dictionary

```python
scores = {"Python": 9, "Git": 8, "Debug": 7}

for topic in scores.keys():
    print(topic)

for score in scores.values():
    print(score)

for topic, score in scores.items():
    print(f"{topic}: {score}")
```

Membership trên dict kiểm tra **key**:

```python
if "Python" in scores:
    print("Đã có điểm Python")
```

## 4. `set` cho uniqueness và membership

Set không giữ phần tử trùng:

```python
actions = {"left", "right", "wait", "wait"}
print(actions)
print("wait" in actions)
```

Các phép toán đơn giản trả lời câu hỏi về hai nhóm:

```python
group_a = {"dict", "set", "loop"}
group_b = {"set", "function", "loop"}

print(group_a | group_b)  # tất cả
print(group_a & group_b)  # phần chung
print(group_a - group_b)  # chỉ có ở A
```

Set phù hợp để kiểm tra membership hoặc loại trùng. Nếu thứ tự quan trọng, cần
giữ list và dùng set phụ để theo dõi phần tử đã thấy.

## 5. Nested data

Data thực tế thường chứa nhiều tầng:

```python
learner = {
    "name": "An",
    "skills": ["functions", "dicts"],
    "progress": {"week": 8, "completed": 7},
}

print(learner["progress"]["week"])
```

Đọc từ ngoài vào trong: lấy `progress`, rồi lấy `week`. Chỉ thêm tầng lồng nhau
khi tầng đó thể hiện một nhóm dữ liệu có ý nghĩa.

## 6. Data model khác behavior

```text
data model = chương trình lưu những gì và liên hệ giữa chúng
behavior   = function đọc hoặc thay đổi data như thế nào
```

```python
task = {"title": "Học dict", "tags": ["python"], "done": False}


def mark_done(item: dict) -> dict:
    updated = item.copy()
    updated["done"] = True
    return updated
```

Dict là model. `mark_done` là behavior. Tách hai ý này giúp ta debug từng phần.

## 7. Structured bot state

```text
COURSE TEACHING MODEL
NOT VUACOC PRODUCTION CONTRACT
```

Local Arena truyền một state nhỏ từ góc nhìn của bot:

```python
state = {
    "turn": 2,
    "max_turns": 6,
    "position": 1,
    "opponent_position": 3,
    "goal": 4,
    "min_position": 0,
    "max_position": 4,
}
```

Đây chỉ là schema giảng dạy của Python Journey. Nó không mô tả production
state, action, API hay runtime của VuaCóc.

## 8. Structured state → heuristic decision

Heuristic là một nhóm rule đơn giản, đọc được, không bảo đảm tối ưu:

```python
LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    position = state.get("position", 0)
    goal = state.get("goal", position)

    if position == goal:
        return "wait"
    if position < goal:
        return "right"
    return "left"
```

Rule nên có thứ tự ưu tiên rõ và luôn trả action thuộc course-local set.

## 9. Cách luyện tập

Với mỗi model:

1. viết ra câu hỏi chương trình cần trả lời;
2. chọn key và kiểu collection vừa đủ;
3. thử normal case, boundary case và key tùy chọn bị thiếu;
4. kiểm tra output, sửa model hoặc behavior nếu cần;
5. giải thích decision rồi commit evidence.
