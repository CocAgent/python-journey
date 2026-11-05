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

first, second = second, first
```

Số tên bên trái phải phù hợp số phần tử được unpack.

## 6. Chọn collection

```text
list  → thứ tự quan trọng và collection cần thay đổi
tuple → nhóm giá trị nhỏ, cố định sau khi tạo
```

Week 06 sẽ dùng loop, `enumerate`, `zip` và comprehensions để xử lý nhiều phần
tử. Week 05 tập trung vào cấu trúc và mutability trước.
