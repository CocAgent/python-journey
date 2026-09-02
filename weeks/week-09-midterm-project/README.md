# Tuần 09 — Midterm Project

Midterm trả lời một câu hỏi: bạn có thể kết hợp nền tảng Week 01–08 thành một
project Python nhỏ, chạy ổn định và giải thích được không?

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Outcomes

Sau Week 09, bạn có thể:

- lập kế hoạch một project vừa sức;
- chia project thành các function có trách nhiệm rõ;
- dùng structured data thay cho nhiều biến rời rạc;
- chạy normal case và boundary case;
- đọc output để tìm và sửa lỗi;
- đánh giá behavior bằng evidence thay vì cảm giác;
- ghi lại commit, bug, cách sửa và known weakness.

## Prerequisites

Hoàn thành Week 01–08 và machine checks của Week 07–08 trước khi bắt đầu.

## Chọn track

Xem [`tracks/README.md`](tracks/README.md):

1. **VuaCóc Bot V1** — flagship track dùng structured state và Local Arena.
2. **Student Manager** — track thay thế giữ bài toán quản lý học sinh legacy.

Hai track dùng cùng tiêu chí về planning, decomposition, correctness và
evidence. Bạn chỉ cần hoàn thành một track.

## Learning path

```text
choose → plan → decompose → implement → run
       → inspect → debug → evaluate → explain → commit
```

1. Đọc [`notes.md`](notes.md).
2. Chọn brief trong [`tracks/`](tracks/).
3. Copy hoặc hoàn thiện artifact phù hợp trong [`starter/`](starter/).
4. Chạy project nhiều lần với các case đã lên kế hoạch.
5. Dùng [`evidence-template.md`](evidence-template.md) để ghi bằng chứng.
6. Chạy [machine check](checks/README.md) cho reference artifacts.
7. Commit project bằng message có ý nghĩa.

## Evaluation

Đánh giá dựa trên project có chạy, dữ liệu và rules có giải thích được, case đã
kiểm tra, bug đã sửa và evidence đã lưu. Không có yêu cầu win-rate cho bot.

Week 09 milestone: [Midterm Bot V1](../../projects/vuacoc-bot-journey/milestones/w09-midterm-bot-v1.md).

## Definition of done

- [ ] Project chạy local bằng một command được ghi trong README.
- [ ] Core behavior được chia thành function.
- [ ] Structured state được dùng có chủ đích.
- [ ] Normal và boundary cases hoàn tất.
- [ ] Một bug và cách sửa được ghi lại.
- [ ] Một known weakness được ghi lại.
- [ ] Evidence template có commit SHA.
- [ ] Không có global state không cần thiết.
