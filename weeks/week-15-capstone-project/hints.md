# Hints — Week 15

Rubric và deliverables canonical: [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## Chốt scope

- Viết một câu problem statement trước khi viết code.
- Liệt kê rõ phần **out-of-scope**; đây là bằng chứng bạn kiểm soát phạm vi.
- Bốn chức năng chạy tốt tốt hơn tám chức năng dở dang.

## Phân rã code

- Tách I/O (input/print) khỏi logic tính toán để test được phần logic.
- Hàm nào cần comment dài để giải thích thường nên tách thành hai hàm.

## Testing

- Mỗi chức năng chính cần ít nhất một normal case và một edge case.
- Test invalid input: chuỗi rỗng, số âm, file chưa tồn tại, dữ liệu hỏng.
- Test đang fail mà bạn hiểu nguyên nhân là known limitation — ghi vào README.

## Debugging evidence

- Giữ lại một bug đã sửa: triệu chứng, minimal failing input, nguyên nhân, cách sửa.
- Đây là mục bạn sẽ được hỏi khi demo.

## README

- Người đọc phải chạy được project chỉ bằng README, không hỏi thêm.
- Có setup, usage, ví dụ input/output, design decision và known limitations.
- Bắt đầu từ [capstone README template](../../templates/capstone-readme-template.md).

## Trước khi handoff

- Chạy readiness check trong [`checks/`](checks/).
- `git status` sạch, không commit secret hoặc file tạm.
