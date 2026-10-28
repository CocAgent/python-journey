# Week 15 — Execution plan

Đây là một kế hoạch gợi ý để đi từ project đang có tới capstone sẵn sàng demo.
Nó không thay đổi requirements hay rubric trong
[FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## Stage 1 — Scope lock

Output:

- problem statement;
- in-scope features;
- out-of-scope;
- run command;
- test command.

Gate:

```text
Tôi biết chính xác mình đang hoàn thiện cái gì.
```

## Stage 2 — Vertical slice

Hoàn thiện một luồng end-to-end trước.

Gate:

```text
Một user flow quan trọng chạy từ đầu tới cuối.
```

## Stage 3 — Harden

Chạy normal/boundary/invalid cases, đọc traceback, sửa bug và thêm regression
test phù hợp.

Gate:

```text
Core behavior có test và known failures được hiểu.
```

## Stage 4 — Document & prove

Hoàn thiện README, AI_USAGE, evidence, known limitations và Git history.

Gate:

```text
Người khác có thể clone/run/test mà không cần hỏi miệng.
```

## Stage 5 — Demo & defend

Chọn một flow ngắn, một test, một bug đã sửa và một design decision.

Gate:

```text
Tôi giải thích và sửa được code mình nộp.
```

## Khi bị trễ tiến độ

Ưu tiên:

```text
correct core
> meaningful tests
> readable code
> README/evidence
> extra features
```

Không “cứu deadline” bằng cách thêm code AI mà chưa kiểm chứng.
