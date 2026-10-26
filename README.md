<!--
  Python Journey — repository landing page
  Keep links relative so they work on GitHub.
-->

<div align="center">

# 🐍 Python Journey

### Từ dòng code đầu tiên đến những chương trình Python có thể kiểm thử

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3"></a>
  <a href="./weeks/"><img src="https://img.shields.io/badge/Roadmap-15%20Weeks-7C3AED?style=for-the-badge" alt="15 week roadmap"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-16A34A?style=for-the-badge" alt="MIT license"></a>
</p>

**Learn · Build · Test · Debug · Improve**

*Học từng bước, luyện tập bằng code thật, và hiểu điều mình viết.*

</div>

---

## 🧭 Bắt đầu từ đây

| Bạn muốn… | Mở tài liệu |
|---|---|
| Cài đặt môi trường và chạy code | [SETUP.md](SETUP.md) |
| Xem toàn bộ chương trình học | [SYLLABUS.md](SYLLABUS.md) |
| Theo dõi tiến độ | [PROGRESS.md](PROGRESS.md) |
| Xem quy tắc viết code | [STYLE_GUIDE.md](STYLE_GUIDE.md) |
| Xem yêu cầu đồ án cuối khóa | [FINAL_PROJECT.md](FINAL_PROJECT.md) |
| Vào danh sách các tuần | [Thư mục weeks](weeks/) |

## 🗺️ Lộ trình 15 tuần

<details open>
<summary><strong>Giai đoạn 1 — Nền tảng Python (Tuần 01–03)</strong></summary>

| Tuần | Chủ đề | Nội dung |
|:---:|---|---|
| 01 | Hello Python | Môi trường, terminal, Git/GitHub, chương trình đầu tiên |
| 02 | Variables & Types | Biến, kiểu dữ liệu, nhập và xuất dữ liệu |
| 03 | Conditionals | Điều kiện, Boolean, kiểm tra dữ liệu đầu vào |

</details>

<details>
<summary><strong>Giai đoạn 2 — Dữ liệu và tư duy lập trình (Tuần 04–08)</strong></summary>

| Tuần | Chủ đề | Nội dung |
|:---:|---|---|
| 04 | Strings & Regex | Xử lý chuỗi và biểu thức chính quy |
| 05 | Lists & Tuples | Dữ liệu tuần tự, mutability, unpacking |
| 06 | Loops | Vòng lặp, `enumerate`, `zip`, comprehensions |
| 07 | Functions | Hàm, scope, phân rã vấn đề, type hints |
| 08 | Dictionaries & Sets | Dữ liệu dạng key-value và tập hợp |

</details>

<details>
<summary><strong>Giai đoạn 3 — Dự án giữa kỳ (Tuần 09)</strong></summary>

| Tuần | Chủ đề | Nội dung |
|:---:|---|---|
| 09 | Midterm Project | Kết hợp kiến thức tuần 01–08 thành chương trình console |

</details>

<details>
<summary><strong>Giai đoạn 4 — Code đáng tin cậy (Tuần 10–14)</strong></summary>

| Tuần | Chủ đề | Nội dung |
|:---:|---|---|
| 10 | Files & Data | File, `pathlib`, CSV, JSON |
| 11 | Exceptions & Debugging | Ngoại lệ, traceback, tìm và sửa lỗi |
| 12 | Testing | Kiểm thử cơ bản với pytest |
| 13 | Modules, CLI & API | Module, package, command line, HTTP/API |
| 14 | OOP Essentials | Class, object, composition, inheritance |

</details>

<details>
<summary><strong>Giai đoạn 5 — Đồ án cuối khóa (Tuần 15)</strong></summary>

| Tuần | Chủ đề | Nội dung |
|:---:|---|---|
| 15 | Capstone Project | Chương trình hoàn chỉnh có hướng dẫn chạy, xử lý lỗi và tests |

</details>

> **Lưu ý:** Bảng trên là bản đồ nội dung. Trạng thái hoàn thành của từng tuần cần được xác nhận từ bài tập và kết quả kiểm tra thực tế; không mặc định tuần nào cũng đã hoàn thành.

## 📁 Cấu trúc dự án

```text
python-journey-123/
├── README.md              # Trang chủ repo
├── weeks/                 # Bài học và bài tập theo tuần
├── projects/              # Dự án thực hành
├── tests/                 # Kiểm thử
├── scripts/               # Script hỗ trợ
├── cheatsheets/           # Tài liệu tra cứu nhanh
└── assets/                # Hình ảnh và tài liệu bổ trợ
```

*Cấu trúc chính xác có thể thay đổi theo các thư mục hiện có trong repository.*

## ⚙️ Cách chạy code

### 1. Clone repository

```bash
git clone https://github.com/LeTriDung-A/python-journey-123.git
cd python-journey-123
```

### 2. Chạy một file Python

```bash
python path/to/file.py
```

Trên một số máy Windows, có thể dùng `py path/to/file.py` nếu lệnh `python` không hoạt động.

### 3. Chạy bài kiểm tra của tuần

Mở README hoặc thư mục `checks/` của tuần tương ứng và dùng đúng lệnh được hướng dẫn tại đó. Không phải tuần nào cũng có cùng một lệnh kiểm tra.

## ✅ Cách học đề xuất

1. Đọc README và ví dụ của tuần.
2. Tự viết từng exercise trước khi xem lời giải.
3. Chạy chương trình, thử dữ liệu khác và kiểm tra trường hợp biên.
4. Đọc lỗi, sửa lỗi rồi chạy lại.
5. Ghi chú điều đã hiểu và commit thay đổi lên GitHub.

## 🎯 Mục tiêu của repository

- Nắm vững cú pháp và cấu trúc dữ liệu Python cơ bản.
- Biết tổ chức chương trình thành hàm và module.
- Đọc/ghi dữ liệu, xử lý ngoại lệ và debug.
- Làm quen với kiểm thử, Git và GitHub.
- Hiểu OOP ở mức nhập môn và biết khi nào nên dùng class.
- Hoàn thành dự án có thể chạy, kiểm tra và giải thích được.

---

<div align="center">

**💻 Learn it. Build it. Test it. Understand it.**

<sub>Python Journey · Học đều từng tuần, tiến bộ qua từng commit.</sub>

</div>
