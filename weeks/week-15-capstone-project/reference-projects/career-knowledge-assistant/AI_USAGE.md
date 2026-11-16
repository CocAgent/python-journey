# AI Usage — reference example

Đây là **mẫu minh bạch AI cho mã tham khảo**, không phải báo cáo của sinh viên.

## AI hỗ trợ gì?

- Hỗ trợ hình thành kiến trúc ứng dụng, ví dụ, tài liệu, test cases.
- Hỗ trợ review contract và các đường lỗi.

## Phần cần người học tự làm

- Chọn tính năng mới trong PROJECT_CHALLENGES.md.
- Tự giải thích và sửa code service/adapter.
- Tự viết test cho thay đổi và chạy trên máy mình.
- Giải thích trade-off khi bảo vệ.

## Kiểm chứng như thế nào?

```bash
python -m pytest -q
python -m career_assistant --help
```

Không coi câu trả lời AI hay kết quả ghi trong README là bằng chứng chạy thật.
Người học tự ghi command, commit, bug, test thực tế và giới hạn còn tồn tại.
