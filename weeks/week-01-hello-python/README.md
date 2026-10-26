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

Nếu thích học qua câu chuyện, đọc tùy chọn
[Giới thiệu Python](../../assets/Story-00-Giới%20thiệu%20Python.md) và
[Hello Python](../../assets/Story-01-Hello%20Python.md) trước khi bắt đầu.

1. **Environment map** — đọc
   [`lesson-01-python-ecosystem-and-environment.md`](lesson-01-python-ecosystem-and-environment.md).
2. **Setup nếu cần** — làm theo [`SETUP.md`](../../SETUP.md) khi Python, VS Code,
   Python extension, terminal hoặc Git chưa sẵn sàng.
3. **Python fundamentals** — đọc [`notes.md`](notes.md).
4. **Examples** — chạy thử ba file trong [`examples/`](examples/) để thấy
   `print()`, phép toán và traceback đầu tiên hoạt động thế nào.
5. **Exercises** — làm hai bài cốt lõi trong [`exercises/`](exercises/), xem [đề và đáp án kiểm tra](exercises/README.md).
   `ex03_input.py` là **bài chuẩn bị Tuần 02, tùy chọn**.
6. **Mini-project** — làm khung ASCII tĩnh theo
   [`mini-project/README.md`](mini-project/README.md); `input()` là phần nâng cao.
7. **Commit evidence** — review thay đổi, lưu [minh chứng](evidence-template.md),
   commit trên nhánh học tập (không push trực tiếp vào `main`).

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

1. [`ex01_hello.py`](exercises/ex01_hello.py) — lời chào, khung ký tự (**cốt lõi**).
2. [`ex02_calculator.py`](exercises/ex02_calculator.py) — số học (**cốt lõi**).
3. [`ex03_input.py`](exercises/ex03_input.py) — `input()` và chuyển kiểu (**tùy chọn, nội dung Tuần 02**).

Mỗi file có TODO chưa hoàn thiện. **Chạy không báo lỗi không có nghĩa đã làm xong**.
Hãy so sánh kết quả theo [đề và cách tự kiểm tra](exercises/README.md) trước
khi xem [`solutions/`](solutions/).

Gợi ý theo từng bài nằm ở [`hints.md`](hints.md).

## Chạy và kiểm chứng (từ thư mục gốc repository)

```bash
# Ví dụ có sẵn:
python weeks/week-01-hello-python/examples/01_print_and_comments.py
python weeks/week-01-hello-python/examples/02_arithmetic.py
python weeks/week-01-hello-python/examples/03_first_error.py

# Hai bài do sinh viên tự viết (starter chưa hoàn thành):
python weeks/week-01-hello-python/exercises/ex01_hello.py
python weeks/week-01-hello-python/exercises/ex02_calculator.py

# CHỈ kiểm tra lời giải và ví dụ tham chiếu, KHÔNG chấm bài sinh viên:
python weeks/week-01-hello-python/checks/check_week.py

# Giảng viên có pytest có thể thử thêm các ca biên:
python -m pytest weeks/week-01-hello-python/tests -q
```

Trên Windows có thể thay `python` bằng `py`, trên macOS/Linux bằng
`python3`, theo command đã kiểm tra tại [SETUP](../../SETUP.md). Dấu
`>>>` là REPL — dùng `exit()` trước khi gõ lệnh terminal.

Chi tiết: [`checks/README.md`](checks/README.md).

## Mini-project — ASCII Art Generator

Mức bắt buộc chỉ dùng `print()` để vẽ khung tĩnh; mức tự chọn hỏi tên
bằng `input()` thuộc Tuần 02. Đề tại [mini-project](mini-project/README.md).

## Commit evidence

Trên branch bài tập của bạn, trước khi commit:

```bash
git status
git diff
```

Chỉ stage file bạn đã chủ động thay đổi. Dùng message mô tả kết quả, ví dụ:

```bash
git commit -m "feat: complete Week 01 Python exercises"
```

Nếu chưa có branch được phân công, tạo bằng `git switch -c student/week01-my-work`
**trước khi sửa bài**. Chỉ `git add` các file do bạn sửa, commit rồi push
nhánh nếu có quyền; nếu không, nộp bằng fork hoặc theo yêu cầu giáo viên.
Không commit secret, `.venv`, `__pycache__` hay file tạm.
Điền commit SHA vào [minh chứng](evidence-template.md).

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
- [ ] Đối chiếu output thật của hai bài cốt lõi với [đề](exercises/README.md).
- [ ] Tự chọn: chuẩn bị Tuần 02 với `ex03_input.py`.
- [ ] Chạy các file trong `examples/`.
- [ ] Hoàn thành mini-project.
- [ ] Ghi [minh chứng](evidence-template.md) và tự soát rubric 10 điểm.
- [ ] Review thay đổi trước khi commit.
- [ ] Commit và push bằng chứng lên GitHub.
- [ ] Cập nhật [`PROGRESS.md`](../../PROGRESS.md).
