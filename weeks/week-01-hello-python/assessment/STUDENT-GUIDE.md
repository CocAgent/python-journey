# Week 01 — Hướng dẫn sinh viên tự kiểm tra và đánh giá với AutoGrade

> **Dành cho sinh viên bắt đầu học Python.** Em tự viết, tự chạy, nhận gợi ý, sửa lỗi và lưu minh chứng. AutoGrade chỉ phản hồi về **5 điểm thực hành**; giảng viên đánh giá **5 điểm còn lại**. Kết quả tự kiểm **không phải điểm thi chính thức**.

## 1. Em sẽ làm những bài nào?

| Bài | Đường dẫn trong `python-journey` | Điểm tự động |
|---|---|---:|
| Bài 01 — Hello, tên, sở thích, hình chữ nhật | `weeks/week-01-hello-python/exercises/ex01_hello.py` | 2 |
| Bài 02 — cộng, trừ, nhân, lũy thừa, chia | `weeks/week-01-hello-python/exercises/ex02_calculator.py` | 2 |
| Mini-project — khung ASCII tĩnh | `weeks/week-01-hello-python/mini-project/starter_basic.py` | 1 |
| **Tổng phần máy tự kiểm** | **11 tiêu chí** | **5** |

`ex03_input.py` và mini-project có `input()` là **bài mở rộng dành cho Week 02**. Không làm phần này **không bị trừ điểm Week 01**. Đọc [đề bài Week 01](../exercises/README.md) trước khi viết.

## 2. Chuẩn bị Python và lấy mã nguồn

**Bước A — Chuẩn bị Python 3.12 trở lên.** Mở Terminal trên VS Code (Terminal → New Terminal) hoặc PowerShell/cmd. Gõ:

```bash
python --version
```

Kết quả phải là Python 3.12 trở lên. Trên Windows có thể dùng `py --version`; trên macOS/Linux thường dùng `python3 --version`. Nếu chưa cài Python, đọc [SETUP.md](../../../SETUP.md).

**Bước B — Lấy đúng thư mục bài tập.** Vào [repository Python Journey](https://github.com/CocAgent/python-journey); chọn **Code → Download ZIP**, giải nén và mở **toàn bộ thư mục** `python-journey` bằng VS Code. Nếu đã biết Git, có thể dùng:

```bash
git clone https://github.com/CocAgent/python-journey.git
cd python-journey
```

Nếu đã tải bằng ZIP thì **không cần chạy `git clone` lần nữa**. Nếu dùng repository fork/branch của lớp, hãy làm trên bản sao được phân công; **không đẩy bài làm lên `CocAgent/python-journey/main`**.

**Bước C — Đứng tại thư mục gốc.** Trong Terminal, kiểm tra em đang ở `python-journey`, nơi có hai thư mục `assessment/` và `weeks/`. Không chạy AutoGrade từ riêng thư mục `exercises/`, vì Python sẽ không tìm thấy gói `assessment`.

## 3. Tự làm bài và tự chạy từng tệp

1. Mở `exercises/ex01_hello.py` tại `weeks/week-01-hello-python/`, thay phần TODO bằng các lệnh `print()`. Phải có `Hello, World!`, tên trên dòng riêng, ba sở thích, khung `5 × 4` đúng khoảng trắng.
2. Hoàn thành `exercises/ex02_calculator.py`. **Viết biểu thức Python** rồi in kết quả; không chỉ gõ sẵn đáp số. Phân biệt `/`, `//`, `%` và `**`.
3. Hoàn thành `mini-project/starter_basic.py` bằng một khung gồm ba dòng, hai viền giống nhau và lời `Xin chào` ở giữa; không bắt buộc `input()`.
4. Lưu tệp trong VS Code (**Ctrl+S** trên Windows). Chạy lần lượt từ thư mục gốc:

```bash
python weeks/week-01-hello-python/exercises/ex01_hello.py
python weeks/week-01-hello-python/exercises/ex02_calculator.py
python weeks/week-01-hello-python/mini-project/starter_basic.py
```

Nếu máy dùng `py` hoặc `python3`, hãy thay tiền tố `python` nhất quán trong **tất cả** các lệnh. So sánh kết quả thật với [đề và kết quả mong đợi](../exercises/README.md).

## 4. Chạy máy tự chấm bài của em

Chỉ thực thi chương trình **em tự viết hoặc đã kiểm tra là đáng tin cậy**. Trong thư mục gốc `python-journey`, gõ **nguyên dòng**:

```bash
python -m assessment grade --week 01 --acknowledge-local-code
```

Trên Windows có thể thay `python` bằng `py`, còn trên macOS/Linux có thể thay bằng `python3`. Tham số `--acknowledge-local-code` xác nhận em biết chương trình đang **chạy mã Python trên máy mình**; đây **không phải** công cụ bảo mật hay máy chủ cách ly.

Kết quả hiện rõ `Chế độ: STUDENT — Week 01`. Đây mới là **chấm mã của em**. Mỗi tiêu chí hiển thị:

- `PASS`: máy nhận ra dấu hiệu đạt tiêu chí, được số điểm ghi sau mã tiêu chí.
- `RETRY`: chưa được công nhận tiêu chí; đọc dòng `Gợi ý:`, kiểm lại mã và đầu ra rồi chạy lại.
- `Điểm tự động: x.xx/5.00`: tổng số điểm máy tự kiểm; **5 điểm còn lại** giảng viên xem minh chứng học tập.

Ví dụ minh họa một phần kết quả, **không phải kết quả của em**:

```text
Chế độ: STUDENT — Week 01
  PASS W01.HELLO: 0.50/0.50 — In Hello, World!
  RETRY W01.REMAINDER: 0.00/0.40 — Chia lấy dư
    Gợi ý: Dùng toán tử % để tìm số kẹo còn lại.
Điểm tự động: 4.60/5.00; chờ giảng viên: tối đa 5.00 điểm.
Đây chỉ là kết quả tự luyện, không phải điểm chính thức.
```

Ví dụ trên chỉ minh họa cách đọc; máy có thể in các tiêu chí khác. **Lưu ý:** mã khởi đầu TODO chưa làm có thể hiện **0/5** — đó là trạng thái bình thường, không có nghĩa AutoGrade bị lỗi.

### Khi chưa đạt 5/5, em cần làm gì?

**Đọc RETRY → tìm đúng tiêu chí → mở tệp liên quan → sửa lỗi → lưu → chạy tệp → tự chấm lại.** Ví dụ `W01.REMAINDER` liên quan phép `100 % 7`; `W01.RECTANGLE` yêu cầu đúng dấu sao và khoảng trắng; `W01.FRAME` yêu cầu viền trên/dưới và chiều dài ba dòng thẳng hàng.

**Không** sửa `assessment/engine/`, `rubric.json`, tests hoặc bài mẫu để đổi `RETRY` thành `PASS`. Phần máy tự chấm dùng đầu ra và dấu hiệu cấu trúc mã (AST) nên **không kiểm được mọi lời giải đúng**. Nếu em chắc bài giải đúng nhưng vẫn `RETRY`, hãy lưu mã, đầu ra và hỏi giảng viên để được xem xét.

### Mã thoát khi chạy lệnh

| Trường hợp | Ý nghĩa |
|---|---|
| Exit code `0` | Đủ **5/5** điểm tự động |
| Exit code `1` | Còn tiêu chí chưa đạt; **không phải lỗi hệ thống** |
| Exit code `2` | Lệnh/cấu hình/đọc file có vấn đề; kiểm lại đường dẫn và tham số |

Nếu terminal hiển thị lệnh có mã thoát `1` khi chưa được 5/5, em vẫn có thể đọc gợi ý và làm bài tiếp.

## 5. Lưu bản đánh giá JSON và đối chiếu tiến bộ

Sau khi sửa bài, em nên lưu báo cáo tại máy:

```bash
python -m assessment grade --week 01 --acknowledge-local-code --json-out .learner-output/week01.json
```

Mở `.learner-output/week01.json` bằng VS Code. Em sẽ thấy `mode: "student"`, `auto_score`, `passed_criteria`, `total_criteria` và từng `checks` gồm `passed`, `earned`, `reason`, `hint`. `manual_score` và `official_score` là `null` (chưa có điểm duyệt/chính thức).

Tệp JSON được tạo **trên máy của em**, không tự tải lên GitHub/Drive. Mỗi lần dùng đúng đường dẫn xuất, báo cáo cũ **bị ghi đè**; nếu cần lưu quá trình tiến bộ, hãy đổi tên báo cáo, chẳng hạn `week01-lan-1.json`, `week01-lan-2.json`. Thư mục `.learner-output/` được dự án bỏ qua khi `git add` theo cấu hình thường dùng. Chỉ chia sẻ báo cáo theo yêu cầu và kênh riêng của giảng viên.

**Không nộp kết quả `--mode reference`**: lệnh `python -m assessment grade --week 01 --mode reference` chỉ chấm **fixture/bài mẫu của hệ thống**, không phải bài em viết; PASS của mẫu không chứng minh em đã làm bài.

## 6. Tự đánh giá phần minh chứng (5 điểm chờ duyệt)

Máy chỉ tự kiểm **5/10 điểm**. Em hãy tự rà soát phần còn lại, rồi giảng viên xác nhận theo [rubric hiện hành của Week 01](../exercises/README.md):

| Minh chứng | Tối đa | Em cần chuẩn bị |
|---|---:|---|
| Môi trường, Terminal và REPL | 2 | `python --version`, `git --version`, thử REPL `2 + 3`, xác định interpreter đang dùng |
| Một lỗi và cách tự sửa | 1 | Mô tả lỗi hoặc ảnh/đầu ra trước sửa, thay đổi cụ thể và kết quả sau sửa |
| Git commit, hướng dẫn chạy, evidence | 2 | Branch/commit SHA khi dùng Git; mô tả các lệnh đã chạy và báo cáo tự chấm |

Điền [phiếu minh chứng Week 01](../evidence-template.md) bằng kết quả **thực tế**, không chép kết quả ví dụ. Nếu học bằng ZIP hoặc chưa có quyền push, hỏi giảng viên hình thức nộp tương đương; không tạo commit giả. Em có thể ghi **điểm tự dự đoán** nhưng không tự gán điểm chính thức.

## 7. Lỗi thường gặp và cách xử lý

| Hiện tượng | Cách xử lý |
|---|---|
| `python` không nhận diện | Kiểm tra cài Python và PATH; thử `py` hoặc `python3` theo hệ điều hành |
| `No module named assessment` | Mở Terminal ở **gốc** `python-journey`, không chạy trong `exercises/`; tải **toàn bộ** repository, không chỉ một file `.py` |
| `the following arguments are required: --week` | Dùng đúng lệnh đầy đủ có `grade --week 01` |
| Thiếu `--acknowledge-local-code` | Chỉ thêm cờ khi em hiểu chương trình sẽ thực thi mã trên máy và chỉ chấm mã đáng tin |
| `RETRY` dù `python ex01_hello.py` không báo lỗi | `chạy được` chưa đủ; cần đúng nội dung/khoảng trắng/biểu thức |
| Lỗi `SyntaxError` | Sửa cú pháp trong file bài tập, lưu lại, thử chạy file riêng rồi mới chấm |
| Báo tệp bị thiếu | Kiểm tra đủ 3 tệp và tên file chính xác; đừng di chuyển khỏi cây thư mục `weeks/` |
| Chạy `--mode reference` ra `5/5` | Chỉ là bài **mẫu**; dùng chế độ STUDENT để đánh giá bài của em |

## 8. Nộp bài và checklist cuối Week 01

Trước khi nộp, em cần:

- [ ] Tự viết và lưu ba file `ex01_hello.py`, `ex02_calculator.py`, `starter_basic.py`.
- [ ] Chạy trực tiếp từng file và đối chiếu kết quả mong đợi.
- [ ] Chạy AutoGrade **chế độ STUDENT**, đọc PASS/RETRY, thử sửa những phần chưa đạt.
- [ ] Ghi điểm **tự động trên 5**, số tiêu chí đã đạt và lệnh kiểm vào minh chứng.
- [ ] Ghi lại ít nhất một lỗi đã sửa và có bằng chứng.
- [ ] Hoàn thiện phần Terminal/REPL, Git/hướng dẫn chạy để giảng viên xét **5 điểm** còn lại.
- [ ] Kiểm tra không nộp secrets, token, file `__pycache__`, thư mục `.venv`, hoặc code/đáp án của người khác.
- [ ] Nộp qua kênh lớp quy định (folder/ZIP/fork/branch được phân công); **không push vào `main` của repository gốc**.

**Ghi nhớ:** `check_week.py` và `pytest weeks/week-01-hello-python/tests` kiểm **lời giải/ví dụ tham khảo của giáo trình**, không chấm file em đã viết. Chỉ lệnh `python -m assessment grade --week 01 --acknowledge-local-code` chấm ba tệp bài làm hiện có trên máy em. Không dùng các cách kiểm lời giải tham khảo thay thế điểm của em.

---

**An toàn:** Subprocess và timeout trong AutoGrade **không tạo sandbox**. Không chạy mã bài nộp của người khác trên máy có tài khoản, bí mật hoặc dữ liệu quan trọng. Khi cần chấm hàng loạt, giảng viên phải có môi trường chạy cô lập riêng.
