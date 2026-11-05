# Architecture — VuaCóc Bot Journey

## Design lock

Kiến trúc giữ decision logic độc lập với cách game hoặc arena giao tiếp:

```text
Game / Arena
    ↓ state
Bot Core
    ↓ action
Adapter
    ↓
Game / Arena
```

Golden rule:

```text
BOT LOGIC MUST NOT DEPEND DIRECTLY ON NETWORK/API
```

## Các lớp trách nhiệm

### Bot Core

- Chứa decision logic xác định hoặc gần pure function khi phù hợp.
- Nhận state và trả action qua contract nội bộ của course.
- Không gọi network trực tiếp.
- Có thể test không cần server hoặc production runtime.

Điểm bắt đầu ở Week 07:

```python
def choose_action(state):
    ...
```

### Arena Adapter

- Chuyển dữ liệu giữa runtime và bot core.
- Chịu trách nhiệm serialization, protocol và network nếu contract chính thức
  sau này yêu cầu.
- Không chứa strategy rules.

```text
ARENA_ADAPTER = DESIGN_ONLY
```

Không triển khai production adapter cho đến khi runtime contract được xác minh.

### Evaluation

- Thu nhận kết quả match.
- Lưu replay hoặc course-local evidence.
- Tổng hợp metrics đã được định nghĩa cho môi trường local.
- Không giả định rating algorithm production.

## Luồng phụ thuộc

```text
runtime input
    ↓ adapter boundary
course state
    ↓ bot core
course action
    ↓ adapter boundary
runtime output
```

Bot core không import hoặc biết chi tiết transport. Adapter có thể phụ thuộc bot
core, nhưng bot core không phụ thuộc ngược lại adapter.

## Tiến hóa tới composition

Week 14 có thể bọc strategy bằng một object nhỏ:

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)
```

Nguyên tắc là **composition before inheritance**. Basic inheritance chỉ được
dùng khi có quan hệ mô hình rõ và giúp người học hiểu hơn; không xây class
hierarchy để tạo vẻ phức tạp.

## Boundary với nội dung nâng cao

Kiến trúc này không giới thiệu multi-agent framework, machine learning,
reinforcement learning, MCTS, distributed agents hoặc LLM orchestration. Nhiều
bot độc lập trong một tournament local vẫn là evidence giáo dục hợp lệ.
