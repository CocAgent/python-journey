# Tuần 01 — Environment · REPL · Terminal · Git/GitHub · Hello Python 🐍

> Học công cụ đủ dùng, viết chương trình đầu tiên, kiểm chứng rồi lưu bằng chứng.

## Mục tiêu tuần

Sau Week 01, bạn có thể:

- phân biệt Python, interpreter/runtime, VS Code, terminal, Git và GitHub;
- chọn standard path thay vì cài mọi công cụ;
- kiểm tra Python >= 3.12 và Git từ terminal;
- dùng Python REPL và chạy file `.py`;
- sử dụng `print()`, comment và biểu thức số học cơ bản;
- đọc thông tin lỗi đầu tiên thay vì bỏ qua;
- tạo commit có ý nghĩa và đưa bằng chứng lên GitHub.

## Thứ tự học

1. **Environment map** — đọc
   [`lesson-01-python-ecosystem-and-environment.md`](lesson-01-python-ecosystem-and-environment.md).
2. **Setup nếu cần** — làm theo [`SETUP.md`](../../SETUP.md) khi Python, VS Code,
   Python extension, terminal hoặc Git chưa sẵn sàng.
3. **Python fundamentals** — đọc [`notes.md`](notes.md).
4. **Exercises** — hoàn thành ba file trong [`exercises/`](exercises/).
5. **Mini-project** — xây ASCII Art Generator theo
   [`mini-project/README.md`](mini-project/README.md).
6. **Commit evidence** — review thay đổi, commit tiến độ và push lên GitHub.

> Đã có Python 3.12+ và Git? Bạn có thể bỏ qua thao tác cài đặt, nhưng vẫn cần
> hiểu environment map và chạy các lệnh kiểm tra.

## Standard path của Week 01

```text
Python >= 3.12
VS Code + Python extension
Terminal
Git
GitHub
```

Jupyter, Colab, Kaggle, Anaconda/Miniconda và Codex là tùy chọn. Không cần cài
các công cụ này để hoàn thành Week 01.

## Bài tập

Mở thư mục [`exercises/`](exercises/) và hoàn thành theo thứ tự:

1. [`ex01_hello.py`](exercises/ex01_hello.py) — in lời chào sáng tạo.
2. [`ex02_calculator.py`](exercises/ex02_calculator.py) — dùng Python để tính toán.
3. [`ex03_input.py`](exercises/ex03_input.py) — trò chuyện với người dùng.

Mỗi file có TODO hướng dẫn. Hãy tự làm trước khi xem [`solutions/`](solutions/).

## Mini-project — ASCII Art Generator

Tạo chương trình nhận tên người dùng và in một hình ASCII có ý nghĩa.

Yêu cầu và starter nằm tại
[`mini-project/README.md`](mini-project/README.md).

## Commit evidence

Trước khi commit:

```bash
git status
git diff
```

Chỉ stage file bạn đã chủ động thay đổi. Dùng message mô tả kết quả, ví dụ:

```bash
git commit -m "feat: complete Week 01 Python exercises"
```

Nếu repository đã cấu hình remote, push branch học tập của bạn lên GitHub.
Không commit secret, virtual environment hoặc file tạm.

## Đọc thêm

| Nguồn | Nội dung |
|---|---|
| [Think Python — Chapter 1](https://allendowney.github.io/ThinkPython/chap01.html) | Programming as a way of thinking |
| [Python Tutorial](https://docs.python.org/3/tutorial/) | Tài liệu Python chính thức |
| [Git documentation](https://git-scm.com/doc) | Khái niệm và command Git |

## Checklist cuối tuần

- [ ] Hiểu bản đồ công cụ và standard path.
- [ ] Python 3.12+ và Git chạy được từ terminal.
- [ ] Xác định được Python executable.
- [ ] Đọc `notes.md`.
- [ ] Hoàn thành `ex01_hello.py`.
- [ ] Hoàn thành `ex02_calculator.py`.
- [ ] Hoàn thành `ex03_input.py`.
- [ ] Hoàn thành mini-project.
- [ ] Review thay đổi trước khi commit.
- [ ] Commit và push bằng chứng lên GitHub.
- [ ] Cập nhật [`PROGRESS.md`](../../PROGRESS.md).
