# Hai ví dụ có lời giải từng bước — không trùng 10 ý đề

Các ví dụ này có mục tiêu **gợi cách suy nghĩ**, không phải đáp án.

## Ví dụ A — Tính tổng bội số của 3

**Đề khác:** hàm `sum_multiples_of_three(start, end)` trả tổng
các số chia hết cho 3 trong đoạn. Dự đoán:
`sum_multiples_of_three(1, 9)` → `18` vì 3+6+9.

```python
def sum_multiples_of_three(start: int, end: int) -> int:
    if type(start) is not int or type(end) is not int or start > end:
        raise ValueError("Đoạn không hợp lệ")
    total = 0
    for number in range(start, end + 1):
        if number % 3 == 0:
            total += number
    return total

assert sum_multiples_of_three(1, 9) == 18
assert sum_multiples_of_three(-3, 3) == 0
```

**Giải thích:** `range(start,end+1)` bao gồm end;
`number % 3 == 0` lọc các số phù hợp;
`return` đưa số về caller.

**Tự thay dữ liệu:** `(1,8)` → 9, `(3,3)` → 3.
Đề chính Câu 2a yêu cầu **số chẵn**, vì vậy hãy tự
chuyển điều kiện, không sao chép cả ví dụ.

## Ví dụ B — Tách các giá trị lớn hơn một ngưỡng

```python
def values_at_least(values: list[int], minimum: int) -> list[int]:
    if not isinstance(values, list):
        raise ValueError("Cần list")
    chosen = []
    for value in values:
        if value >= minimum:
            chosen.append(value)
    return chosen

scores = [3, 7, 9, 4]
print(values_at_least(scores, 7))  # [7, 9]
print(scores)  # [3, 7, 9, 4] — không bị sửa
```

Đếm và lọc cần biết **đang duyệt cái gì**, **giữ điều kiện nào**
và **trả kiểu dữ liệu nào**. Câu 5b yêu cầu trả **tên** từ
dictionary, không phải trả các giá trị điểm từ list.

## Quy trình sau mỗi ví dụ

Dự đoán kết quả trước khi chạy; thử một giá trị biên, một
dữ liệu sai kiểu; giải thích vì sao `return` chứ không
`print`; rồi tự viết bài mới trong `submissions_de1/`.
