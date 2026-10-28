# Midterm Week 09 — 3-Agent Python Workflow

## Mục tiêu
MVP Python thuần chạy offline theo đề tài **#18 OpenAI Agents SDK (Python)** trong danh mục CocAgent. Ba vai trò **Planner → Developer → Reviewer** lần lượt chia bước, mô phỏng công việc, và kiểm tra tính đầy đủ. Đây là **mô phỏng deterministic, KHÔNG phải ba LLM/AI agent thực sự**. Developer không sinh code hoặc chạy lệnh.

## Nguồn tham khảo
- [Danh mục 20 dự án Week 09 — mục #18](https://github.com/CocAgent/python-journey/blob/main/weeks/week-09-midterm-project/project-ideas/catalog-20-du-an.md)
- [OpenAI Agents SDK — mã nguồn](https://github.com/openai/openai-agents-python)
- [Tài liệu chính thức](https://openai.github.io/openai-agents-python/)
- [Rubric 10 điểm](https://github.com/CocAgent/python-journey/blob/main/weeks/week-09-midterm-project/project-ideas/rubric-10-diem.md)

Đây là mã tự viết lấy cảm hứng từ ý tưởng orchestration, **không sao chép SDK** và **không phụ thuộc SDK/API key**. Hướng nâng cấp sau W15: thay các hàm mô phỏng bằng Agent/Runner, thêm tool có kiểm soát và approval.

## Yêu cầu
Python 3.12+; Windows PowerShell/VS Code. Không cần Internet khi chạy chương trình chính.

## Chạy
Từ thư mục gốc repo:

```powershell
cd projects/midterm-3-agent
python main.py
```

Nhập: `Tao nhan vat di chuyen 2D`.
Kết quả: 3 bước kế hoạch, 3 dòng mô phỏng và `passed: True`.

## Kiểm thử
```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
```
Có 6 test cho đường chạy thường, input rỗng, plan rỗng, thiếu bước, sai thứ tự và status sai. Kết quả chỉ được công nhận sau khi chạy thực tế.

## Input / output và trường hợp biên
- Input: chuỗi yêu cầu không rỗng.
- Output: dict chứa task, plan, work, report.
- Input biên: chuỗi rỗng/khoảng trắng → ValueError, CLI in lỗi.
- Hạn chế: không hiểu ngữ nghĩa yêu cầu, không tạo game, không gọi LLM, reviewer chỉ so khớp bước và trạng thái.

## Kiến trúc
- `planner.py:plan_task` kiểm tra input và tạo 3 bước.
- `developer.py:develop` tạo nhật ký mô phỏng.
- `reviewer.py:review` so sánh kế hoạch với nhật ký.
- `main.py:run_pipeline` điều phối; `main` cung cấp CLI.

## An toàn, ghi công và minh chứng
Không đọc/ghi file dự án khác, không thực thi code sinh tự động, không yêu cầu secret. Chỉ dùng dữ liệu giả. Để nộp: lưu output terminal thực tế, commit SHA, lỗi đã sửa, và ảnh demo vào evidence.md. Không tuyên bố PASS khi chưa kiểm tra thực tế.
