# Tuần 12 — Kiểm thử chương trình với pytest

> **Mục tiêu:** Không chỉ thấy chương trình chạy, mà tự tạo được bằng chứng cho thấy chương trình xử lý đúng nhiều tình huống.

## Sau tuần này, sinh viên làm được gì?

1. Giải thích được vì sao chạy thử với một dữ liệu đúng **chưa đủ**.
2. Viết phép kiểm tra `assert` có kết quả **cụ thể**, thay vì chỉ kiểm tra chung chung.
3. Viết test cho tình huống thường gặp, điều kiện biên, dữ liệu sai và lỗi đã từng xảy ra.
4. Dùng `pytest.raises` để kiểm tra chương trình báo lỗi đúng cách.
5. Đọc thông báo `FAILED`, tìm nguyên nhân và sửa một lỗi có thể tái hiện.
6. Phân biệt rõ **test tham chiếu** và **test do sinh viên viết**.

**Điều kiện đầu vào:** đã biết hàm (`def`, `return`), `if` và ngoại lệ (`raise`). Cần Python 3.12+ và `pytest` theo [SETUP](../../SETUP.md).

## Lộ trình thực hành

| Chặng | Hoạt động | Bằng chứng |
|---|---|---|
| 1 · Hiểu | Đọc [bài giảng](notes.md), chạy ví dụ | Dự đoán kết quả trước khi chạy |
| 2 · Quan sát | Chạy [ví dụ pytest](examples/) | Biết test nào PASS/FAIL và vì sao |
| 3 · Tự viết | Hoàn thành [bốn test starter](exercises/test_decision_starter.py) | Từng phép `assert` kiểm tra đúng hành vi |
| 4 · Thử lỗi | Chạy kiểm tra với **4 phiên bản cố ý có lỗi** | Test do sinh viên viết phát hiện lỗi |
| 5 · Vận dụng | Làm [mini-project](mini-project/README.md) | Code + báo cáo ngắn về lỗi đã thử |

### 1. Chạy ví dụ (từ thư mục gốc repository)

```bash
python -m pytest weeks/week-12-testing-pytest/examples -q
```

Ví dụ `test_order_total.py` minh họa nhiều dữ liệu (`parametrize`) và kiểm tra ngoại lệ (`raises`).

### 2. Tự viết bốn test — bước quan trọng nhất

Mở `exercises/test_decision_starter.py` và thay bốn dòng `pytest.fail(...)` bằng kiểm tra của chính bạn. **Bản chưa làm được thiết kế để FAIL**, tránh hiểu nhầm rằng bài tập đã hoàn thành.

```bash
python -m pytest weeks/week-12-testing-pytest/exercises/test_decision_starter.py -q
```

Trước khi sửa, bốn test chưa hoàn thành phải báo lỗi. Sau khi sửa, hãy kiểm tra chúng chạy đúng.

### 3. Kiểm tra chất lượng test do sinh viên viết

```bash
python weeks/week-12-testing-pytest/checks/check_student_tests.py
```

Công cụ kiểm tra sẽ:

- chạy test với chương trình đúng: **phải PASS**;
- lần lượt thay bằng bốn chương trình **cố ý sai**: test phải phát hiện lỗi;
- thông báo loại sai sót chưa được phát hiện (nếu có).

Đây là **self-check mang tính hướng dẫn**, không phải hệ thống chấm điểm chống gian lận. Bài test yếu (chẳng hạn `assert action in LOCAL_ACTIONS`) có thể PASS với cả chương trình sai và sẽ không đạt bước này.

### 4. Đối chiếu bộ test tham chiếu của giáo trình

```bash
python weeks/week-12-testing-pytest/checks/check_week.py
```

**Chú ý:** lệnh này chỉ chạy `tests/test_decision.py` do giáo trình cung cấp. `PASS` ở đây **không chứng minh bài của sinh viên đã đúng**. Xem [giải thích các lệnh](checks/README.md).

## Thói quen quan trọng

- Dự đoán trước kết quả mong đợi, rồi mới chạy test.
- Khi test FAIL, không sửa giá trị mong đợi cho “xanh”; xác nhận lại yêu cầu và sửa nguyên nhân.
- Không viết `assert True`, `pass` hoặc một điều kiện quá rộng để thay cho kiểm thử.
- Comment/docstring bằng tiếng Việt: giải thích **lý do**, **trường hợp biên** và **mục đích test**, không dịch máy móc từng dòng.
- Có thể hỏi AI gợi ý đầu vào bất thường; tự kiểm tra, tự giải thích kết quả và công khai sự hỗ trợ theo hướng dẫn của khóa.

## Bài nộp và tiêu chí tự đánh giá (10 điểm)

| Thành phần | Điểm |
|---|---:|
| Bốn test xác nhận **hành vi cụ thể** (normal, edge, invalid, regression) | 4 |
| Test phát hiện được bốn lỗi cố ý (mỗi lỗi 0,5 điểm) | 2 |
| Mô tả được một lần FAIL và nguyên nhân/sửa lỗi | 2 |
| Giải thích được `assert`, `raises`, cách chạy test và giới hạn của test | 2 |
| **Tổng** | **10** |

Điểm số trên là **rubric tham khảo để giảng viên đánh giá**. Lệnh self-check chỉ cung cấp bằng chứng kỹ thuật, không tự quyết định toàn bộ điểm.

## Checklist trước khi nộp

- [ ] Chạy được các ví dụ của bài học.
- [ ] Hoàn thành bốn test starter, không để `pytest.fail`/TODO thay cho kết quả.
- [ ] Chạy bốn test với chương trình đúng và thấy PASS.
- [ ] Chạy `check_student_tests.py` và ghi lại lỗi đã phát hiện.
- [ ] Hoàn thành mini-project và giải thích được mã đã viết.
- [ ] Ghi lệnh chạy và kết quả thực tế; chỉ báo PASS khi đã kiểm chứng.

Đọc [gợi ý theo từng bước](hints.md) nếu bị vướng; ưu tiên tự thử trước.

---

## Mở rộng — kiểm thử lỗi ở nhiều tệp Python

Sau khi hoàn thành bot, hãy thử ví dụ **đơn hàng đi qua ba tệp**: [pricing.py](examples/multi_file_lab/pricing.py), [storage.py](examples/multi_file_lab/storage.py), [service.py](examples/multi_file_lab/service.py). Xem [hướng dẫn và sơ đồ trách nhiệm](examples/multi_file_lab/README.md).

```bash
python -m pytest weeks/week-12-testing-pytest/examples/test_multi_file_lab.py -q
python weeks/week-12-testing-pytest/checks/check_multi_file_faults.py
```

Kết quả mong đợi của ví dụ tham chiếu: **8 ca kiểm thử PASS**, sau đó **6/6 lỗi cố ý bị phát hiện ở 3 tệp**. Công cụ chỉ dùng bản sao tạm; việc kiểm tra lỗi cố ý không thay thế đánh giá bài nộp của sinh viên.

**Phân biệt:** bốn phép thử Bot thuộc *bài tập sinh viên*; bài thử đơn hàng nhiều tệp là *ví dụ tham chiếu để quan sát và tự mở rộng*.
