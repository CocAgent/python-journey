# Dùng folder ôn tập trên máy truy cập qua Chrome Remote Desktop

Liên kết Chrome Remote Desktop là đường dẫn **phiên điều khiển máy**,
không phải thư mục giáo trình hoặc file có thể đọc như GitHub.
Chỉ người đang được cấp quyền hợp lệ vào máy mới nên thao tác.
Không chia sẻ mã phiên, mật khẩu, thông tin kết nối hoặc ảnh có
dữ liệu nhạy cảm; **không commit chúng vào repo**.

Tài liệu ôn tập này được tạo trong GitHub
`CocAgent/python-journey/review/`, **chưa được sao chép
trực tiếp vào máy từ xa**. Làm một trong hai cách trên máy đó:

## Cách A — Máy đã có repository Python Journey

Mở terminal trong chính thư mục repository (ví dụ Windows
`D:\Projects\python-journey` **nếu đó thực sự là đường dẫn trên máy**).

```bash
git remote -v
git branch --show-current
git status --short
git fetch origin
```

Nếu `git status --short` **còn thay đổi chưa lưu**, dừng và
bảo toàn chúng trước khi cập nhật; đừng dùng `reset --hard`
hoặc `git clean -fd`.

Khi repo sạch và bạn được phép cập nhật `main`:

```bash
git switch main
git pull --ff-only origin main
python review/practice/checks/check_review.py --solutions
```

Lệnh `--solutions` xác nhận bộ tài liệu tham khảo chạy được,
**không chấm bài sinh viên**. Sau đó sinh viên chỉnh file
trong `review/practice/starter/` và chạy:

```bash
python review/practice/checks/check_review.py --starter
```

Nếu `git switch main` hoặc `pull` báo xung đột, không ép
ghi đè; xử lý thay đổi đang có hoặc dùng cách B.

## Cách B — Chưa có repo hoặc không muốn thay đổi repo hiện tại

Trên máy đó, mở
[GitHub Python Journey](https://github.com/CocAgent/python-journey).
Chọn **Code → Download ZIP**, giải nén vào thư mục riêng,
mở terminal tại gốc thư mục đã giải nén và chạy lệnh trên.

Hoặc clone vào một thư mục hoàn toàn **mới**, không đè file cũ:

```bash
git clone https://github.com/CocAgent/python-journey.git
cd python-journey
python review/practice/checks/check_review.py --solutions
```

Cần Python >=3.12. Tham khảo [SETUP.md](../SETUP.md) nếu
terminal chưa nhận `python`; trên Windows có thể dùng `py -3`.

**Giới hạn:** cách trên chỉ giúp bạn mang thư mục ôn tập lên máy
qua GitHub. ChatGPT không nhìn/điều khiển phiên Chrome Remote
Desktop và không xác nhận đường dẫn/dữ liệu thực tế trên máy.
