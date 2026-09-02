# Course-local Line Arena

> This is a Python Journey teaching contract. It is not the production
> contract of vuacoc.com.

Line Arena là môi trường turn-based rất nhỏ để biến decision function thành
một match có replay và result. Nó không mô phỏng full VuaCóc game và không
claim fidelity hay compatibility với production.

Thư mục dùng tên `local_arena` thay vì `local-arena` để là một Python module có
thể import trực tiếp.

## Pipeline

```text
Student Bot
   ↓
Local Arena
   ↓
Baseline Bots
   ↓
Match
   ↓
Replay
   ↓
Evaluation
```

```text
COURSE_LOCAL_ONLY = YES
COURSE_LOCAL_ARENA = YES
VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED
NETWORK_CALLS = 0
SECRETS = 0
```

## Game at a glance

- Line positions: `0..4`.
- Bot A starts at `0` and aims for `4`.
- Bot B starts at `4` and aims for `0`.
- Local actions: `left`, `right`, `wait`.
- Both actions are applied from the same pre-turn state.
- Positions are independent; sharing a position does not block movement.
- A bot wins by reaching its goal; otherwise the engine stops at `max_turns`.

The full course-local schema and failure behavior are in [`CONTRACT.md`](CONTRACT.md).

## Run from repository root

Stable example:

```bash
python projects/vuacoc-bot-journey/local_arena/examples/run_match.py
```

CLI smoke test:

```bash
python projects/vuacoc-bot-journey/local_arena/cli.py --bot-a forward --bot-b wait --replay
```

Available selections are `wait`, `forward`, `cautious` and `student`. CLI
syntax is infrastructure, not a Week 07 learning objective.

## Security boundary

> Local Arena is not a security sandbox. Do not run untrusted Python code.

The arena calls a Python function in the current process. It does not use
`eval`, execute learner strings, spawn a process, download code or isolate an
untrusted bot.
