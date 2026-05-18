# Hướng dẫn cài đặt môi trường

## 1. Cài đặt Python

### Windows
1. Truy cập [python.org/downloads](https://python.org/downloads)
2. Tải Python 3.11 hoặc mới hơn
3. **Quan trọng**: Tích chọn **"Add Python to PATH"** khi cài đặt
4. Xác nhận: mở Command Prompt → `python --version`

### macOS
```bash
# Dùng Homebrew (khuyến nghị)
brew install python@3.11

# Xác nhận
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
python3 --version
```

## 2. Cài đặt VS Code

1. Tải tại [code.visualstudio.com](https://code.visualstudio.com)
2. Cài đặt bình thường
3. Mở VS Code → Extensions (Ctrl+Shift+X) → Tìm **"Python"** → Install
4. Khuyến nghị thêm: **"Python Indent"**, **"autopep8"**

## 3. Tạo Virtual Environment

```bash
# Tạo venv (chạy 1 lần)
python -m venv .venv

# Kích hoạt (chạy mỗi khi mở terminal)
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Xác nhận
which python  # Phải trỏ vào .venv
```

## 4. Clone repo và bắt đầu

```bash
git clone https://github.com/CocAgent/python-journey.git
cd python-journey
cd weeks/week-01-hello-python
cat README.md
```

## 5. Cấu trúc thư mục làm việc

```
python-journey/
├── weeks/
│   ├── week-01-hello-python/
│   │   ├── README.md       ← Đọc trước
│   │   ├── notes.md        ← Kiến thức chi tiết
│   │   ├── exercises/      ← Bài tập (có TODO)
│   │   ├── solutions/      ← Lời giải (đừng peek!)
│   │   └── mini-project/   ← Dự án nhỏ cuối tuần
│   ├── week-02-.../
│   └── ...
├── PROGRESS.md             ← Đánh dấu tiến trình
├── SETUP.md                ← File này
└── README.md               ← Tổng quan khóa học
```

## Troubleshooting

**`python` không nhận trên Windows?** → Thử `python3` hoặc `py`

**Permission denied trên macOS/Linux?** → Thêm `sudo` trước lệnh cài đặt

**VS Code không nhận Python?** → Ctrl+Shift+P → "Python: Select Interpreter" → Chọn Python 3.11

**Lỗi encoding khi in tiếng Việt?** → Thêm `# -*- coding: utf-8 -*-` ở đầu file, hoặc dùng `encoding="utf-8"` khi đọc/ghi file
