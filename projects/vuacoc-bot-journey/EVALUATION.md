# Evaluation Design

Evaluation giúp người học trả lời không chỉ “bot thắng bao nhiêu?” mà còn “bot
có đúng, đáng tin cậy và giải thích được không?”. Mọi tiêu chí ở đây áp dụng
cho course/local environment.

## 1. Correctness

- Bot trả action thuộc teaching action set.
- Cùng input và cùng strategy tạo cùng output khi thiết kế yêu cầu deterministic.
- Normal case và boundary case có evidence.

## 2. Robustness

- Known bad input không làm hỏng toàn bộ luồng local.
- Bug đã sửa có regression test.
- Known failures được ghi lại thay vì che giấu.

## 3. Strategy

- Strategy có mục tiêu và rules giải thích được.
- So sánh với baseline local theo cùng điều kiện.
- Win rate, nếu được đo local, chỉ là một tín hiệu chứ không phải tiêu chí duy nhất.

## 4. Software quality

- Bot core tách khỏi adapter.
- Tên hàm, module và dữ liệu thể hiện trách nhiệm.
- Tests tập trung vào hành vi quan trọng.
- Git history cho thấy quá trình cải tiến.

## 5. Explainability

- Người học mô tả được state đi vào, rule được chọn và action đi ra.
- Người học giải thích được một trade-off hoặc known failure.
- README và demo đủ để người khác chạy và hiểu thiết kế.

## Evidence tối thiểu ở W15

```text
BOT_RUNS
TESTS_PASS
REPLAY_AVAILABLE
KNOWN_FAILURES_DOCUMENTED
BASELINE_EVALUATION_DONE
DESIGN_EXPLAINED
AI_USAGE_DISCLOSED
```

Không có rating algorithm production nào được khóa trong tài liệu này. Nếu
runtime contract chưa được xác minh, tournament local vẫn là evidence giáo dục
hợp lệ và phải được ghi rõ là local.
