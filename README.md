# Python Journey 🐍

> **Python cơ bản theo hướng học qua làm — từ zero đến một chương trình có thể kiểm chứng.**

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![15 Weeks](https://img.shields.io/badge/Duration-15%20Weeks-f59e0b?style=flat-square)](#lộ-trình-15-tuần)
[![Level](https://img.shields.io/badge/Level-Beginner-6366f1?style=flat-square)](#đối-tượng)

**Learning loop:** `Learn → Build → Test → Debug → Improve → Commit → Prove`

**Featured spiral project:** [VuaCóc Bot Journey](projects/vuacoc-bot-journey/README.md) https://vuacoc.com/

---

## Vị trí trong lộ trình

```text
CocAgent Python Learning Path
────────────────────────────────────────────────────────────
① python-journey       Python nền tảng · 15 tuần  ← BẠN ĐANG Ở ĐÂY
② python-mastery       Python chuyên sâu
③ dsa-python-course    Cấu trúc dữ liệu & thuật toán
④ data-python-course   Phân tích dữ liệu
────────────────────────────────────────────────────────────
Đầu vào: không yêu cầu kinh nghiệm lập trình
```

> **Mục tiêu cuối khóa:** người học không chỉ “biết cú pháp Python”, mà có thể viết một chương trình nhỏ **đúng, rõ ràng, có kiểm thử, biết debug và giải thích được vì sao giải pháp hoạt động**.

---

## Triết lý học

Python Journey không đi theo mô hình “đọc hết cú pháp rồi mới làm project”.

Mỗi chủ đề được học qua một vòng ngắn:

```text
Vấn đề → Khái niệm → Ví dụ nhỏ → Tự làm → Test → Debug → Cải tiến → Giải thích
```

Ba nguyên tắc:

1. **Học qua làm** — khái niệm phải được dùng ngay trong bài tập hoặc mini-project.
2. **Đúng phải có bằng chứng** — từ sớm người học làm quen với self-check và test, không chỉ nhìn output rồi đoán là đúng.
3. **Đơn giản nhưng đáng tin cậy** — không nhồi kỹ thuật chỉ để trông “nâng cao”.

---

## Đối tượng

| Phù hợp ✅ | Chưa phù hợp ⏭️ |
|---|---|
| Chưa từng lập trình | Đã thành thạo Python và cần nội dung chuyên sâu |
| Học sinh, sinh viên bắt đầu | Chỉ cần tra cứu nhanh một API cụ thể |
| Biết ngôn ngữ khác, muốn học Python bài bản | Muốn đi thẳng vào framework/AI mà bỏ qua nền tảng |
| Người muốn có workflow GitHub ngay từ đầu | — |

**Thời lượng đề nghị:** 7–10 giờ/tuần.

---

## Đầu ra sau 15 tuần

Sau khóa học, người học có thể:

- viết chương trình Python rõ ràng với biến, điều kiện, vòng lặp và hàm;
- sử dụng `list`, `tuple`, `dict`, `set` phù hợp với dữ liệu;
- xử lý chuỗi và biết khi nào regex hữu ích;
- đọc/ghi dữ liệu với file, CSV, JSON và `pathlib`;
- đọc traceback, xử lý exception và debug có phương pháp;
- viết test cơ bản bằng `pytest`, bao gồm edge cases;
- tổ chức code thành module và hiểu dependency/project structure ở mức nhập môn;
- gọi một HTTP API đơn giản, đọc status code và xử lý JSON response;
- hiểu type hints như contract hỗ trợ người đọc và tooling;
- dùng class khi OOP thực sự làm mô hình rõ hơn; hiểu composition và inheritance cơ bản;
- dùng Git/GitHub để lưu lịch sử phát triển;
- hoàn thành capstone có code, tests, README và bằng chứng chạy được;
- sẵn sàng bước sang **Python Mastery**, **DSA with Python** hoặc **Data Python**.

---

# Lộ trình 15 tuần

## Giai đoạn 1 — Khởi đầu

| Tuần | Chủ đề chính | Sản phẩm / trọng tâm |
|---|---|---|
| **01** | Environment · REPL · Terminal · Git/GitHub · Hello Python | Chạy chương trình đầu tiên, commit đầu tiên |
| **02** | Variables · Types · Input/Output | Chương trình nhập/xử lý dữ liệu đơn giản |
| **03** | Conditionals · Boolean · Input validation | Ra quyết định và bảo vệ input |

## Giai đoạn 2 — Dữ liệu & tư duy chương trình

| Tuần | Chủ đề chính | Sản phẩm / trọng tâm |
|---|---|---|
| **04** | Strings · Text processing · Regex mini-lab | Text Analyzer |
| **05** | Lists · Tuples · Mutability · Unpacking | Quản lý dữ liệu tuần tự |
| **06** | Loops · `enumerate` · `zip` · comprehensions | Lặp có chủ đích, tránh index thừa |
| **07** | Functions · Decomposition · Scope · Type hints | Utility Toolkit có contract rõ |
| **08** | Dict · Set · Nested data · Data modeling | Word/Data Counter |

## Tuần 09 — Midterm Project 🏆

Tổng hợp W01–W08 thành một chương trình console có cấu trúc. Trọng tâm là **phân rã vấn đề, dữ liệu, hàm, Git history và khả năng giải thích code**.

## Giai đoạn 3 — Viết chương trình đáng tin cậy

| Tuần | Chủ đề chính | Sản phẩm / trọng tâm |
|---|---|---|
| **10** | File · `pathlib` · CSV · JSON | Data persistence |
| **11** | Exceptions · Tracebacks · Debugging · Defensive coding | Tìm và sửa lỗi có phương pháp |
| **12** | **Testing with pytest** | Test normal case, edge case, invalid input |
| **13** | Modules · Packages · Dependencies · CLI · API/HTTP | Chương trình nhiều module + API nhỏ |
| **14** | OOP Essentials · Composition · Basic inheritance | Mô hình hóa khi class thực sự hữu ích |

## Tuần 15 — Capstone Project 🎓

Xây dựng một chương trình Python hoàn chỉnh có:

- vấn đề và phạm vi rõ ràng;
- ít nhất 4 chức năng có ý nghĩa;
- code được phân rã hợp lý;
- xử lý lỗi và edge cases;
- tests có ý nghĩa;
- README và hướng dẫn chạy;
- Git history rõ ràng;
- khả năng demo và giải thích quyết định thiết kế.

Yêu cầu chính thức nằm tại [`FINAL_PROJECT.md`](FINAL_PROJECT.md).

---

## Ranh giới với Python Mastery

Python Journey trả lời:

> **Can I program reliably in Python?**

Python Mastery trả lời:

> **Can I engineer good Python software?**

Các nội dung sau để dành cho Python Mastery hoặc khóa chuyên sâu:

- advanced decorators;
- iterators/generators chuyên sâu;
- advanced typing và protocols;
- descriptors/metaclasses;
- advanced testing/mocking;
- concurrency/asyncio;
- design patterns và architecture;
- profiling/performance;
- packaging/publishing chuyên sâu.

---

## Cấu trúc repository

```text
python-journey/
├── README.md
├── SYLLABUS.md
├── SETUP.md
├── STYLE_GUIDE.md
├── PROGRESS.md
├── FINAL_PROJECT.md
├── weeks/
│   ├── week-01-hello-python/
│   ├── ...
│   └── week-15-capstone-project/
├── cheatsheets/
└── assets/
```

Trong quá trình nâng cấp V2, mỗi tuần sẽ dần hội tụ về learning pattern:

```text
README → notes/examples → exercises → self-check/tests → challenge → mini-project
```

---

## Chuẩn code của khóa

```python
def calculate_average(scores: list[float]) -> float:
    """Trả về điểm trung bình; trả 0.0 nếu danh sách rỗng."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
```

Người học được khuyến khích:

- đặt tên rõ nghĩa;
- giữ hàm có trách nhiệm rõ ràng;
- tránh bare `except:`;
- dùng `with` khi làm việc với file;
- comment để giải thích **tại sao**, không lặp lại điều code đã nói;
- viết test cho hành vi quan trọng.

---

## Bắt đầu

```bash
git clone https://github.com/CocAgent/python-journey.git
cd python-journey
cat SETUP.md
```

Sau đó mở:

```text
weeks/week-01-hello-python/
```

---

## Tài liệu chính

- [`SYLLABUS.md`](SYLLABUS.md) — nguồn chân lý curriculum 15 tuần.
- [`PROGRESS.md`](PROGRESS.md) — checklist tiến trình.
- [`SETUP.md`](SETUP.md) — cài đặt môi trường.
- [`STYLE_GUIDE.md`](STYLE_GUIDE.md) — quy tắc viết code.
- [`FINAL_PROJECT.md`](FINAL_PROJECT.md) — yêu cầu capstone chính thức.

---

> **Learn it. Build it. Test it. Understand it. Improve it.**
