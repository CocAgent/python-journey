# Buổi 1 — Bản đồ hệ sinh thái Python và chuẩn bị môi trường 🐍

> Trước khi viết chương trình đầu tiên, hãy hiểu **mình đang dùng công cụ nào và công cụ đó làm nhiệm vụ gì**.

Một trong những nhầm lẫn phổ biến nhất của người mới học Python là nghĩ:

> Python, Anaconda, VS Code, Colab, Kaggle, Jupyter và Codex đều là những cách khác nhau để “chạy Python”.

Điều đó chỉ đúng một phần.

Mỗi công cụ nằm ở **một tầng khác nhau**.

---

# 1. Bản đồ tổng thể

Hãy hình dung hệ sinh thái như sau:

```text
                         BẠN
                          │
                          ▼
                 ┌─────────────────┐
                 │  Viết / yêu cầu │
                 └────────┬────────┘
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       VS Code          Colab            Kaggle
       Editor         Cloud Notebook    Data/ML Platform
          │               │                │
          ▼               ▼                ▼
        Python          Python           Python
      Interpreter      Runtime           Runtime
          │
          ▼
   Packages / Libraries
          │
     pip / conda
          │
          ▼
      Project files
          │
          ▼
         Git
          │
          ▼
        GitHub

Codex / AI Agent
      │
      └── hỗ trợ đọc, viết, kiểm tra và cải tiến code
```

Điều quan trọng:

> **Python là ngôn ngữ và runtime.
> VS Code là nơi viết code.
> Git lưu lịch sử.
> GitHub lưu và cộng tác trên repository.
> Colab/Kaggle cung cấp máy chạy trên cloud.
> Anaconda quản lý một hệ sinh thái Python/data science.
> Codex là trợ lý/agent hỗ trợ lập trình.**

---

# 2. Python là gì?

Python là ngôn ngữ lập trình mà chúng ta học trong khóa này.

Ví dụ:

```python
name = "An"
print(f"Xin chào {name}!")
```

Nhưng một file `.py` chỉ là **văn bản chứa code**.

Để máy tính thực sự chạy nó, chúng ta cần một **Python interpreter**.

Ví dụ:

```bash
python hello.py
```

Có thể hiểu đơn giản:

```text
hello.py
   ↓
Python interpreter
   ↓
máy tính thực hiện lệnh
   ↓
kết quả
```

## Trong Python Journey

Baseline của khóa:

```text
Python >= 3.12
```

Không cần chạy đúng cùng một patch version.

Điều quan trọng là code của khóa hoạt động trên các phiên bản Python hiện đại được hỗ trợ.

---

# 3. Kiểm tra Python đã được cài chưa

Mở Terminal / PowerShell / Git Bash.

Chạy:

```bash
python --version
```

hoặc trên Windows:

```bash
py --version
```

Kết quả mong đợi có dạng:

```text
Python 3.12.x
```

hoặc mới hơn.

Ví dụ:

```text
Python 3.13.x
Python 3.14.x
```

đều phù hợp với baseline khóa học.

---

# 4. Python và VS Code khác nhau thế nào?

## Python

Python **chạy chương trình**.

## VS Code

VS Code là một **code editor / development environment** giúp chúng ta:

- viết code;
- tô màu cú pháp;
- tìm file;
- chạy chương trình;
- đọc lỗi;
- debug;
- dùng terminal;
- làm việc với Git;
- cài extension.

Có thể hình dung:

```text
VS Code = bàn làm việc
Python = động cơ chạy chương trình
```

VS Code không thay thế Python.

Nếu chỉ cài VS Code mà không có Python interpreter, máy tính vẫn chưa thể chạy chương trình Python local.

---

# 5. Thiết lập VS Code cho Python

Cài:

```text
1. Visual Studio Code
2. Python
3. Python extension trong VS Code
```

Sau đó mở một folder, ví dụ:

```text
python-journey/
```

Tạo:

```text
hello.py
```

với nội dung:

```python
print("Hello, Python Journey!")
```

Chạy trong terminal:

```bash
python hello.py
```

Kết quả:

```text
Hello, Python Journey!
```

Đây là bằng chứng đầu tiên rằng:

```text
EDITOR = OK
PYTHON = OK
TERMINAL = OK
```

---

# 6. Terminal là gì và tại sao phải học?

Terminal cho phép chúng ta nói chuyện trực tiếp với hệ điều hành bằng lệnh.

Ví dụ:

```bash
python hello.py
```

```bash
git status
```

```bash
cd python-journey
```

Nhiều người mới cố tránh terminal vì nghĩ nó “quá kỹ thuật”.

Trong khóa này chúng ta làm ngược lại:

> Học một lượng terminal nhỏ nhưng đủ dùng ngay từ đầu.

Bạn không cần thuộc hàng trăm command.

Ban đầu chỉ cần hiểu:

```text
pwd      tôi đang ở đâu?
cd       chuyển thư mục
ls       trong đây có gì?
python   chạy Python
git      làm việc với Git
```

---

# 7. Git là gì?

Git lưu lại **lịch sử thay đổi của project**.

Ví dụ:

```text
Version 1
hello.py

      ↓ sửa

Version 2
hello.py + calculator.py

      ↓ sửa bug

Version 3
calculator fixed
```

Git giúp trả lời:

```text
Tôi đã thay đổi gì?
Thay đổi khi nào?
Tại sao?
File trước đây trông như thế nào?
```

Một commit có thể giống:

```bash
git commit -m "feat: add first Python program"
```

---

# 8. GitHub là gì?

Git và GitHub không phải một thứ.

```text
Git
= hệ thống quản lý phiên bản

GitHub
= nền tảng lưu repository và cộng tác
```

Flow cơ bản:

```text
Máy của bạn
     │
     │ git commit
     ▼
Local repository
     │
     │ git push
     ▼
GitHub
```

Trong Python Journey, GitHub không chỉ là nơi nộp bài.

Nó là **nhật ký bằng chứng về quá trình học**.

---

# 9. Jupyter Notebook là gì?

Trong file Python thông thường:

```text
program.py
```

chương trình thường được chạy như một file.

Notebook lại chia công việc thành các **cell**:

```text
Cell 1
code

Cell 2
kết quả

Cell 3
giải thích

Cell 4
biểu đồ
```

Notebook đặc biệt hữu ích cho:

- khám phá dữ liệu;
- toán học;
- visualization;
- machine learning;
- thí nghiệm;
- giảng dạy.

Nhưng notebook không thay thế hoàn toàn `.py`.

Trong khóa này:

```text
.py       → con đường chính
Notebook  → công cụ bổ sung khi phù hợp
```

---

# 10. Anaconda là gì?

Anaconda **không phải một ngôn ngữ lập trình mới**.

Anaconda Distribution là một bộ môi trường tập trung mạnh vào:

```text
Python
conda
Jupyter
data science packages
machine learning packages
environment management
```

Nó giúp người dùng data science cài nhiều thư viện dễ hơn.

Ví dụ:

```text
numpy
pandas
matplotlib
scikit-learn
Jupyter
```

có thể được quản lý trong cùng hệ sinh thái.

---

# 11. Conda là gì?

`conda` là công cụ quản lý:

```text
packages
+
environments
```

Ví dụ, bạn có thể tạo:

```text
Environment A
Python 3.12
numpy
pandas

Environment B
Python 3.14
không có pandas
```

Hai môi trường không cần làm ảnh hưởng nhau.

Đây là ý tưởng rất quan trọng:

> **Một project nên có môi trường dependency riêng.**

---

# 12. Có bắt buộc cài Anaconda không?

**Không.**

Python Journey sử dụng con đường chuẩn:

```text
Python
+
venv
+
python -m pip
```

Anaconda/Miniconda là **con đường tùy chọn**, đặc biệt hữu ích khi học tiếp:

```text
Data Science
Machine Learning
Scientific Computing
```

Không nên yêu cầu một học viên mới cài đồng thời nhiều Python distribution mà chưa hiểu chúng.

---

# 13. Colab là gì?

Google Colab cung cấp notebook chạy trên cloud.

Điểm khác lớn so với VS Code local:

```text
VS Code
code ở máy bạn
Python chạy trên máy bạn

Colab
notebook mở trong browser
Python chạy trên runtime cloud
```

Điều đó có nghĩa:

> Bạn có thể thử Python mà không cần chuẩn bị đầy đủ môi trường local.

Colab rất hữu ích cho:

- notebook;
- demo nhanh;
- chia sẻ bài;
- data science;
- machine learning;
- môi trường lớp học.

---

# 14. Có phải cài Colab không?

Không.

Colab chủ yếu được sử dụng qua trình duyệt.

Flow:

```text
Browser
   ↓
Colab Notebook
   ↓
Cloud Runtime
   ↓
Python
```

Vì runtime cloud có thể được cập nhật theo thời gian, một notebook cũ không nên giả định mọi version thư viện luôn giống nhau.

Đây cũng là lý do sau này chúng ta học:

```text
dependency
version
environment
reproducibility
```

---

# 15. Kaggle là gì?

Kaggle là một nền tảng tập trung mạnh vào:

```text
Datasets
Notebooks
Machine Learning
Competitions
Models
Community
```

Kaggle Notebook cũng cho phép chạy Python trên cloud.

Nhưng Kaggle có thêm một điểm rất mạnh:

> **Code được đặt ngay cạnh dữ liệu và các bài toán thực tế.**

Ví dụ một workflow sau này có thể là:

```text
Kaggle Dataset
      ↓
Kaggle Notebook
      ↓
pandas
      ↓
analysis
      ↓
machine learning model
      ↓
evaluation
```

---

# 16. Colab và Kaggle khác nhau thế nào?

Có thể nhớ đơn giản:

| Công cụ | Phù hợp nhất khi |
|---|---|
| **Colab** | Muốn mở notebook nhanh và chạy Python trên cloud |
| **Kaggle** | Muốn notebook + dataset + machine learning + competition |

Cả hai đều rất hữu ích.

Nhưng trong Python Journey:

```text
Local Python + VS Code
```

vẫn là môi trường học chính.

---

# 17. Codex là gì?

Codex là một AI coding agent.

Nó không phải:

```text
Python interpreter
compiler
replacement for Git
replacement for understanding code
```

Codex có thể hỗ trợ những công việc như:

```text
đọc repository
tìm file liên quan
giải thích code
đề xuất thay đổi
sửa nhiều file
chạy test
đọc lỗi
review diff
hỗ trợ refactor
```

Điểm khác với chatbot đơn thuần là một coding agent có thể làm việc với **repository và công cụ phát triển**.

---

# 18. Có nên dùng AI khi đang học Python?

Có — nhưng phải dùng đúng cách.

## Cách dùng tốt

Hỏi:

> “Giải thích traceback này cho tôi.”

> “Đừng viết lời giải. Hãy cho tôi một gợi ý.”

> “Test case nào tôi còn thiếu?”

> “Đoạn code này có bug ở đâu? Hãy giúp tôi tự tìm.”

> “So sánh hai cách viết này.”

## Cách dùng kém

Hỏi:

> “Làm toàn bộ bài tập này cho tôi.”

rồi copy kết quả mà không hiểu.

Trong Python Journey:

```text
AI = tutor + reviewer + pair programmer
AI ≠ người học thay bạn
```

---

# 19. Bộ công cụ nào bắt buộc trong khóa?

## Bắt buộc

```text
Python >= 3.12
VS Code
Python extension
Terminal
Git
GitHub account
```

Đây là **STANDARD PATH**.

---

## Tùy chọn

```text
Jupyter
Colab
Kaggle
Anaconda / Miniconda
Codex
```

Không cần cài tất cả trong Buổi 1.

---

# 20. Khi nào dùng công cụ nào?

Hãy dùng câu hỏi sau:

### Tôi chỉ muốn chạy một chương trình Python?

```text
Python + Terminal
```

### Tôi muốn viết/debug project?

```text
VS Code + Python
```

### Tôi muốn lưu lịch sử code?

```text
Git
```

### Tôi muốn đưa project lên Internet và cộng tác?

```text
GitHub
```

### Tôi muốn thử notebook ngay trong browser?

```text
Colab
```

### Tôi muốn làm việc với dataset/ML/competition?

```text
Kaggle
```

### Tôi muốn quản lý scientific/data environments bằng conda?

```text
Miniconda / Anaconda
```

### Tôi muốn AI hỗ trợ đọc, sửa, test repository?

```text
Codex
```

---

# 21. Một nguyên tắc rất quan trọng: đừng cài mọi thứ

Người mới thường nghĩ:

> “Càng cài nhiều công cụ thì môi trường càng chuyên nghiệp.”

Không đúng.

Môi trường tốt là:

```text
ít
+
hiểu rõ
+
reproducible
```

Buổi đầu chỉ cần đạt:

```text
Python works
VS Code works
Terminal works
Git works
GitHub works
```

Các công cụ còn lại sẽ được giới thiệu khi có bài toán cần chúng.

---

# 22. Lab 1 — Kiểm tra môi trường

Chạy:

```bash
python --version
```

```bash
git --version
```

Sau đó tạo:

```text
hello.py
```

với:

```python
print("Hello, Python Journey!")
```

Chạy:

```bash
python hello.py
```

Kết quả:

```text
Hello, Python Journey!
```

---

# 23. Lab 2 — Python đang chạy ở đâu?

Tạo:

```python
import sys

print(sys.version)
print(sys.executable)
```

Chạy chương trình.

Quan sát:

```text
Python version
Python executable path
```

Câu hỏi:

> Python mà VS Code đang sử dụng có phải Python mà terminal đang sử dụng không?

Đây là câu hỏi đầu tiên giúp bạn hiểu vấn đề **environment**.

---

# 24. Lab 3 — Local và Cloud

Chạy cùng đoạn code:

```python
import platform
import sys

print(platform.system())
print(sys.version)
```

ở:

```text
Máy local
```

và sau đó thử trên:

```text
Google Colab
```

Quan sát sự khác biệt.

Mục tiêu:

> Hiểu rằng cùng là Python nhưng chương trình có thể chạy trên **hai máy khác nhau**.

---

# 25. Lab 4 — GitHub là bằng chứng

Sau chương trình đầu tiên:

```bash
git status
```

Sau đó:

```bash
git add hello.py
```

```bash
git commit -m "feat: complete first Python program"
```

Nếu repository đã cấu hình remote:

```bash
git push
```

Chu trình đầu tiên đã hoàn thành:

```text
Learn
  ↓
Build
  ↓
Run
  ↓
Check
  ↓
Commit
  ↓
Prove
```

---

# 26. Bạn đã hoàn thành Buổi 1 khi nào?

Không phải khi bạn “đã cài hết phần mềm”.

Bạn hoàn thành khi có thể trả lời:

- [ ] Python là gì?
- [ ] Python khác VS Code ở đâu?
- [ ] Git khác GitHub ở đâu?
- [ ] Local runtime khác cloud runtime thế nào?
- [ ] Anaconda khác Python như thế nào?
- [ ] Colab và Kaggle dùng cho tình huống nào?
- [ ] Codex có thể hỗ trợ gì và không nên làm thay điều gì?
- [ ] `python --version` chạy được.
- [ ] `git --version` chạy được.
- [ ] `hello.py` chạy được.
- [ ] Có ít nhất một commit Git.

---

# 27. Bản đồ ghi nhớ cuối buổi

```text
Python
│
├── chạy code
│
├── Local
│   ├── Terminal
│   ├── VS Code
│   ├── venv / pip
│   └── Git → GitHub
│
├── Data environment
│   ├── conda
│   └── Anaconda / Miniconda
│
├── Cloud Notebook
│   ├── Colab
│   └── Kaggle
│
└── AI-assisted development
    └── Codex
```

Hãy nhớ:

> **Không cần biết mọi công cụ ngay hôm nay.
> Quan trọng là biết mỗi công cụ giải quyết vấn đề gì.**

---

## Kết quả đầu ra của Buổi 1

```text
ENVIRONMENT_MAP_UNDERSTOOD = YES
PYTHON_AVAILABLE = YES
EDITOR_AVAILABLE = YES
TERMINAL_AVAILABLE = YES
GIT_AVAILABLE = YES
FIRST_PROGRAM_RUN = YES
FIRST_COMMIT_CREATED = YES
```

Buổi tiếp theo:

> **Hello Python — từ câu lệnh đầu tiên đến chương trình đầu tiên có input, output và lỗi để debug.**
