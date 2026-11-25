# Bài nộp Week 01 — Trương Gia Hiên

Trương Gia Hiên · MSSV: 2125110165 · Lớp: CCQ2511E

Bài nộp riêng cho PR #254, dựa trên giáo trình `d6192585ff13b9f204e1d441898ddd1d86b472ae`. Giữ nguyên từng dòng đề/comment trong bản sao và thêm lời giải dưới TODO. Các starter chung ngoài thư mục này được giữ nguyên.

- `exercises/`: hai bài cốt lõi và bài input mở rộng.
- `mini-project/starter_basic.py`: khung ASCII tĩnh.
- `mini-project/starter.py`: khung nhập tên mở rộng.

Từ thư mục gốc repository, chạy bài bằng Python 3.12+:

```powershell
$env:PYTHONUTF8 = '1'
python weeks/week-01-hello-python/submissions/2125110165/exercises/ex01_hello.py
python weeks/week-01-hello-python/submissions/2125110165/exercises/ex02_calculator.py
python weeks/week-01-hello-python/submissions/2125110165/exercises/ex03_input.py
python weeks/week-01-hello-python/submissions/2125110165/mini-project/starter_basic.py
python weeks/week-01-hello-python/submissions/2125110165/mini-project/starter.py
```

## Tự kiểm bằng máy chấm gốc

Máy chấm Week 01 tìm file theo cấu trúc `weeks/week-01-hello-python/...`. Tạo bản sao tạm được Git bỏ qua để chấm đúng bài nộp mà vẫn giữ starter chung:

```powershell
$submission = 'weeks/week-01-hello-python/submissions/2125110165'
$checkRoot = '.learner-output/check-2125110165-week01'
$weekFolder = Join-Path $checkRoot 'weeks/week-01-hello-python'
New-Item -ItemType Directory -Force -Path $weekFolder | Out-Null
Copy-Item -LiteralPath "$submission/exercises", "$submission/mini-project" -Destination $weekFolder -Recurse -Force
python -m assessment grade --week 01 --submission $checkRoot --acknowledge-local-code
```

Kết quả tự kiểm đã chạy: **5/5**, 11/11 tiêu chí. Phần minh chứng và điểm chính thức chờ giảng viên đánh giá. Báo cáo máy chấm được giữ ở local.
