# Tuần 12 — Testing with pytest

Tests biến expected behavior thành evidence chạy lại được.

## Outcomes

- giải thích vì sao test hữu ích;
- nhận biết pytest discovery và tên `test_*`;
- dùng `assert` và Arrange → Act → Assert;
- viết normal, edge, invalid và regression case;
- test quyết định bot và legal local actions ở phạm vi learner.

## Learner tests và maintainer tests

`weeks/week-12-testing-pytest/tests/` thuộc bài học. `tests/` ở root kiểm
tra invariant của repository; hai scope không được trộn.

Đi theo [notes](notes.md), [examples](examples/), [exercise](exercises/),
[hints](hints.md) và [mini-project](mini-project/README.md).

```bash
pytest weeks/week-12-testing-pytest/tests -q
python weeks/week-12-testing-pytest/checks/check_week.py
```


## Bài mẫu bổ sung — nhiều bộ dữ liệu kiểm thử

Hãy đọc hai file [order_total.py](examples/order_total.py) và
[test_order_total.py](examples/test_order_total.py). Ví dụ dùng
`@pytest.mark.parametrize` để thử trường hợp bình thường, trường hợp biên
và đầu vào sai mà không lặp lại toàn bộ hàm test.

Chạy riêng bài mẫu từ **thư mục gốc repository**:

```bash
python -m pytest weeks/week-12-testing-pytest/examples/test_order_total.py -q
```

## Tự làm bài kiểm thử (không dùng đáp án mẫu)

Mở [test_decision_starter.py](exercises/test_decision_starter.py),
thay từng dòng `raise NotImplementedError` bằng các phép kiểm tra đúng.
Lúc đầu lệnh dưới đây **phải thất bại** vì bài chưa được hoàn thành:

```bash
python -m pytest weeks/week-12-testing-pytest/exercises/test_decision_starter.py -q
```

Khi tất cả test chuyển sang PASS, hãy cố ý thay một giá trị kỳ vọng cho sai
để xác nhận test có khả năng phát hiện lỗi, sau đó khôi phục lại giá trị đúng.

**Phân biệt:** `tests/test_decision.py` là bộ tham chiếu có sẵn;
`exercises/test_decision_starter.py` mới là phần sinh viên phải tự viết.
