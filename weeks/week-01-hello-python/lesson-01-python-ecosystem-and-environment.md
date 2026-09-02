# Buổi 1 — Bản đồ hệ sinh thái Python và chuẩn bị môi trường 🐍
> Trước khi cài một công cụ, hãy hiểu công cụ đó giải quyết vấn đề gì.
Buổi này giúp bạn nhìn thấy vai trò của Python, editor, terminal, Git, GitHub,
notebook cloud, trình quản lý môi trường và coding agent. Phần cài đặt chi tiết
chỉ nằm trong [`SETUP.md`](../../SETUP.md).
## Kết quả học tập
Sau buổi này, bạn có thể:
- phân biệt ngôn ngữ, runtime, editor và nền tảng cloud;
- giải thích Git khác GitHub như thế nào;
- phân biệt môi trường local với cloud;
- chọn standard path của Python Journey;
- nhận biết lúc nào công cụ tùy chọn thật sự hữu ích;
- kiểm tra Python và Git bằng terminal;
- chạy chương trình Python đầu tiên;
- xác định Python executable đang được sử dụng.
## 1. Bản đồ tổng thể

```text
                         BẠN
                          │
             viết code / chạy lệnh / yêu cầu
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       VS Code          Colab            Kaggle
        editor      cloud notebook    data/ML platform
          │               │                │
          ▼               ▼                ▼
        Python          Python           Python
   interpreter/runtime  runtime          runtime
          │
          ▼
   packages / libraries
          │
       pip / conda
          │
          ▼
      project files
          │
          ▼
         Git
          │
          ▼
        GitHub
Codex / coding agent
└── hỗ trợ đọc, giải thích, review, test và refactor repository
```
Các tầng không thay thế lẫn nhau:
- **Python** chạy code.
- **VS Code** giúp viết và debug code.
- **Terminal** là nơi gửi lệnh trực tiếp.
- **Git** lưu lịch sử thay đổi.
- **GitHub** lưu repository và hỗ trợ cộng tác.
- **Colab/Kaggle** cung cấp runtime trên cloud.
- **Conda** quản lý package và environment.
- **Codex** hỗ trợ công việc lập trình.
> **Understand the tool before installing the tool.**
## 2. Hai con đường công cụ
### STANDARD PATH — bắt buộc

```text
Python >= 3.12
VS Code
Python extension
Terminal
Git
GitHub account
```
Đây là con đường chính của Python Journey:

```text
Viết trong VS Code
        ↓
Chạy bằng Python local
        ↓
Kiểm tra bằng terminal
        ↓
Lưu lịch sử bằng Git
        ↓
Đưa bằng chứng lên GitHub
```
Nếu môi trường chưa sẵn sàng, làm theo [`SETUP.md`](../../SETUP.md).
Nếu đã có đủ công cụ, bạn có thể bỏ qua phần cài đặt nhưng vẫn cần hoàn thành
bản đồ khái niệm và các lab kiểm tra.
### OPTIONAL PATH — chỉ dùng khi có nhu cầu

```text
Jupyter
Colab
Kaggle
Anaconda / Miniconda
Codex
```
Bạn không cần cài tất cả trong Week 01. Công cụ tùy chọn chỉ nên được thêm khi
bài toán cần notebook, dataset, scientific package, cloud runtime hoặc hỗ trợ AI.
## 3. Python, interpreter và runtime
### Nó là gì?
Python là ngôn ngữ lập trình được học trong khóa này. File `.py` là văn bản
chứa code; interpreter đọc code đó và thực hiện lệnh.

```python
name = "An"
print(f"Xin chào {name}!")
```

```text
hello.py
   ↓
Python interpreter
   ↓
runtime thực hiện chương trình
   ↓
output hoặc traceback
```
### Nó giải quyết vấn đề gì?
Python cho phép mô tả logic để máy tính tính toán, xử lý dữ liệu, tự động hóa
và xây dựng ứng dụng.
### Có bắt buộc không?
Có. Baseline của khóa là:

```text
Python >= 3.12
```
Không cần cùng một patch version. Python 3.12.x, 3.13.x hoặc mới hơn đều đáp
ứng baseline nếu nội dung khóa hoạt động bình thường.
### Khi nào tôi nên dùng?
Dùng Python mỗi khi chạy bài tập, mini-project hoặc capstone của khóa.
## 4. VS Code và Terminal
### VS Code

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Code editor/development environment. |
| Nó giải quyết gì? | Viết code, tìm file, đọc lỗi, debug, dùng terminal và Git trong một giao diện. |
| Có bắt buộc không? | Có trong standard path của khóa. |
| Khi nào dùng? | Khi viết, chạy, debug và tổ chức project local. |
VS Code không thay thế Python interpreter:

```text
VS Code = bàn làm việc
Python  = động cơ chạy chương trình
```
Python extension giúp VS Code nhận interpreter, hỗ trợ syntax, chạy và debug
Python. Extension không tự biến VS Code thành Python runtime.
### Terminal

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Giao diện gửi lệnh trực tiếp cho hệ điều hành. |
| Nó giải quyết gì? | Chạy Python, Git và các công cụ project một cách rõ ràng, có thể lặp lại. |
| Có bắt buộc không? | Có. |
| Khi nào dùng? | Khi kiểm tra môi trường, chạy file, xem lỗi và làm việc với Git. |
Ban đầu chỉ cần hiểu một nhóm lệnh nhỏ:

```text
pwd / Get-Location    tôi đang ở đâu?
cd                    chuyển thư mục
ls / Get-ChildItem    trong đây có gì?
python / py / python3 chạy Python
git                   làm việc với Git
```
## 5. Git và GitHub
### Git

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Hệ thống quản lý phiên bản chạy trên máy của bạn. |
| Nó giải quyết gì? | Ghi lại thay đổi, lý do thay đổi và lịch sử project. |
| Có bắt buộc không? | Có. |
| Khi nào dùng? | Trong suốt quá trình học và phát triển project. |
Một commit là một mốc lịch sử có ý nghĩa:

```bash
git commit -m "feat: add first Python program"
```
### GitHub

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Nền tảng lưu repository và cộng tác. |
| Nó giải quyết gì? | Đồng bộ repository, review và chia sẻ bằng chứng học tập. |
| Có bắt buộc không? | Có tài khoản GitHub trong standard path. |
| Khi nào dùng? | Khi push tiến độ, chia sẻ hoặc cộng tác. |
Git và GitHub không phải một thứ:

```text
git commit
    ↓
local repository
    ↓
git push
    ↓
GitHub repository
```
Trong Python Journey, GitHub là nhật ký bằng chứng về quá trình học, không chỉ
là nơi nộp bài cuối cùng.
## 6. Local và cloud
### Local runtime
Code và Python chạy trên máy của bạn.
Ưu điểm:
- làm việc với project nhiều file;
- dùng editor, terminal và Git trực tiếp;
- kiểm soát environment;
- tiếp tục làm việc khi không có cloud runtime.
Đây là môi trường chính của Python Journey.
### Cloud runtime
Code chạy trên một máy từ xa do nền tảng cung cấp, thường qua trình duyệt.
Ưu điểm:
- bắt đầu notebook nhanh;
- dễ chia sẻ thí nghiệm;
- có thể dùng tài nguyên cloud;
- thuận tiện cho data science và machine learning.
Điểm cần nhớ:

```text
Cùng một đoạn Python
≠
luôn chạy trong cùng một máy hoặc cùng một environment
```
Runtime cloud có thể thay đổi version và package theo thời gian. Vì vậy,
environment và reproducibility vẫn quan trọng.
## 7. Notebook và nền tảng cloud

| Công cụ | Nó là gì? | Giải quyết vấn đề gì? | Bắt buộc? | Khi nên dùng? |
|---|---|---|---|---|
| **Jupyter Notebook** | Tài liệu gồm các cell code, kết quả và giải thích. | Khám phá dữ liệu, toán học, biểu đồ và thí nghiệm. | Không. | Khi cần làm việc tương tác theo từng cell. |
| **Google Colab** | Notebook chạy trên cloud trong browser. | Chạy và chia sẻ notebook mà không cần chuẩn bị đầy đủ runtime local. | Không. | Khi cần demo nhanh hoặc cloud notebook. |
| **Kaggle** | Nền tảng dataset, notebook, model và competition. | Đặt code cạnh dữ liệu và bài toán data/ML. | Không. | Khi làm việc với dataset, ML hoặc competition. |
Notebook không thay thế hoàn toàn file `.py`:

```text
.py       → con đường chính của khóa
Notebook  → công cụ bổ sung khi phù hợp
```
Colab và Kaggle không phải lab bắt buộc trong Week 01.
## 8. Conda, Anaconda và Miniconda
### Conda

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Công cụ quản lý package và environment. |
| Nó giải quyết gì? | Tách dependency và phiên bản giữa các project. |
| Có bắt buộc không? | Không. Python Journey dùng `venv` và `python -m pip`. |
| Khi nào dùng? | Khi workflow scientific/data cần conda package hoặc conda environment. |
### Anaconda

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Distribution gồm Python, conda và nhiều công cụ/package data science. |
| Nó giải quyết gì? | Cung cấp bộ scientific/data tools tích hợp. |
| Có bắt buộc không? | Không. |
| Khi nào dùng? | Khi muốn một distribution data science đầy đủ. |
### Miniconda

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | Distribution tối giản tập trung vào conda. |
| Nó giải quyết gì? | Bắt đầu với conda nhưng chỉ cài package cần thiết. |
| Có bắt buộc không? | Không. |
| Khi nào dùng? | Khi cần conda với môi trường gọn hơn Anaconda. |
Ý tưởng quan trọng:

```text
Project A → environment A → dependencies A
Project B → environment B → dependencies B
```
Không cài đồng thời nhiều Python distribution khi chưa hiểu chúng.
## 9. Codex và coding agent

| Câu hỏi | Trả lời |
|---|---|
| Nó là gì? | AI coding agent có thể làm việc với repository và công cụ phát triển. |
| Nó giải quyết gì? | Hỗ trợ đọc code, giải thích, review, test và refactor. |
| Có bắt buộc không? | Không. |
| Khi nào dùng? | Khi cần tutor, reviewer hoặc pair programmer có khả năng kiểm chứng. |
Codex có thể hỗ trợ:
- đọc repository và tìm file liên quan;
- giải thích code hoặc traceback;
- gợi ý test case;
- chạy test và đọc kết quả;
- review diff;
- hỗ trợ refactor có kiểm soát.
Codex không phải Python interpreter, compiler, Git hoặc sự thay thế cho hiểu biết
của người học.

```text
AI = tutor + reviewer + pair programmer
AI != replacement for understanding
```
Cách dùng tốt là yêu cầu giải thích, gợi ý, review và kiểm chứng. Không nộp code
do AI tạo ra nếu bạn không thể giải thích và tự kiểm tra nó.
## 10. Chọn công cụ theo nhu cầu

| Tôi muốn... | Công cụ phù hợp |
|---|---|
| Chạy một chương trình Python | Python + Terminal |
| Viết và debug project | VS Code + Python |
| Lưu lịch sử code | Git |
| Đồng bộ và cộng tác | GitHub |
| Làm notebook tương tác local | Jupyter |
| Mở notebook nhanh trên cloud | Colab |
| Làm việc với dataset/ML/competition | Kaggle |
| Quản lý scientific environment bằng conda | Miniconda hoặc Anaconda |
| Nhờ AI đọc, review và test repository | Codex |
Môi trường tốt không phải môi trường có nhiều công cụ nhất:

```text
ít
+
hiểu rõ
+
có thể tái tạo
```
## 11. Lab kiểm tra nhẹ
Các lab sau xác nhận standard path. Chúng không thay thế hướng dẫn cài đặt trong
[`SETUP.md`](../../SETUP.md).
### LAB 1 — Kiểm tra Python
Trong Windows PowerShell hoặc Terminal:

```powershell
python --version
```
Nếu command `python` chưa được nhận trên Windows, thử launcher:

```powershell
py --version
```
Trên macOS/Linux, command thường là:

```bash
python3 --version
```
Kết quả phải là Python 3.12 hoặc mới hơn. Nếu chưa đạt, quay lại
[`SETUP.md`](../../SETUP.md).
### LAB 2 — Kiểm tra Git

```bash
git --version
```
Bạn cần thấy một version của Git thay vì thông báo “command not found”.
### LAB 3 — Chạy chương trình đầu tiên
Tạo file `hello.py`:

```python
print("Hello, Python Journey!")
```
Chạy bằng command hoạt động trên máy của bạn:

```bash
python hello.py
```
Trên Windows có thể dùng:

```powershell
py hello.py
```
Trên macOS/Linux có thể dùng:

```bash
python3 hello.py
```
Kết quả:

```text
Hello, Python Journey!
```
### LAB 4 — Xác định Python executable
Tạo file `where_is_python.py`:

```python
import sys
print(sys.version)
print(sys.executable)
```
Chạy file và quan sát:
- version Python;
- đường dẫn executable;
- executable trong terminal có trùng interpreter VS Code đang chọn không.
Đây là bước đầu để hiểu environment, không phải bài cấu hình nâng cao.
### OPTIONAL EXPLORATION — Local và cloud
Nếu muốn khám phá thêm, chạy đoạn sau ở local và trong Colab hoặc Kaggle:

```python
import platform
import sys
print(platform.system())
print(sys.version)
print(sys.executable)
```
So sánh kết quả để thấy chương trình đang chạy trên các máy/environment khác
nhau. Phần này hoàn toàn tùy chọn.
## 12. Checklist hoàn thành Buổi 1
- [ ] Tôi giải thích được Python và interpreter/runtime.
- [ ] Tôi phân biệt được Python với VS Code.
- [ ] Tôi phân biệt được Git với GitHub.
- [ ] Tôi hiểu local runtime khác cloud runtime.
- [ ] Tôi biết Anaconda, Miniconda và conda dùng khi nào.
- [ ] Tôi biết Colab và Kaggle không phải công cụ bắt buộc.
- [ ] Tôi hiểu Codex hỗ trợ gì và không nên làm thay điều gì.
- [ ] Python 3.12+ chạy được.
- [ ] Git chạy được.
- [ ] `hello.py` chạy được.
- [ ] Tôi xác định được Python executable.
## Bản đồ ghi nhớ

```text
Python
│
├── Local — standard path
│   ├── VS Code + Python extension
│   ├── Terminal
│   ├── venv / pip
│   └── Git → GitHub
│
├── Data environment — optional
│   ├── conda
│   ├── Anaconda
│   └── Miniconda
│
├── Cloud notebook — optional
│   ├── Colab
│   └── Kaggle
│
└── AI-assisted development — optional
    └── Codex
```
## Kết quả đầu ra

```text
ENVIRONMENT_MAP_UNDERSTOOD = YES
PYTHON_AVAILABLE = YES
TERMINAL_AVAILABLE = YES
GIT_AVAILABLE = YES
FIRST_PROGRAM_RUN = YES
PYTHON_EXECUTABLE_IDENTIFIED = YES
```
Buổi tiếp theo:
> **Hello Python — từ câu lệnh đầu tiên đến chương trình đầu tiên có output và lỗi để debug.**
