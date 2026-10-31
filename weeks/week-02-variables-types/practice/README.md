# Week 02 — Bài tương tự: tự viết sau khi xem ví dụ

**Dành cho sinh viên mới học.** Đây là ba bài tự luyện (starter TODO)
độc lập với ba bài gốc trong `../exercises/` và
[mini-project Thẻ sinh viên](../mini-project/README.md).
Chỉ cần Python >=3.12 và thư viện chuẩn; **không cần pip, network hoặc pytest**.

## Cách bắt đầu

Đầu tiên đọc [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md)
và chạy ví dụ 04–06. Sau đó mở thư mục `starter/` bằng VS Code,
đọc đề và tự hoàn thành TODO.

Từ **repository root**, có thể chạy từng file:

```bash
python weeks/week-02-variables-types/practice/starter/lab01_profile.py
python weeks/week-02-variables-types/practice/starter/lab02_shop.py
python weeks/week-02-variables-types/practice/starter/lab03_ticket.py
```

Lab 03 sẽ chờ nhập tên và số vé. Nhập lần lượt `Lan`, rồi `2`,
mỗi lần nhấn Enter.

**Mỗi bài hãy thực hiện tuần tự:** dự đoán → chạy starter →
sửa TODO → thử case thường → thử case sai → tự kiểm →
cuối cùng mới xem lời giải.

## Mục tiêu và cách tự kiểm

| Lab | Dữ liệu ban đầu | Cần viết | Kiểm sai |
|---|---|---|---|
| **01 — Profile** | `name="An"`, `age_text="18"` | `int()`, `type()`, f-string | giải thích được vì sao `"18" + 1` sai |
| **02 — Shop** | `unit_price_text="25000"`, `quantity_text="3"` | chuyển số, tính `75,000 VND` | từ chối `"ba"` trước `int()` |
| **03 — Ticket** | người dùng nhập tên và số vé | in phiếu giá `12,000 VND/vé` | `abc`, `0`, `-1` không in hóa đơn |

Chạy **máy kiểm bài sinh viên**:

```bash
python weeks/week-02-variables-types/practice/checks/check_practice.py --starter
```

Khi hoàn thành, cần có:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Week 02 student practice: PASS (3/3)
```

**Máy kiểm cố ý FAIL khi starter chưa hoàn thiện.** Nó đọc output
bài sinh viên, không kiểm số lượng hàm hoặc bắt em dùng một cách code
duy nhất. Nếu fail, đọc lab tương ứng, kiểm lại output, không sửa
checker để làm đẹp kết quả.

Nếu bí, xem gợi ý trong [hints.md](../hints.md). Chỉ sau khi thử
mới mở `solutions/` và chạy:

```bash
python weeks/week-02-variables-types/practice/checks/check_practice.py --solutions
```

Máy kiểm lời giải tham khảo PASS **không có nghĩa bài của em đã làm**.

## Bài mở rộng tự chọn — thay đổi dữ liệu

Chọn **một** trong các bài sau, không chép nguyên ví dụ:

- **Sách:** `price_text="18000"`, `quantity_text="4"` → `72,000 VND`.
- **Điểm kiểm tra:** `score_text="8.5"` → dùng `float()`, in một chữ số thập phân.
- **Vé xe:** `quantity_text="0"` → thông báo không hợp lệ, không in hóa đơn.

Nộp một ghi chú ngắn:

```text
Dự đoán ban đầu:
Kết quả thực tế:
Vì sao đúng/sai:
Em đã sửa dòng nào:
Một input khác em tự kiểm:
Một giới hạn chưa giải quyết:
```

Week02 chỉ yêu cầu đọc hiểu và làm đúng ví dụ/ứng dụng đơn giản.
Exception nâng cao ở Week11, pytest ở Week12; bộ này **không tạo rubric mới**.
