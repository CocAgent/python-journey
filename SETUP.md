# Hướng dẫn cài đặt môi trường

> `SETUP.md` là nguồn chân lý duy nhất cho installation và troubleshooting của Python Journey.

Baseline của khóa:

```text
Python >= 3.12
```

Standard path:

```text
Python
VS Code
Python extension
Terminal
Git
GitHub account
```

Jupyter, Colab, Kaggle, Anaconda/Miniconda và Codex là công cụ tùy chọn. Không
cần cài tất cả để bắt đầu.

## 1. Kiểm tra trước khi cài

Có thể máy của bạn đã có đủ công cụ. Hãy kiểm tra trước.

### Windows — PowerShell hoặc Command Prompt

```powershell
python --version
py --version
git --version
```

Bạn chỉ cần một trong hai launcher `python` hoặc `py` chạy đúng Python 3.12+.
Không cần cả hai command cùng hoạt động.

### macOS/Linux — Terminal

```bash
python3 --version
git --version
```

Nếu Python đạt 3.12+ và Git trả về version, bạn có thể chuyển tới phần VS Code
và virtual environment.

## 2. Windows

### 2.1 Cài Python

1. Mở [python.org/downloads](https://www.python.org/downloads/).
2. Chọn Python 3.12 hoặc mới hơn cho Windows.
3. Chạy installer. Cho phép installer thêm Python vào `PATH` nếu tùy chọn đó
   xuất hiện.
4. Đóng terminal cũ, mở terminal mới.
5. Kiểm tra:

```powershell
python --version
```

Nếu command trên chưa được nhận, thử Python Launcher:

```powershell
py --version
```

Kết quả cần là Python 3.12 hoặc mới hơn.

### 2.2 Cài VS Code và Python extension

1. Cài VS Code từ [code.visualstudio.com](https://code.visualstudio.com/).
2. Mở Extensions bằng `Ctrl+Shift+X`.
3. Tìm extension **Python** do Microsoft phát hành.
4. Chọn **Install**.
5. Mở Command Palette bằng `Ctrl+Shift+P`.
6. Chọn **Python: Select Interpreter** và chọn Python 3.12+ vừa kiểm tra.

### 2.3 Cài Git

1. Cài Git for Windows từ [git-scm.com/download/win](https://git-scm.com/download/win).
2. Mở terminal mới.
3. Kiểm tra:

```powershell
git --version
```

## 3. macOS

### 3.1 Cài hoặc nâng cấp Python

Kiểm tra trước:

```bash
python3 --version
```

Nếu version thấp hơn 3.12, chọn một nguồn được duy trì:

- installer chính thức tại [python.org/downloads/macos](https://www.python.org/downloads/macos/); hoặc
- Homebrew với công thức không khóa minor version:

```bash
brew install python
```

Sau khi cài, mở terminal mới và xác nhận:

```bash
python3 --version
```

### 3.2 Cài VS Code và Python extension

1. Cài VS Code từ [code.visualstudio.com](https://code.visualstudio.com/).
2. Cài extension **Python** do Microsoft phát hành.
3. Dùng **Python: Select Interpreter** để chọn Python 3.12+.

### 3.3 Cài Git

Kiểm tra:

```bash
git --version
```

Nếu Git chưa có, làm theo hướng dẫn chính thức của
[Git for macOS](https://git-scm.com/download/mac) hoặc công cụ quản lý package
bạn đã chọn. Kiểm tra lại `git --version` sau khi cài.

## 4. Linux

Tên package và version Python phụ thuộc distribution và release. Không giả định
mọi Ubuntu/Debian repository đều cung cấp cùng một minor version.

1. Kiểm tra:

```bash
python3 --version
git --version
```

2. Nếu thiếu Python, dùng tài liệu package chính thức của distribution để cài
   Python 3, module `venv` và `pip`.
3. Nếu Python thấp hơn 3.12, xem nguồn cài đặt được distribution hỗ trợ hoặc
   hướng dẫn chính thức tại [python.org/downloads/source](https://www.python.org/downloads/source/).
4. Cài VS Code theo
   [hướng dẫn Linux chính thức](https://code.visualstudio.com/docs/setup/linux).
5. Cài extension **Python** do Microsoft phát hành và chọn interpreter 3.12+.
6. Kiểm tra lại:

```bash
python3 --version
git --version
```

Chỉ dùng quyền quản trị cho package manager của hệ điều hành khi tài liệu chính
thức của distribution yêu cầu. Không dùng `sudo` để sửa lỗi `pip` hoặc `venv`
một cách mặc định.

## 5. Tạo virtual environment

Chạy trong thư mục project.

### Windows với `python`

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

### Windows với `py`

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

Nếu PowerShell chặn activation script, có thể mở Command Prompt và dùng:

```bat
.venv\Scripts\activate.bat
```

Không cần thay đổi execution policy toàn máy chỉ để bắt đầu khóa học.

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python --version
```

Khi environment được kích hoạt, command `python` cần trỏ tới executable trong
`.venv`. Kiểm tra trực tiếp:

```bash
python -c "import sys; print(sys.executable)"
```

Thoát environment bằng:

```bash
deactivate
```

## 6. Clone repository và bắt đầu

```bash
git clone https://github.com/CocAgent/python-journey.git
cd python-journey
```

Mở repository trong VS Code, sau đó đọc theo thứ tự:

1. [`README.md`](README.md)
2. [`SETUP.md`](SETUP.md)
3. [`weeks/week-01-hello-python/README.md`](weeks/week-01-hello-python/README.md)

Nếu command `code` đã có trong `PATH`:

```bash
code .
```

## 7. Troubleshooting

### Terminal không nhận Python

- Đóng và mở terminal sau khi cài.
- Trên Windows, thử cả `python --version` và `py --version`.
- Trên macOS/Linux, dùng `python3 --version`.
- Kiểm tra lại lựa chọn interpreter trong VS Code.
- Nếu version thấp hơn 3.12, quay lại hướng dẫn theo hệ điều hành ở trên.

### VS Code dùng sai Python

1. Mở Command Palette.
2. Chọn **Python: Select Interpreter**.
3. Chọn executable trong `.venv` nếu project đã có virtual environment.
4. Mở terminal mới trong VS Code và kiểm tra version.

### Lỗi quyền truy cập khi tạo environment hoặc cài package

Xác định command, thư mục và environment đang gây lỗi trước. Kích hoạt virtual
environment và cài package vào đó. Không thêm `sudo` vào lệnh `pip`/`venv` như
một giải pháp tổng quát.

### Tiếng Việt hiển thị sai

Python 3 dùng UTF-8 cho source code theo mặc định. Hãy phân biệt:

- **source encoding** — cách file `.py` được lưu;
- **file I/O encoding** — encoding khi chương trình đọc/ghi dữ liệu;
- **terminal/display encoding** — cách terminal hiển thị ký tự.

Trong Week 01, hãy lưu file bằng UTF-8 và kiểm tra terminal. Khi học file I/O,
sử dụng rõ `encoding="utf-8"` với `open(...)` khi phù hợp.

## 8. Checklist xác nhận

- [ ] Python 3.12+ chạy bằng command phù hợp với hệ điều hành.
- [ ] VS Code đã được cài.
- [ ] Python extension do Microsoft phát hành đã được cài.
- [ ] VS Code chọn đúng interpreter.
- [ ] Terminal chạy được Python.
- [ ] Git trả về version.
- [ ] GitHub account sẵn sàng.
- [ ] Virtual environment tạo và kích hoạt được.
- [ ] Repository đã được clone và mở đúng thư mục.
