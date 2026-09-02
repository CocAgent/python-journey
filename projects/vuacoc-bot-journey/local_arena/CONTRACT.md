# Course-local Line Arena Contract

> This is a Python Journey teaching contract. It is not the production
> contract of vuacoc.com.

```text
COURSE_LOCAL_ARENA = YES
COURSE_LOCAL_STATE_SCHEMA = YES
COURSE_LOCAL_ACTION_SCHEMA = YES
VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED
```

## Bot interface

```python
def choose_action(state):
    ...
```

Arena truyền một dictionary mới cho mỗi lời gọi. Bot trả một string action.
Không yêu cầu class, inheritance hoặc hidden state.

## State schema

Đây là course-local state nhìn từ một bot:

| Key | Meaning |
|---|---|
| `turn` | turn hiện tại, bắt đầu từ 1 |
| `max_turns` | giới hạn do engine sở hữu |
| `position` | vị trí của bot trên line |
| `opponent_position` | vị trí bot còn lại |
| `goal` | endpoint bot đang hướng tới |
| `min_position` | luôn là 0 trong model này |
| `max_position` | luôn là 4 trong model này |

## Action schema

```text
left
right
wait
```

`left` giảm position một đơn vị, `right` tăng một đơn vị, `wait` giữ nguyên.
Transition luôn clamp vào range `0..4`.

## Match and terminal behavior

Hai bot nhận view từ cùng state trước turn. Engine validate cả action trước khi
transition. Một bot đạt goal thì thắng; cả hai đạt goal cùng turn thì hòa; hết
`max_turns` thì result là hòa với reason `max_turns_reached`.

## Fail-closed behavior

- Action ngoài local set tạo `status="bot_failure"`; bot còn lại thắng.
- Exception từ bot tạo `status="bot_failure"`; tên exception và message được
  ghi trong reason, không bị nuốt im lặng.
- Strategy luôn trả `wait` vẫn kết thúc vì engine sở hữu `max_turns`.
- Một function thật sự không return không thể được giới hạn an toàn trong cùng
  process; không chạy code không tin cậy.

## Replay

Mỗi completed transition ghi turn number, state trước action, action của bot A,
action của bot B và state sau action.

```text
COURSE LOCAL FORMAT
NOT VUACOC PRODUCTION FORMAT
```

Contract này không đề xuất endpoint, authentication, timeout, submission
protocol, rating, production replay schema hoặc SDK.
