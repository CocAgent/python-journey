# Hints — Week 15

Rubric và deliverables canonical:
[FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## Chốt scope

- Viết problem statement trong một câu.
- Nêu rõ out-of-scope.
- Bốn chức năng nghiệp vụ chạy tốt tốt hơn tám chức năng dở dang.
- Không thêm class, file hay dependency chỉ để “trông chuyên nghiệp”.

## Khi project quá lớn

Cắt theo thứ tự:

1. bỏ UI phụ;
2. bỏ feature không ảnh hưởng luồng chính;
3. giữ persistence đơn giản;
4. giữ test cho logic cốt lõi;
5. giữ README và evidence.

Không cắt testing/debugging để cứu feature phụ.

## Phân rã code

- Tách I/O khỏi logic để phần logic test được.
- Mỗi hàm nên có một trách nhiệm rõ.
- Đừng hiểu “phân rã” thành quota số hàm.
- Class chỉ dùng khi state + behavior thực sự thuộc cùng một mô hình.

## Testing

Ưu tiên test behavior:

- normal case;
- boundary/empty;
- invalid input;
- regression của bug từng gặp.

Một test chỉ kiểm `True is True` không tạo evidence.

## Debugging evidence

Giữ lại một câu chuyện bug ngắn:

```text
Symptom
→ minimal failing input
→ root cause
→ fix
→ regression test
```

Đây là phần rất mạnh khi bảo vệ.

## AI usage

AI có thể hỗ trợ giải thích, review, gợi ý test và debugging.

Trước khi dùng output AI:

- đọc và giải thích lại bằng lời của bạn;
- chạy test/command kiểm chứng;
- thử ít nhất một edge case;
- bỏ phần bạn không hiểu hoặc không phù hợp.

Nếu giảng viên thay một input hoặc yêu cầu nhỏ mà bạn không sửa được code của
mình, evidence AI usage chưa đạt mục tiêu học tập.

## Demo

Đừng demo mọi feature.

Chọn một flow đại diện:

```text
setup/run
→ main behavior
→ one edge case
→ tests
→ one bug/design decision
```

Nếu demo live lỗi, đọc traceback và giải thích cách bạn sẽ isolate lỗi tốt hơn
việc cố che màn hình.

## Trước handoff

- chạy readiness check;
- chạy test suite;
- đọc README như người mới;
- kiểm tra không có secret/file tạm;
- `git status` sạch;
- chuẩn bị câu trả lời cho “Tại sao bạn thiết kế như vậy?”.
