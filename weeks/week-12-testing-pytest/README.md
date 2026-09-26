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
