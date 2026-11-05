# Tuần 15 — Capstone · Integrate · Prove · Defend

Tuần cuối không phải lúc bắt đầu một project mới. Đây là lúc biến những gì bạn đã
xây thành một sản phẩm **chạy được, kiểm chứng được và giải thích được**.

```text
Scope lock
→ Integrate
→ Test & debug
→ Document & prove
→ Demo & defend
```

## Nguồn chân lý

Yêu cầu, deliverables và rubric duy nhất của capstone nằm tại
[FINAL_PROJECT.md](../../FINAL_PROJECT.md).

Week 15 **không tạo rubric thứ hai**, không đặt quota class/hàm/file và không
biến VuaCóc Bot thành đề tài bắt buộc.

## Outcomes

Sau Week 15, bạn có thể:

- chốt scope vừa sức và nói rõ phần không làm;
- hoàn thiện một vertical slice end-to-end;
- chạy test, sửa regression và ghi known limitations;
- tạo evidence từ test, debugging và Git history;
- viết README đủ để người khác chạy lại;
- giải thích một quyết định thiết kế và một trade-off;
- demo/bảo vệ code của chính mình trong 5–8 phút;
- mô tả cách đã dùng và kiểm chứng AI nếu có.

## Learning path

1. Đọc [kế hoạch thực thi](execution-plan.md) và chốt scope.
2. Hoàn thiện luồng chính trước khi thêm feature phụ.
3. Dùng [integration checklist](notes.md) để test/debug.
4. Có thể dùng [evidence template](evidence-template.md) để gom bằng chứng.
5. Chạy readiness checker.
6. Chuẩn bị [demo & defense](demo-defense.md).
7. Commit trạng thái cuối với worktree sạch.

Các template hỗ trợ:

- [Capstone README template](../../templates/capstone-readme-template.md)
- [AI usage template](../../templates/AI_USAGE.template.md)

## Readiness checker

Chạy từ repository root:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py path/to/my-project
```

Checker mặc định chỉ kiểm **evidence cơ học**:

- README có các phần cốt lõi;
- có `AI_USAGE.md`;
- Python source parse được;
- có ít nhất 5 test function;
- pytest collect được;
- không có bare `except:`.

Nó **không chấm chất lượng thiết kế** và không suy điểm rubric.

Sau khi tự tin với project của chính mình, có thể chạy cả tests:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py \
  path/to/my-project --run-tests
```

Không dùng `--run-tests` cho code không tin cậy.

## Definition of ready

Trước khi demo:

- [ ] Luồng chính chạy được từ command ghi trong README.
- [ ] Các chức năng nghiệp vụ đã chốt đều có evidence.
- [ ] Ít nhất 5 test có ý nghĩa và test suite PASS.
- [ ] Có ít nhất một bug đã tái hiện, sửa và kiểm tra lại.
- [ ] README mô tả scope, cách chạy, test, cấu trúc và limitations.
- [ ] `AI_USAGE.md` phản ánh đúng cách dùng AI.
- [ ] Git history cho thấy quá trình build/test/debug/improve.
- [ ] Bạn giải thích được code mà không phụ thuộc vào AI.
- [ ] `git status` sạch khi handoff.

## Flagship optional track — VuaCóc Bot Journey

[VuaCóc Bot Journey](../../projects/vuacoc-bot-journey/README.md) có thể dùng
làm capstone nếu bạn đã phát triển bot từ Week 07.

W15 của track này là **integration + tournament + evidence**, không phải bắt đầu
bot từ đầu. Local tournament/replay chỉ là course-local evidence và không chứng
minh tương thích production VuaCóc.

## Dự án tham khảo chạy được — Career Knowledge Assistant

[Career Knowledge Assistant](reference-projects/career-knowledge-assistant/README.md)
là ứng dụng Python/SQLite hoàn chỉnh để sinh viên **cài đặt, chạy, test,
đọc code và tự mở rộng**. Bản cơ sở chạy offline bằng CLI; sinh viên có thể
chọn phát triển API với FastAPI hoặc dashboard với Streamlit.

- Có mã nguồn đầy đủ, test, tài liệu setup và AI disclosure.
- Có [challenges](reference-projects/career-knowledge-assistant/PROJECT_CHALLENGES.md)
  cho các hướng backend, automation, data và agent foundations.
- Không bắt buộc chọn đề tài này và **không thay thế**
  [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## Hướng phát triển nghề nghiệp — Commerce & Marketing

Sinh viên muốn tiếp tục MVP Week 09 thành capstone có thể xem
[13 nguồn mở Commerce & Marketing](../week-09-midterm-project/project-ideas/commerce-marketing-open-source.md),
trong đó có Saleor (commerce API), ERPNext/Odoo (quản trị doanh nghiệp),
PostHog/Umami (analytics) và Mautic (marketing automation).
Ví dụ nâng cấp: giỏ hàng + quản lý tồn kho hoặc dashboard conversion rate,
thêm lưu dữ liệu, validation, pytest và CLI/API adapter tùy chọn.

Đây là **hướng tham khảo**, không bắt buộc cài hệ thống gốc và không thay
[FINAL_PROJECT.md](../../FINAL_PROJECT.md). Không dùng thẻ thanh toán,
dữ liệu khách hàng thật hay gửi marketing thật trong bài mẫu.
