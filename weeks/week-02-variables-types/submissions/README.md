# Week 02 — Bài làm sinh viên được tách biệt (không phải lời giải chuẩn)

Mục đích của thư mục này là lưu **bản sao bài nộp có nguồn gốc rõ ràng** để giảng viên phản biện, không để bài làm sinh viên ghi đè ba tệp `exercises/` gốc của giáo trình.

**Không coi đây là đáp án, bài mẫu chính thức hoặc minh chứng đã đạt điểm.** Bài làm có thể có lỗi và vẫn phải được đánh giá. Không đưa thư mục này vào các fixture `assessment/core-exercises/fixtures/reference/` hoặc chạy tự động trong GitHub Actions.

Ví dụ cấu trúc bài nộp:

```text
weeks/week-02-variables-types/
├── exercises/                 # Đề gốc CHUNG, giữ nguyên TODO để người mới thực hành
├── assessment/core-exercises/  # Bộ kiểm của giảng viên, không sửa theo bài nộp
└── submissions/
    ├── README.md
    └── pr-251/
        ├── README.md           # Nguồn gốc, phạm vi, ghi nhận đánh giá
        └── exercises/
            ├── ex01_variables.py
            ├── ex02_type_conversion.py
            └── ex03_input_calc.py
```

Bài nộp riêng chỉ được đưa vào đây khi có quyền sử dụng/phản biện thích hợp. Sinh viên tiếp tục làm bài trên fork hoặc bản sao của mình; không sửa file chung hay đưa file kết quả riêng, khóa API, thông tin cá nhân chưa kiểm soát vào Git. Ví dụ đang công khai được trích trực tiếp từ [PR #251](https://github.com/CocAgent/python-journey/pull/251).

### Quy trình kiểm tra

1. **Kiểm toán toàn bộ tập test trước:** từ gốc repository dùng `python weeks/week-02-variables-types/assessment/core-exercises/grader.py --audit-tests` (không thực thi bài sinh viên).
2. **Chỉ khi đã xác nhận source tin cậy và có môi trường cách ly phù hợp**, mới cân nhắc chạy `grader.py --student --submission ... --acknowledge-local-code`; không chạy bài nộp chưa tin cậy trên server, CI có secrets hay máy giảng viên chứa dữ liệu thật.
3. Mọi kết quả là điểm **tự luyện**, `official_score=null`. Lời giải đúng nhưng khác khuôn kiểm AST/stdout cần giảng viên xem lại.

Không dùng giải pháp `git merge` trực tiếp một PR do học viên tạo trên bản sao đã xóa/sửa hàng trăm file của khóa học.
