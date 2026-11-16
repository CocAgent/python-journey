# Week 15 — Sinh viên tự kiểm tra: Capstone — tích hợp và bảo vệ

> Hướng dẫn tự học dùng **mã của chính sinh viên**. PASS của bài mẫu không phải điểm của bạn. Checker chỉ kiểm phần ghi bên dưới; giảng viên vẫn quyết định điểm học phần.

## 1. Chuẩn bị

Mở [README của tuần](../README.md), đọc notes, ví dụ và yêu cầu bài tập. Cài Python >=3.12 và mở Terminal ở thư mục gốc `python-journey`. Trên Windows có thể dùng `py`, trên macOS/Linux thường dùng `python3` thay cho `python`. Tải toàn bộ repository (ZIP hoặc Git), không chỉ một tệp `.py`.

**Phạm vi checker:** Kiểm readiness cơ học; rubric duy nhất tại FINAL_PROJECT.md.

**Hai hoạt động cần tự quan sát:** Hoàn thiện luồng chính, README, AI_USAGE, ít nhất 5 test. Demo project, ghi bug và regression, bảo vệ thiết kế.

## 2. Tự kiểm readiness của capstone

**Nguồn chân lý:** [FINAL_PROJECT.md](../../../FINAL_PROJECT.md) — không thêm rubric điểm mới. Chốt scope theo [execution plan](../execution-plan.md), làm luồng chính, viết README, `AI_USAGE.md` và test. Xem [evidence template](../evidence-template.md) và [demo/defense](../demo-defense.md).

Ở gốc repository, thay `path/to/my-project` bằng thư mục dự án thực tế của bạn:

```bash
python -m assessment guide --week 15
python -m assessment selfcheck --week 15 --project path/to/my-project --acknowledge-local-code
```

Checker kiểm cấu trúc README, AI_USAGE, cú pháp, ít nhất năm hàm test, pytest collect và bare except. **pytest --collect-only có thể thực thi code khi import**: chỉ chạy với project tin cậy. Không có điểm tự động cho thiết kế, demo hay chất lượng tư duy.

Muốn chạy thêm test thật (chỉ với code bạn tin cậy):

```bash
python -m assessment selfcheck --week 15 --project path/to/my-project --run-tests --acknowledge-local-code
```

Xuất JSON riêng tư trên máy (không tự upload):

```bash
python -m assessment selfcheck --week 15 --project path/to/my-project --acknowledge-local-code --json-out .learner-output/week15.json
```

`auto_score` và `official_score` vẫn là `null`. PASS readiness **không phải đạt capstone**. Demo, bảo vệ và rubric `FINAL_PROJECT.md` vẫn bắt buộc.

## 3. Trước khi nộp

- [ ] Scope, luồng chính, test và README đúng spec.
- [ ] Có AI_USAGE, bug/regression và known weakness.
- [ ] Demo, bảo vệ và chứng minh mã do mình làm; không dùng dữ liệu thật nhạy cảm.

Xem [mẫu minh chứng chung](../../../assessment/EVIDENCE-TEMPLATE.md) cùng [mẫu của capstone](../evidence-template.md).
