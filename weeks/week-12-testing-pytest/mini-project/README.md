# Mini-project — Tested Bot Decisions

Viết tests cho một decision function trước khi thay đổi rule:

- normal movement;
- legal action;
- edge case at goal;
- invalid input;
- regression cho bug đã sửa.

Chạy learner tests riêng:

```bash
pytest weeks/week-12-testing-pytest/tests -q
```

Đối chiếu behavior arena ở mức phù hợp:

```bash
pytest projects/vuacoc-bot-journey/tests/test_local_arena.py -q
```
