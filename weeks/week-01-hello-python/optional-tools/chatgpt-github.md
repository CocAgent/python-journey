# Kết nối GitHub với ChatGPT — học và đọc code cùng AI (tự chọn)

Đây là cách **cho ChatGPT truy cập repository mà bạn có quyền**, để giải
thích, tìm tệp và góp ý code. **Không phải lệnh `git clone`, `git push`**
và không tự động cấp quyền sửa hay merge vào `main`.

**Kết nối tài khoản là bước người dùng tự xác nhận** trên giao diện
ChatGPT và GitHub; giảng viên không cần xin mật khẩu hoặc token của sinh viên.

## 1. Chuẩn bị

- Đăng nhập [ChatGPT](https://chatgpt.com/) và [GitHub](https://github.com/)
  bằng **tài khoản của chính mình**.
- Có quyền xem repository cần học, ví dụ
  [CocAgent/python-journey](https://github.com/CocAgent/python-journey).
- Không dùng tài khoản giảng viên chung, không sao chép Personal Access Token
  hoặc thông tin xác thực vào hộp chat.

Kết nối GitHub tùy vào **gói, không gian làm việc và chế độ ChatGPT**.
Không thấy GitHub trong chat thông thường không có nghĩa tính năng đã
được bật ở tất cả chế độ.

## 2. Kết nối trên ChatGPT

1. Mở **Settings (Cài đặt) → Plugins (Tiện ích)**. Một số giao diện cũ
   có tên **Apps**; dùng mục kết nối ứng dụng đang hiển thị trên tài khoản.
2. Tìm và chọn **GitHub** (hoặc plugin có tích hợp GitHub).
3. Chọn kết nối, đăng nhập/ủy quyền trên trang **GitHub chính thức**.
4. Trong bước chọn repository, cấp quyền cho **repo cần học**, thay vì
   toàn bộ repository nếu không cần thiết.
5. Quay lại ChatGPT và mở cuộc trò chuyện/chế độ có quyền dùng GitHub.
   Nếu repo của tổ chức cần phê duyệt, hãy yêu cầu admin GitHub xử lý;
   không tìm cách vượt qua bước xác nhận.

Nếu mục GitHub không xuất hiện, kiểm tra khả năng hỗ trợ theo gói và
chế độ. Có tài khoản chỉ truy cập được qua các chế độ như nghiên cứu
hoặc agent, không nhất thiết ở chat thông thường.

**Nguồn chính thức, ưu tiên nếu giao diện thay đổi:**
[OpenAI — Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt).

## 3. Bài thực hành với Python Journey

Sau khi kết nối được và cấp quyền repo:

```text
Hãy đọc CocAgent/python-journey ở nhánh main,
đặc biệt weeks/week-01-hello-python/README.md và
exercises/ex01_hello.py.

Cho tôi biết mục tiêu của từng TODO, giải thích print() và
gợi ý một bước nhỏ để tự làm. KHÔNG đưa toàn bộ lời giải.
Hãy chỉ rõ tên file đã đọc. Nếu không truy cập được repo,
nói rõ thay vì đoán nội dung.
```

Prompt đối chiếu code (chỉ khi bạn đã lưu bài trên nhánh có thể truy cập):

```text
Hãy tìm và đọc bài ex01_hello.py trên nhánh bài tập của tôi
(nếu tài khoản đang cho phép truy cập nhánh đó).
Đối chiếu với yêu cầu Tuần 01: các dòng print, ba sở thích
và hình chữ nhật 5x4. Chỉ nêu lỗi/hint, không sửa thay tôi.
Phân biệt điều bạn đọc thấy và điều chưa kiểm chứng bằng chạy code.
```

**Lưu ý:** ChatGPT có thể nhìn thấy **phiên bản đã có trên GitHub**
được cấp quyền. Mã đang sửa nhưng **chưa commit/push ở local không
tự động xuất hiện** trong kết nối GitHub. Với code local chưa đẩy lên,
bạn có thể dán một đoạn ngắn không nhạy cảm vào chat để hỏi.

## 4. Quyền và giới hạn cần hiểu

| Việc | Có kết nối GitHub–ChatGPT là đủ? |
|---|---|
| Đọc, tìm kiếm, giải thích mã được cấp quyền | Có, trong chế độ được hỗ trợ |
| Đọc file đang nằm riêng trên máy local | Không |
| Tự động commit/push/merge | **Không**; cần công cụ và quyền ghi riêng |
| Cấp quyền repo riêng tư của tổ chức | Cần GitHub/app authorization, có thể cần admin |
| Chuyển quyền GitHub sang Google Antigravity | Không, phải cấu hình riêng nếu cần |

Trong các công cụ có khả năng hành động/viết code (ví dụ Codex hoặc
workflow được cấp quyền riêng), hãy dùng **nhánh học tập**, xem diff và
kiểm thử, chỉ merge sau review. Không suy rằng chỉ việc bấm
"Connect GitHub" sẽ cho ChatGPT quyền quản trị tổ chức.

## 5. Quản lý hoặc thu hồi quyền

Vào **Settings → Plugins → GitHub** để mở mục quản lý quyền repository
hoặc chọn **Disconnect**. Tùy tài khoản, giao diện có thể tên khác;
đối chiếu tài liệu OpenAI mới nhất. Đảm bảo chỉ cấp quyền tối thiểu.

Ghi vào [minh chứng học tập](../evidence-template.md) phần ChatGPT đã
giúp, đường dẫn tài liệu đã đọc và cách **bạn tự kiểm tra** đầu ra Python.
Không nộp ảnh màn hình chứa email riêng, token, mã bí mật hoặc bài của
người khác.
