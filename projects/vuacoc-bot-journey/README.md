# VuaCóc Bot Journey

VuaCóc Bot Journey là project xuyên khóa để người học nâng cấp cùng một hệ
thống ra quyết định từ Week 07 đến Week 15. Người học không gặp `functions`,
`dict`, JSON, exceptions, `pytest`, modules và OOP như những chương rời rạc:
mỗi chủ đề làm bot **more capable, more reliable, more explainable**.

Đây là một spiral project, không phải project chỉ bắt đầu ở tuần cuối:

```text
Observe state
   ↓
Choose action
   ↓
Run match
   ↓
Inspect result
   ↓
Test/debug
   ↓
Improve
```

Learning loop xuyên suốt:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Hành trình W07–W15

| Week | Milestone | Điều bot học thêm |
|---|---|---|
| W07 | [Function Bot](milestones/w07-function-bot.md) | quyết định xác định bằng function |
| W08 | [State + Heuristic](milestones/w08-state-and-heuristic.md) | state có cấu trúc và rule dễ giải thích |
| W09 | [Midterm Bot V1](milestones/w09-midterm-bot-v1.md) | ghép các phần thành bot chạy local |
| W10 | [Replay + Data](milestones/w10-replay-and-data.md) | lưu evidence bằng file, JSON và CSV |
| W11 | [Robust Bot](milestones/w11-robustness-and-debugging.md) | phân biệt lỗi phần mềm với thua chiến thuật |
| W12 | [Tested Bot](milestones/w12-testing-with-pytest.md) | khóa hành vi bằng regression tests |
| W13 | [Adapter Boundary](milestones/w13-modules-cli-arena-adapter.md) | tách bot core khỏi runtime adapter |
| W14 | [Strategy Composition](milestones/w14-strategy-composition.md) | thay strategy mà không viết lại core |
| W15 | [Capstone Tournament](milestones/w15-capstone-tournament.md) | tích hợp, đánh giá, giải thích và demo |

Xem [bảng milestone](MILESTONES.md), [kiến trúc](ARCHITECTURE.md),
[evaluation](EVALUATION.md) và [trạng thái integration contract](INTEGRATION_CONTRACT.md).

## Phạm vi của track

VuaCóc Bot Journey là **flagship capstone track**: một lộ trình nổi bật giúp
kết nối các tuần thành một câu chuyện phát triển liên tục. Đây không phải lựa
chọn capstone bắt buộc duy nhất. Mọi capstone vẫn dùng yêu cầu và rubric
canonical trong [`FINAL_PROJECT.md`](../../FINAL_PROJECT.md).

Python Journey chỉ đi đến nhiều bot độc lập cùng tham gia môi trường chung,
match, tournament và evaluation. Reinforcement learning, self-play training,
MCTS chuyên sâu, opponent modeling nâng cao, LLM agent orchestration và hệ
thống agent phân tán nằm ngoài phạm vi khóa học.

## Trạng thái integration

```text
VUACOC_RUNTIME_CONTRACT = UNVERIFIED
ARENA_ADAPTER = DESIGN_ONLY
PRODUCTION_INTEGRATION = NO
```

Các milestone hiện dùng teaching models và local evidence. Không nội dung nào
trong thư mục này được xem là contract runtime chính thức của VuaCóc.
