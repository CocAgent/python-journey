# Bộ bài tập tương tự — Week 13 (Study Progress Mini-Project)

Đây là **bài để sinh viên tự viết**, không phải bài toán điểm học phần thực tế.
Ngưỡng điểm 5/10 chỉ minh họa cho `if/else`. Chạy Python >=3.12, offline.

**Đọc trước:** [GUIDED-LABS.md](../GUIDED-LABS.md). Nếu chưa rõ
cách dữ liệu chạy giữa module, CLI, HTTP và storage, xem thêm
[ba ví dụ từng bước](../WALKTHROUGH-EXAMPLES.md). Chạy lệnh dưới đây khi
đứng tại thư mục `weeks/week-13-modules-cli-api/`.

## Quy trình cho từng bài

1. Chạy một `examples.exNN` tương ứng đã có của Week13.
2. Mở `practice/starter/labNN_*.py`, đọc mô tả và dự đoán output.
3. Sửa **chỉ file trong starter/**. Dùng lại hàm `status_for_score()`
   trong `practice/study_core.py`, không tự copy logic cốt lõi.
4. Chạy module vừa sửa bằng `python -m`.
5. Chạy `python -m practice.checks.check_lab --starter`, sửa cho đến
   khi PASS 4/4.
6. Chỉ sau khi tự làm, mở `practice/solutions/` để đối chiếu và
   giải thích khác biệt.

## Các lệnh để thử

```bash
python -m practice.starter.lab01_module
python -m practice.starter.lab02_cli --score 7.5
python -m practice.starter.lab03_http
python -m practice.starter.lab04_adapter
python -m practice.checks.check_lab --starter
```

**Trước khi viết mã, checker trên phải FAIL**. Nếu sửa starter để kiểm
PASS 4/4, đó là bài của chính em; lệnh solution dưới đây không thay thế
bằng chứng tự làm:

```bash
python -m practice.checks.check_lab --solutions
```

## Lộ trình 4 lab

| Lab | Em sẽ viết | Kết quả mục tiêu | Test lỗi |
|---|---|---|---|
| 1 | Import module, return + main guard | `Điểm 7.5: Đạt` | input số sai bị core từ chối |
| 2 | CLI `--score`, JSON, exit 0/2 | `{"score": 7.5, "status": "Đạt"}` | 12 / thiếu flag / chữ |
| 3 | Parse HTTP/JSON fixture | dict có score 8, status Đạt | 404 / JSON sai / thiếu score |
| 4 | Adapter form dict → report | dict student An, score 7.5 | thiếu score / tên rỗng / bool |

## Không làm thay bài tập gốc

`exercises/ex01_modules.py`–`ex04_adapter.py` vẫn là bốn bài khác,
có [lời giải riêng](../solutions/README.md). Bộ tương tự này giúp **tự
chuyển kiến thức từ Bot demo sang một miền dữ liệu khác**.

Nếu em muốn nâng cấp thêm, chọn một đề tài từ
[20 mã nguồn tham khảo Week09](../../week-09-midterm-project/project-ideas/catalog-20-du-an.md)
hoặc [Ticket Desk](../advanced_projects/README.md) và tự tạo feature mới.
