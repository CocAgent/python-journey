# Week 10 — Ba lab thực hành tương tự, có checker gọi hàm thật

Đọc [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md), sau đó
**tự viết trong `starter/`**, không sao chép `solutions/`.
Mọi file được kiểm qua `TemporaryDirectory`; không ghi vào
repo hoặc dữ liệu production. Không cần cài pytest.

## Lab 01 — Ghi và đọc ghi chú UTF-8

`lab01_text_notes.py` có hai hàm `save_notes(path, lines)`
và `load_notes(path)`. Khi lưu `["Chào", "Tạm biệt"]`,
file chứa `Chào\nTạm biệt\n` và tải lại đúng hai dòng.

File rỗng `[]` phải round-trip được. File **chưa tồn tại**
phải gây `FileNotFoundError`, không giả thành file rỗng.
Tạo thư mục cha và dùng `with path.open(...,encoding="utf-8")`.

## Lab 02 — Bảng điểm CSV

`save_scores(path, rows)` ghi header `name,score` và
`load_scores(path)` trả `list[dict]` với điểm dạng **int**.
Ví dụ `[{"name":"An","score":8}]` phải giữ nguyên sau khi
save rồi load. Header sai, tên rỗng, điểm chữ, điểm ngoài
0..10 hay `True` (khi lưu) phải từ chối bằng `ValueError`.

Nhớ mở CSV với `newline=""`. **Kiểm tất cả input trước khi
ghi**, không được làm hỏng file cũ khi row invalid.

## Lab 03 — JSON replay với schema nhỏ

Ba hàm: `validate_replay`, `save_replay`, `load_replay`.
Contract là dict có `format="COURSE LOCAL FORMAT"`,
`production_compatibility="NOT VUACOC PRODUCTION FORMAT"`
và `turns` là list các event:

```python
{
    "turn": 1,  # int thực, >= 1
    "action": "wait"  # left/right/wait
}
```

`[]` và object thiếu nhãn là JSON hợp cú pháp nhưng
**schema sai** → `ValueError`. `{broken` →
`JSONDecodeError`; file thiếu → `FileNotFoundError`.
Dữ liệu sai phải bị từ chối trước khi ghi đè file cũ.

## Cách chạy

Từ gốc `python-journey`:

```bash
# Kiểm chính code learner. Ban đầu FAIL (0/3) là đúng.
python weeks/week-10-files-io/practice/checks/check_practice.py --starter

# Chỉ kiểm reference; không thay kết quả sinh viên.
python weeks/week-10-files-io/practice/checks/check_practice.py --solutions
```

Khi hoàn tất: `Week 10 student practice: PASS (3/3)`.
Nếu FAIL, xem tên lab và input, sửa starter; không sửa checker
để tạo PASS giả. Sinh viên chưa cần hiểu mã checker.

Ghi evidence: đường dẫn đã ghi, output dự đoán/thực tế, một
file thiếu, một input sai định dạng, kết quả sửa lỗi. Không
thay exercises hoặc tiêu chí mini-project hiện hành.
