# Google Antigravity — viết code Python cùng trợ lý AI (tự chọn)

> **Tên sản phẩm là Google Antigravity**, không phải "Antygravity".
> Đây là công cụ phát triển phần mềm có agent AI, **không phải Python
> interpreter** và cũng không phải module `import antigravity` của Python.

Phần này dành cho người đã chạy được `python --version`, Git, và ít nhất
một file `.py`. **Không bắt buộc** cài Antigravity để học Python Journey.

## 1. Chọn giao diện và cài từ nguồn chính thức

Google cung cấp **Antigravity App** (desktop), **Antigravity IDE**,
**Antigravity CLI** (`agy`) và tích hợp vào một số IDE.
Với người mới, hãy chọn **một trong hai** cách dưới đây:

- **Ứng dụng:** vào [trang tải của Google](https://antigravity.google/download),
  tải bản đúng hệ điều hành rồi cài và đăng nhập tài khoản Google theo yêu cầu.
- **VS Code:** mở Extensions (`Ctrl+Shift+X` trên Windows),
  tìm **Google Antigravity** và kiểm tra đúng nhà phát hành trước khi cài.
  Mở panel Antigravity và đăng nhập khi được yêu cầu.

Không cần cài CLI/SDK, gọi API, mua gói hay lấy API key để hoàn thành bài
Tuần 01. Đối với cách cài Python/Git/VS Code, vẫn dùng
[SETUP.md](../../../SETUP.md), không thay thế bằng công cụ AI.

Tài liệu chính thức:
[Google Antigravity — Getting started](https://antigravity.google/docs/getting-started)
và [codelab IDE](https://codelabs.developers.google.com/getting-started-agy-ide).

## 2. Mở repository Python Journey an toàn

Nếu **đã có repository trên máy**, bỏ qua `git clone`. Nếu chưa:

```bash
git clone https://github.com/CocAgent/python-journey.git
cd python-journey
git status
```

Giảng viên có thể đã chỉ định nhánh bài tập. **Dùng đúng nhánh được giao**;
nếu chưa có, tự tạo nhánh học tập bằng Git (không làm trên `main`):

```bash
git switch -c student/week01-practice
git branch --show-current
```

Đối với **Antigravity App**, tạo **New Project → Add Folder** và chọn
thư mục local `python-journey`. Agent có chế độ **Local** (làm việc
ngay trong thư mục) hoặc **New worktree** (tách một Git worktree);
khi mới học, hãy hiểu rõ nhánh và vị trí file trước khi chấp nhận chỉnh sửa.
Nếu đã dùng IDE khác, mở thư mục repo rồi dùng panel Antigravity tương ứng.

**Không có bước nào ở đây tự cấp quyền GitHub cho ChatGPT.** Antigravity
và ChatGPT là hai sản phẩm khác nhau.

## 3. Prompt gia sư: trợ giúp, không làm hộ

Đưa hướng dẫn sau vào agent chat, chỉ sau khi đã mở repo đúng:

```text
Bạn là gia sư Python Tuần 01. Trước hết đọc AGENTS.md và
weeks/week-01-hello-python/README.md.

Tôi đang học print(), chuỗi, phép toán và terminal.
Hãy giải thích bài ex01_hello.py theo từng TODO và cho tôi một gợi ý
đầu tiên. KHÔNG giải sẵn tất cả TODO.
Không sửa solutions/, tests/, AGENTS.md hay file ngoài Tuần 01.
Không tự commit, push, merge, xóa file hoặc chạy lệnh nguy hiểm.
Nếu muốn sửa file, hãy nêu những dòng sẽ đổi và hỏi tôi trước.
Sau đó hướng dẫn tôi tự chạy chương trình và đọc kết quả.
```

Bạn có thể hỏi thêm: **"Vì sao `print('Hello')` khác
`print(Hello)`? Hãy giải thích như cho người chưa học lập trình."**

## 4. Tự viết, chạy và đối chiếu

Một đoạn học thử (không phải lời giải toàn bộ bài tập):

```python
print("Xin chào Python!")
print(2 + 3)
```

Kết quả mong đợi:

```text
Xin chào Python!
5
```

Chạy file bài tập đã chỉnh từ terminal **ở thư mục gốc repo**:

```bash
python weeks/week-01-hello-python/exercises/ex01_hello.py
git status
git diff -- weeks/week-01-hello-python/exercises/ex01_hello.py
```

Thay `python` bằng `py` hoặc `python3` nếu đó là lệnh hoạt động
trên máy bạn. **REPL có dấu `>>>` không phải terminal**; gõ `exit()`
trước khi chạy các lệnh trên.

So sánh output với [đề bài](../exercises/README.md). Không coi lời khẳng
định "đã sửa xong" của agent là bằng chứng; **bạn phải chạy và kiểm tra**.
Nếu agent đề xuất thay đổi ngoài phạm vi, từ chối rồi yêu cầu làm lại.

## 5. Kiểm soát quyền và ghi minh chứng

- Đọc kế hoạch, lệnh terminal dự kiến và phần diff trước khi chấp thuận.
- Chỉ mở workspace cần thiết; không đưa `.env`, credential, token hoặc
  bài nộp cá nhân vào agent chat.
- Tránh chế độ thực thi lệnh tự động không cần xác nhận khi mới học.
- Không để AI tự động commit, push, merge hoặc thay đổi branch bảo vệ.
- GitHub không đồng nghĩa đã lưu bài: `git commit` lưu tại local;
  `git push` cần quyền và nhánh phù hợp.
- Trong [minh chứng](../evidence-template.md), ghi prompt đã dùng,
  file bạn sửa, câu lệnh chạy, output thật và phần bạn tự giải thích được.

**Giới hạn:** Antigravity chỉ hỗ trợ viết và kiểm tra code; nó không
thay thế Python, Git, tài khoản GitHub hoặc việc sinh viên tự hiểu bài.
