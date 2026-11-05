# Tuần 10 — File · pathlib · CSV · JSON · Replay

Tuần này dữ liệu sống lâu hơn một lần chạy: text cho nội dung đơn giản, CSV
cho bảng và JSON cho dữ liệu có cấu trúc.

## Outcomes

- tạo đường dẫn bằng `pathlib.Path`;
- đọc/ghi text với `encoding="utf-8"`;
- đọc/ghi CSV và JSON bằng context manager;
- giải thích Python object ↔ JSON-compatible data;
- lưu, tải và kiểm tra replay course-local.

## Learning path

```text
notes → examples → exercises → hints → machine check
      → replay persistence → evidence
```

Đi theo [notes](notes.md), [examples](examples/), [exercises](exercises/),
[hints](hints.md), [machine check](checks/README.md) và
[mini-project](mini-project/README.md).

Replay của project chỉ mang nhãn `COURSE LOCAL FORMAT` và
`NOT VUACOC PRODUCTION FORMAT`.

Exercise ghi output vào `.learner-output/` bên trong thư mục tuần. Output luyện
tập không được commit; evidence cần nộp phải được chép có chủ đích vào project
của người học.

## Lộ trình bổ sung — dự đoán, làm bài tương tự, tự kiểm

Đọc [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md) trước khi chạy
ba ví dụ bổ sung về text/path, CSV và JSON/schema:

```bash
python weeks/week-10-files-io/examples/04_predict_text_paths.py
python weeks/week-10-files-io/examples/05_predict_csv_types.py
python weeks/week-10-files-io/examples/06_predict_json_validation.py
```

Tiếp theo tự hoàn thiện [3 lab starter](practice/README.md):
UTF-8 notes, CSV scores và JSON replay validation.

```bash
python weeks/week-10-files-io/practice/checks/check_practice.py --starter
python weeks/week-10-files-io/practice/checks/check_practice.py --solutions
```

**Lưu ý:** `--starter` kiểm trực tiếp bài viết của sinh viên
trong thư mục tạm; ban đầu **FAIL (0/3)** là đúng thiết kế.
`--solutions` chỉ kiểm tham khảo, không chứng minh sinh viên
đã giải xong. Ví dụ/lab bổ sung không sửa bài gốc, và tuyệt đối
không ghi ra production hay file dữ liệu ngoài thư mục tạm.
