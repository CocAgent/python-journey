# Week 05 — Lists, Tuples, Mutability và Unpacking

## 1. List là collection có thứ tự

```python
topics = ["strings", "lists", "tuples"]
print(topics[0])
print(topics[-1])
print(topics[:2])
```

## 2. Thay đổi list

```python
topics.append("mutability")
topics[0] = "text"
topics.remove("tuples")
last = topics.pop()
```

Các operation này thay đổi list hiện có. `sorted(topics)` tạo list mới, còn
`topics.sort()` thay đổi list tại chỗ.

## 3. Mutability: alias và copy

```python
original = ["A", "B"]
alias = original
copied = original.copy()

alias.append("C")
print(original)  # ["A", "B", "C"]
print(copied)    # ["A", "B"]
```

`alias` và `original` gọi cùng một list. `copy()` tạo một shallow copy đủ cho
list phẳng trong bài học này. Không đi sâu vào object identity internals.

## 4. Tuple và immutability

```python
point = (3, 7)
```

Tuple có thứ tự nhưng không hỗ trợ gán lại một phần tử. Tuple phù hợp cho một
nhóm nhỏ có cấu trúc cố định như coordinate hoặc RGB value.

## 5. Packing và unpacking

```python
profile = "An", 20, "Python"
name, age, topic = profile
print(f"{name} · {age} · {topic}")

first = "A"
second = "B"
first, second = second, first
print(first, second)  # B A
```

Số tên bên trái phải phù hợp số phần tử được unpack.

## 6. Chọn collection

```text
list  → thứ tự quan trọng và collection cần thay đổi
tuple → nhóm giá trị nhỏ, cố định sau khi tạo
```

Week 06 sẽ dùng loop, `enumerate`, `zip` và comprehensions để xử lý nhiều phần
tử. Week 05 tập trung vào cấu trúc và mutability trước.

## 7. Từ ví dụ đến bài tự viết

Sổ tay [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md) giải thích vì sao
`alias = original` **không tạo bản sao**, vì sao `sort()` trả
`None`, khi nào `remove`/`pop` có thể gây lỗi, và tuple không
thể gán lại một phần tử.

Để nhớ sâu hơn, làm [3 lab tương tự](practice/README.md).
Kết quả `--starter` là kiểm code sinh viên; kết quả `--solutions`
chỉ kiểm đáp án mẫu, không được đánh tráo.

**Giới hạn của copy:** `list.copy()` tạo shallow copy. Với các
list phẳng chứa số/chuỗi dùng trong bài chính là phù hợp; với
list lồng nhau, phần tử con có thể vẫn dùng chung. Tuple bất biến ở
cấp phần tử nhưng có thể chứa object mutable như list.

Các ví dụ mới chưa cần loop/comprehension; Week 06 học các công cụ
này có hệ thống.
