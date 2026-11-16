# Mini-project — Collection Workflow

Model ba bước công việc bằng list các tuple `(title, status)`.

## Yêu cầu

- thêm, cập nhật và xóa item trong list;
- unpack một tuple để hiển thị title và status;
- chứng minh alias và copy khác nhau;
- không cần loop hoặc comprehension trong core evidence.

```bash
python weeks/week-05-lists-tuples/mini-project/starter.py
```

## Bài đệm trước Collection Workflow

Nếu còn nhầm alias với copy hoặc chưa quen unpack tuple,
hãy đọc [3 ví dụ bổ sung](../WORKED-EXAMPLES.md), tự hoàn thiện
[bài tập tương tự](../practice/README.md) rồi mới quay lại project.

Khi `tasks` là **list các tuple**, có thể thay `tasks[1]`
bằng một tuple khác, nhưng không thể gán `tasks[1][1] = "done"`.
Thử dự đoán trạng thái `tasks` và `copied_tasks` trước khi
chạy để hiểu snapshot một lớp.
