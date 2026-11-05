# W09 — Midterm Bot V1

## Python focus

Tích hợp kiến thức W01–W08 thành một chương trình local có cấu trúc.

## Milestone

Ghép structured teaching state, decision function và local action thành Bot V1
chạy trong Line Arena. Bot được đánh giá riêng với WaitBot, ForwardBot và
CautiousBot; milestone này không triển khai Arena production.

## Definition of done

```text
BOT_RUNS_LOCALLY = YES
LEGAL_TEACHING_ACTIONS = YES
RULES_EXPLAINABLE = YES
GIT_HISTORY = PRESENT
README = PRESENT
```

“Legal” trong milestone này chỉ nói về action set do course-local model định
nghĩa. Nó không phải legal-action contract của VuaCóc.

## Evidence

- Một lệnh local chạy được từ README của project người học.
- Bot V1 tạo action cho các teaching states đã công bố.
- Kết quả với cả ba baseline được ghi riêng, không gộp thành win percentage bắt buộc.
- Người học giải thích behavior và xác định ít nhất một known weakness.
- Git history cho thấy các bước build, debug và improve.

Chạy reference evaluator từ repository root:

```bash
python weeks/week-09-midterm-project/reference/evaluate_baselines.py
```

Kiểm tra reference artifacts:

```bash
python weeks/week-09-midterm-project/checks/check_midterm_reference.py
```

Evidence cho mỗi baseline gồm opponent, result, turn count, một observed
strength và một observed weakness. Dùng
[`evidence-template.md`](../../../weeks/week-09-midterm-project/evidence-template.md)
để ghi commit SHA, bug đã sửa, known weakness và next improvement.
