# Week 10 — File I/O: Dự đoán → Chạy → Quan sát → Tự làm

Đọc bài chính trong [README](README.md) và [notes](notes.md) trước.
Bộ thực hành này bổ sung ba ví dụ và ba lab, **không thay exercises
hoặc Replay Inspector**. Chỉ dùng thư viện chuẩn Python >=3.12,
tất cả file trong ví dụ được tạo dưới `TemporaryDirectory()`.

## Chạy từ gốc repository

```bash
python weeks/week-10-files-io/examples/04_predict_text_paths.py
python weeks/week-10-files-io/examples/05_predict_csv_types.py
python weeks/week-10-files-io/examples/06_predict_json_validation.py
```

Học theo vòng: **che output → dự đoán → chạy → giải thích →
thay một input → làm lab tương tự → kiểm chứng**.

## Ví dụ 04 — File text và đường dẫn

Một đường dẫn `Path("notes/lesson.txt")` là *tương đối với
working directory của terminal*, không phải tự động tương đối
với mã Python. Trong ví dụ, ta neo đường dẫn vào thư mục tạm
và chủ động tạo thư mục cha trước khi ghi UTF-8.

| Tình huống | Em dự đoán | Kết quả |
|---|---|---|
| `target.exists()` trước khi ghi | … | `False` |
| Ghi `"Chào Python\nDòng hai\n"` | … | Hai dòng UTF-8 |
| `target.exists()` sau khi ghi | … | `True` |
| Đọc đường dẫn thiếu | … | `FileNotFoundError` |
| Thư mục tạm sau khi ra khỏi `with` | … | Tự được dọn |

Cảnh giác: `path.write_text(...)` là cách viết ngắn của
`path.open(..., encoding="utf-8")` và thao tác ghi; bài lab
luyện **context manager** `with` trực tiếp. File thiếu không
được trả `[]` giả như dữ liệu vốn rỗng, trừ khi contract
đã thiết kế rõ hành vi đó.

**Bài tương tự:** [Lab 01 — Lưu ghi chú](practice/README.md),
nhận `Path` từ caller, tạo thư mục cha và round-trip dòng
tiếng Việt; so sánh file rỗng với file chưa tồn tại.

## Ví dụ 05 — CSV: chữ số trong file là chuỗi

```python
writer = csv.DictWriter(stream, fieldnames=["name", "score"])
writer.writeheader()
writer.writerow({"name": "An", "score": 8})
```

Sau khi đọc bằng `csv.DictReader`, dữ liệu trông như
`{"name": "An", "score": "8"}`: **score là str**, không
phải `int`! Phải chuyển kiểu và kiểm phạm vi rồi mới tính.

| Trường hợp | Dự đoán | Kết quả |
|---|---|---|
| Điểm 8 ghi rồi đọc | … | `"8"` |
| `type(row["score"]).__name__` | … | `str` |
| `int("8")` | … | `8` |
| `int("not-a-number")` | … | `ValueError` |
| Header sai tên/thứ tự | … | Parser có thể đọc nhưng schema phải từ chối |

**Chú ý `newline=""` khi mở CSV** để module `csv` quản
lý newline đúng trên các hệ điều hành. Không tin dữ liệu chỉ vì
file được parse thành công.

**Bài tương tự:** [Lab 02 — Điểm số CSV](practice/README.md)
lưu/đọc bảng học viên, kiểm header, kiểu và khoảng 0..10.
Dữ liệu invalid phải bị từ chối trước khi ghi đè file cũ.

## Ví dụ 06 — JSON hợp cú pháp chưa chắc hợp schema

Replay giảng dạy mang đúng hai nhãn:

```text
COURSE LOCAL FORMAT
NOT VUACOC PRODUCTION FORMAT
```

`json.loads("[]")` là **JSON hợp lệ**, nhưng **không hợp
contract replay** vì ta cần một object có `format`,
`production_compatibility`, `turns`.

| Dữ liệu | Parse JSON? | Hợp replay? |
|---|---|---|
| object đủ nhãn, turns list | Có | Có (sau validation) |
| `[]` | Có | Không |
| `{"turns":[]}` | Có | Không — thiếu nhãn |
| `{broken` | Không | Không — `JSONDecodeError` |
| file chưa tồn tại | Không thể đọc | `FileNotFoundError` |

Việc chuyển `dict` ⇄ JSON **không tự đảm bảo** trường dữ liệu
đúng kiểu. Lab sẽ kiểm `turn` là int thật (không nhận bool),
`action` thuộc `{"left","right","wait"}`. Đây là **schema
học tập offline**, không đại diện cho API VuaCóc sản xuất.

**Bài tương tự:** [Lab 03 — Lưu replay có kiểm schema](practice/README.md).

## Những lỗi cần sinh viên tự nhận ra

| Hiện tượng | Cách tìm nguyên nhân |
|---|---|
| File xuất hiện ở thư mục lạ | Kiểm `Path.cwd()`; truyền đường dẫn rõ |
| File thiếu nhưng vẫn trả `[]` | Đừng đánh tráo missing với empty |
| CSV tính tổng sai kiểu | `DictReader` trả chuỗi, cần `int()` và validation |
| JSON parse được nhưng replay hỏng | Phân biệt parse với schema validation |
| File bị ghi đè trước khi validation | Kiểm input **trước** mở file ghi |
| UTF-8 tiếng Việt hiển thị sai | Mở cả hai chiều với `encoding="utf-8"` |
| Thấy `COURSE LOCAL FORMAT` rồi suy ra production | Không được — hai schema độc lập |

## Tự kiểm code sinh viên

```bash
python weeks/week-10-files-io/practice/checks/check_practice.py --starter
python weeks/week-10-files-io/practice/checks/check_practice.py --solutions
```

`--starter` kiểm đúng hàm sinh viên, file được tạo trong
thư mục tạm, rồi tự xóa. Khi TODO chưa hoàn thành: **FAIL (0/3)**
là đúng. Chỉ so với `--solutions` sau khi tự làm.
`--solutions` PASS không phải kết quả của sinh viên.

**Chuyển giao Week 11:** chọn một file thiếu, một CSV sai điểm,
một JSON sai cú pháp. Ghi tên lỗi, input nhỏ nhất gây lỗi,
và cho biết lỗi nào có thể xử lý tại biên đọc dữ liệu.
