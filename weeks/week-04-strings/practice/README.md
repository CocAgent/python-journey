# Week 04 — Ba bài tự luyện tương tự, có máy tự kiểm

**Chỉ học sau khi đã xem [ba ví dụ từng bước](../WORKED-EXAMPLES.md).**
Bộ này độc lập với 4 bài `exercises/` có sẵn và mini-project
Text Analyzer; **không thay rubric hoặc yêu cầu Week04**.

## Quy trình sinh viên

1. **Dự đoán** output trước khi chạy `examples/04–06`.
2. Mở `practice/starter/`, đọc TODO và thử một input thường.
3. Tự viết code ngay bên dưới TODO; **không sao chép solutions**.
4. Thử input sai và giá trị biên, xem có báo thành công giả không.
5. Chạy `--starter` để kiểm chính file đã viết.
6. Chỉ khi tự làm xong, so với `practice/solutions/` và giải thích khác biệt.

## Lab 01 — Truy cập và đảo từ khóa

File: `starter/lab01_keyword.py`.

| Input | Kết quả mong đợi |
|---|---|
| `Python` | `Đầu: P`, `Cuối: n`, `Đảo: nohtyP`, `Độ dài: 6` |
| `  Python  ` | như trên (đã `strip`) |
| `Cóc` | `Độ dài: 3` |
| chỉ khoảng trắng | `Từ khóa không được rỗng` |

Gợi ý: **kiểm `if not keyword:` trước khi truy cập `keyword[0]`**.

## Lab 02 — Chuẩn hóa câu, đếm từ

File: `starter/lab02_word_counter.py`.

| Input | Kết quả mong đợi |
|---|---|
| `  PYTHON   la  Python ` | `Chuẩn hóa: python la python`, `Số từ: 3`, `Từ python: 2` |
| `python pythonic python` | `Số từ: 3`, `Từ python: 2` |
| `Xin   chào` | `Chuẩn hóa: xin chào`, `Số từ: 2` |
| rỗng / toàn khoảng trắng | `Câu không được rỗng` |

Gợi ý: `words = sentence.lower().split()`. Dùng
`" ".join(words)` và `words.count("python")`, **không**
dùng `sentence.count("python")` vì `pythonic` không phải từ `python`.

## Lab 03 — Kiểm mã sự kiện bằng regex

File: `starter/lab03_event_code.py`.

Mã sự kiện **giả lập** theo mẫu `EV-` + **3 chữ số ASCII**:

| Input | Kết quả mong đợi |
|---|---|
| `EV-123`, `EV-000`, `EV-999` | `Mã hợp lệ: <mã>` |
| `EV-12`, `EV-1234` | `Mã không hợp lệ` |
| `XEV-123`, `EV-123X` | `Mã không hợp lệ` |
| `ev-123`, `EV-１２３`, rỗng | `Mã không hợp lệ` |

Gợi ý: `re.fullmatch(r"EV-[0-9]{3}", code)`. `re.search`
không phù hợp khi bắt buộc **toàn bộ** mã khớp.

## Chạy và tự kiểm

Từ gốc `python-journey/`:

```bash
# Chạy file sinh viên và nhập dữ liệu khi được hỏi
python weeks/week-04-strings/practice/starter/lab01_keyword.py
python weeks/week-04-strings/practice/starter/lab02_word_counter.py
python weeks/week-04-strings/practice/starter/lab03_event_code.py

# Bộ kiểm sẽ FAIL khi TODO chưa hoàn thành — đúng thiết kế
python weeks/week-04-strings/practice/checks/check_practice.py --starter

# Lời giải tham khảo, chỉ để đối chiếu sau khi tự làm
python weeks/week-04-strings/practice/checks/check_practice.py --solutions
```

Máy kiểm dùng `subprocess` và nhiều input tự động;
**sinh viên chưa cần hiểu cách viết bộ checker** hoặc cài pytest.
Khi hoàn thành ba bài:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Week 04 student practice: PASS (3/3)
```

Nếu FAIL: đọc input và kết quả thực tế trong thông báo, sửa file
`practice/starter/`, **không sửa checker**. CI chỉ xác thực
`--solutions`, không tuyên bố sinh viên đã hoàn thành bài.

## Ghi bằng chứng

```text
Bài:
Input thường → dự đoán → kết quả thật:
Input biên → dự đoán → kết quả thật:
Input sai → vì sao bị từ chối:
Một lỗi em đã phát hiện và tự sửa:
Một giới hạn của cách làm:
```

`split()` ở đây tách theo khoảng trắng, không phải bộ tách từ
tiếng Việt hoàn chỉnh. `[0-9]` là quy tắc học tập, không phải
tiêu chuẩn nhận dạng mã vé sản xuất.
