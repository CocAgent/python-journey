# Tuần 11 — Exceptions, Tracebacks và Debugging

Tuần này tập trung vào cách **đọc lỗi trước khi sửa**, xử lý những lỗi đầu vào có thể dự đoán và giữ cho lỗi lập trình được nhìn thấy. Mục tiêu không phải là làm chương trình “không bao giờ báo lỗi”, mà là làm cho lỗi được phát hiện, giải thích và sửa một cách có kiểm soát.

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đọc traceback để xác định exception type, message, file, dòng và thao tác gây lỗi.
- Phân biệt dữ liệu đầu vào không hợp lệ với programming bug.
- Dùng `try`, `except`, `else`, `finally` và `raise` đúng mục đích.
- Kiểm tra dữ liệu tại boundary và đưa ra thông báo lỗi có ích.
- Tái hiện lỗi bằng input nhỏ nhất, cô lập nguyên nhân, sửa và kiểm tra hồi quy.
- Phân biệt chiến thuật yếu của bot với lỗi phần mềm trong dự án local.

## Lộ trình học

1. Đọc [notes](notes.md) để nắm traceback, exception và defensive coding.
2. Chạy các ví dụ trong thư mục [examples](examples/), quan sát cả trường hợp thành công lẫn thất bại.
3. Tự giải các bài trong [exercises](exercises/) trước khi xem [hints](hints.md).
4. Chạy [machine check](checks/README.md) để kiểm tra lời giải.
5. Hoàn thành [mini-project](mini-project/README.md) và ghi lại bằng chứng debug.

## 1. Đọc traceback

Khi chương trình phát sinh lỗi, hãy bắt đầu từ **dòng cuối cùng** của traceback. Dòng đó thường cho biết exception type và message. Sau đó đọc ngược lên để tìm frame gần code của bạn nhất, gồm tên file, số dòng và operation liên quan.

Ví dụ:

```python
raw_age = "twenty"
age = int(raw_age)
```

Lệnh `int(raw_age)` phát sinh `ValueError`, vì chuỗi `"twenty"` không biểu diễn một số nguyên hợp lệ. Hãy dùng traceback để tìm đúng operation gây lỗi thay vì đoán hoặc sửa nhiều chỗ cùng lúc.

## 2. Bắt exception cụ thể

Dùng `try/except` khi bạn biết operation nào có thể thất bại và có cách xử lý phù hợp.

```python
raw_age = input("Nhập tuổi: ")

try:
    age = int(raw_age)
except ValueError:
    print("Tuổi phải là số nguyên.")
else:
    print(f"Tuổi của bạn là {age}.")
```

- `try`: chứa operation có khả năng phát sinh lỗi dự kiến.
- `except ValueError`: xử lý đúng loại lỗi đã dự kiến.
- `else`: chỉ chạy khi khối `try` hoàn thành mà không có exception.

Không nên dùng `except Exception: pass` để che mọi lỗi. Cách đó có thể biến typo, `NameError` hoặc lỗi invariant thành hành vi khó phát hiện và debug.

## 3. Validate dữ liệu và dùng `raise`

Kiểm tra điều kiện tại ranh giới nhận dữ liệu hoặc trước khi dữ liệu đi vào phần logic chính. Nếu giá trị vi phạm contract, hãy báo lỗi rõ ràng.

```python
def validate_action(action: str) -> str:
    allowed_actions = {"left", "right", "wait"}

    if action not in allowed_actions:
        raise ValueError(f"illegal local action: {action!r}")

    return action


print(validate_action("left"))
# validate_action("jump")  # ValueError: illegal local action: 'jump'
```

Thông báo lỗi nên giúp xác định giá trị nào không hợp lệ và vì sao. Chỉ bắt exception ở nơi chương trình thực sự có thể xử lý hoặc bổ sung ngữ cảnh hữu ích.

## 4. Hiểu `finally`

`finally` chạy khi rời cấu trúc `try`, kể cả khi có exception hoặc khi function thực hiện `return`. Nó phù hợp cho cleanup hoặc ghi nhận một thao tác luôn phải diễn ra; không dùng nó để nuốt lỗi.

```python
audit_log = []

def parse_score(raw: str) -> int | None:
    try:
        score = int(raw)
    except ValueError:
        return None
    else:
        return score if 0 <= score <= 10 else None
    finally:
        audit_log.append(f"parsed={raw!r}")
```

Trong ví dụ này, đầu vào không chuyển được thành số nguyên hoặc điểm nằm ngoài khoảng 0–10 sẽ cho kết quả `None`; log vẫn được ghi. Với file, nên ưu tiên `with open(...)` vì context manager thường quản lý việc đóng file rõ ràng hơn.

## 5. Quy trình debug

Dùng quy trình sau mỗi khi gặp lỗi:

```text
Reproduce → Read traceback → Isolate → Fix → Re-test
```

1. **Reproduce:** tạo lại lỗi với các bước và input xác định.
2. **Read traceback:** đọc exception type, message, file và dòng lỗi.
3. **Isolate:** tìm input nhỏ nhất vẫn tái hiện được lỗi; thu hẹp vùng code liên quan.
4. **Fix:** sửa nguyên nhân gốc bằng thay đổi nhỏ, có chủ đích.
5. **Re-test:** chạy lại trường hợp lỗi và các trường hợp liên quan; thêm regression check nếu phù hợp.

## 6. Strategy loss và software defect

Trong bot hoặc game local, hai trường hợp sau không giống nhau:

| Trường hợp | Ý nghĩa |
| --- | --- |
| **Strategy loss** | Bot tuân thủ contract và chạy đúng, nhưng quyết định hoặc chiến thuật chưa tốt. |
| **Software defect** | Chương trình crash, tạo replay sai định dạng hoặc sinh hành động local không hợp lệ. |

Một trận thua không tự động chứng minh có bug. Ngược lại, một bot có chiến thuật tốt vẫn cần xử lý lỗi đúng cách. Hãy ghi nhận failure reason rõ ràng thay vì âm thầm bỏ qua exception.

## Lệnh kiểm tra

Chạy machine check từ thư mục gốc repository:

```bash
python weeks/week-11-exceptions/checks/check_solutions.py
```

Chạy các test của local arena và replay cho mini-project:

```bash
pytest projects/vuacoc-bot-journey/tests/test_local_arena.py -q
pytest projects/vuacoc-bot-journey/tests/test_replay.py -q
```

Nếu lệnh thất bại, hãy đọc output, tái hiện lỗi và sửa nguyên nhân; đừng bỏ qua kết quả chỉ để test có vẻ thành công.

## Checklist hoàn thành

- [ ] Giải thích được exception type và message từ một traceback.
- [ ] Phân biệt được expected bad input với programming bug.
- [ ] Dùng đúng vai trò của `try/except/else/finally` và `raise`.
- [ ] Chạy machine check và xem lại kết quả.
- [ ] Ghi lại minimal failing input, nguyên nhân, fix và regression check cho mini-project.
- [ ] Phân biệt strategy weakness với software defect.

## Evidence cần lưu

- Output `Week 11 solution checks: PASS` từ machine check (khi đạt).
- Một traceback đã đọc và giải thích được nguyên nhân.
- Một ví dụ xử lý input sai bằng exception cụ thể.
- Bằng chứng mini-project: minimal failing input, exception type/message hoặc failure reason, nguyên nhân đã cô lập, fix và regression check.

**Nguyên tắc quan trọng:** xử lý lỗi dự kiến một cách cụ thể, nhưng đừng che giấu lỗi lập trình.