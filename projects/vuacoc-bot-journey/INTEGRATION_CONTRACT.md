# VuaCóc Integration Contract — Verification Ledger

```text
VUACOC_RUNTIME_CONTRACT = UNVERIFIED
ARENA_ADAPTER = DESIGN_ONLY
PRODUCTION_INTEGRATION = NO
LOCAL_ARENA_IMPLEMENTED = YES
```

Tài liệu này là ledger các câu hỏi cần đo từ nguồn chính thức hoặc code/runtime
thật. `NOT_MEASURED` không phải placeholder implementation và không cho phép
suy đoán contract.

Local Arena implementation dùng contract riêng trong
[`local_arena/CONTRACT.md`](local_arena/CONTRACT.md). Sự tồn tại của local arena
không cung cấp bằng chứng cho bất kỳ production ledger item nào bên dưới.

## STATE_SCHEMA

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## ACTION_SCHEMA

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## LEGAL_ACTION_RULES

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## TURN_PROTOCOL

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## TIME_LIMIT

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## ERROR_PROTOCOL

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## AUTH

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## BOT_SUBMISSION_FORMAT

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## MATCH_API

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## REPLAY_FORMAT

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## RATING_EXPOSURE

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

## SDK

```text
STATUS = NOT_MEASURED
SOURCE = NONE
```

Chỉ đổi một mục sang trạng thái khác khi có source có thể kiểm tra. Mọi teaching
schema, action set, replay hoặc adapter trong course phải tiếp tục gắn nhãn
course-local và không được trình bày như production contract.

```text
DO_NOT_IMPLEMENT_PRODUCTION_ADAPTER
UNTIL CONTRACT IS VERIFIED
```
