# Week 15 — Integration checklist

Canonical requirements và rubric:
[FINAL_PROJECT.md](../../FINAL_PROJECT.md).

Tài liệu này giúp thực thi capstone; nó không thêm tiêu chí chấm điểm mới.

## 1. Scope lock

Trước khi code tiếp, viết:

- một câu problem statement;
- danh sách chức năng đã chốt;
- phần **out-of-scope**;
- điều kiện “done” cho luồng chính.

Nếu còn feature mới chưa cần cho luồng chính, đưa vào “future improvement”.

## 2. Integrate một vertical slice

Ưu tiên một luồng end-to-end:

```text
input
→ core logic
→ persistence/output
→ visible result
```

Một vertical slice chạy ổn định có giá trị hơn nhiều module chưa nối được.

## 3. Test và debug

Chạy lại các nhóm case phù hợp:

```text
normal
boundary
empty
invalid
regression
```

Khi gặp bug:

```text
Reproduce
→ Minimal failing input
→ Locate
→ Fix
→ Re-test
→ Add/adjust regression test
```

Phân biệt:

- **software defect**: behavior sai so với contract;
- **known limitation**: giới hạn đã hiểu và ghi rõ;
- **future feature**: chưa thuộc scope hiện tại.

Không che lỗi bằng `except: pass`.

## 4. Evidence pack

Evidence tốt trả lời được:

- Tôi đã chạy command nào?
- Test nào chứng minh behavior chính?
- Bug nào đã sửa?
- Commit nào thể hiện thay đổi quan trọng?
- Known limitation nào còn lại?
- Nếu dùng AI, tôi kiểm chứng output bằng cách nào?

Có thể dùng [evidence-template.md](evidence-template.md). Đây là template hỗ
trợ, không phải deliverable bắt buộc mới.

## 5. README

Người review phải có thể chạy project chỉ từ README.

README nên trả lời:

1. Project giải quyết vấn đề gì?
2. Scope/chức năng chính là gì?
3. Setup và chạy thế nào?
4. Test thế nào?
5. Cấu trúc/module chính làm gì?
6. Quyết định thiết kế/trade-off nào đáng chú ý?
7. Known limitations là gì?

## 6. Git/GitHub evidence

Commit message nên nói được intent, ví dụ:

```text
feat: persist transactions to json
test: cover empty expense list
fix: reject negative amount
docs: document known limitations
```

Không cần nhiều commit giả tạo. Cần history phản ánh tiến trình thật.

Trước handoff:

```bash
git status
git log --oneline --decorate -10
```

## 7. Optional VuaCóc local tournament

Nếu chọn flagship track:

```bash
python projects/vuacoc-bot-journey/local_arena/tournament_cli.py
```

Ghi lại:

- điều kiện tournament;
- kết quả local;
- replay/evidence;
- một strength;
- một weakness;
- một improvement tiếp theo.

Không suy từ kết quả local sang production VuaCóc.

## 8. Demo/defense

Dùng [demo-defense.md](demo-defense.md) để chuẩn bị 5–8 phút.

Mục tiêu không phải slide đẹp. Mục tiêu là chứng minh:

```text
I built it
I tested it
I debugged it
I understand it
```
