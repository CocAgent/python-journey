# Tuần 15 — Capstone · Tests · README · Git/GitHub

Tuần cuối tích hợp kỹ năng đã học thành evidence có thể chạy, đọc và review.

## Canonical capstone

Đề bài, deliverables và rubric duy nhất nằm tại
[FINAL_PROJECT.md](../../FINAL_PROJECT.md). Week 15 không định nghĩa rubric
thứ hai và VuaCóc Bot không phải lựa chọn bắt buộc.

## Outcomes

- hoàn thiện một vertical slice có scope rõ;
- chạy tests và ghi known failures;
- viết README có setup, usage, evidence và limitations;
- tạo commit history dễ review;
- demo một kết quả có thể tái hiện.

Flagship optional track:
[VuaCóc Bot Journey](../../projects/vuacoc-bot-journey/README.md), gồm local
tournament và replay course-local.

Xem [integration checklist](notes.md) và [gợi ý theo hạng mục](hints.md).

Starter documentation:

- [Capstone README template](../../templates/capstone-readme-template.md)
- [AI usage template](../../templates/AI_USAGE.template.md)

## Readiness check

Week 15 không có exercises hay official solutions: deliverable chính là project
của bạn. Thay vào đó, tự kiểm tra evidence cơ học trước khi handoff:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py path/to/my-project
```

Check xác nhận README có setup/usage/test, có `AI_USAGE.md`, đủ hàm, đủ test,
pytest collect được và không có bare `except:`. Nó **không chấm điểm** — rubric
duy nhất vẫn là [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

Chi tiết: [`checks/README.md`](checks/README.md).
