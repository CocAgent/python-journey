# Week 11 — Bản giải thích ngắn gọn để trình bày

## 1. Tuần này học gì?

Week 11 học cách đọc thông báo lỗi, tìm nguyên nhân, xử lý dữ liệu nhập sai và viết chương trình an toàn hơn. Hai ý chính là **debugging** (gỡ lỗi) và **defensive coding** (lập trình phòng thủ).

## 2. Các khái niệm chính

- **Traceback:** thông tin giúp tìm đường đi đến nơi phát sinh lỗi. Đọc loại lỗi và thông báo ở cuối, rồi tìm dòng code liên quan.
- **Expected bad input:** dữ liệu sai có thể dự đoán, ví dụ nhập chữ thay vì số. Ta nên xử lý đúng lỗi đó.
- **Programming bug:** lỗi trong code, ví dụ gõ sai tên biến. Cần tìm và sửa, không nên che giấu bằng cách bắt mọi ngoại lệ.
- **Validation:** kiểm tra dữ liệu có hợp lệ trước khi dùng.
- **`raise`:** chủ động báo lỗi khi dữ liệu vi phạm quy tắc.
- **Debugging loop:** tái hiện lỗi → đọc traceback → khoanh vùng → sửa → kiểm tra lại.
- **Strategy loss và software defect:** bot có thể thua vì chiến thuật yếu dù code chạy đúng; crash hoặc hành động trái luật là lỗi phần mềm.

## 3. Ví dụ xử lý dữ liệu nhập sai

```python
try:
    age = int(input("Nhập tuổi: "))
except ValueError:
    print("Tuổi phải là số nguyên.")
```

Nếu người dùng nhập `abc`, Python phát sinh `ValueError` và chương trình hiển thị lời nhắc thay vì để lỗi chuyển kiểu không được xử lý.

Không nên viết `except Exception: pass` vì cách đó có thể che giấu lỗi thật.

## 4. `raise`, `else` và `finally`

```python
def validate_action(action: str) -> str:
    if action not in {"left", "right", "wait"}:
        raise ValueError(f"Invalid action: {action!r}")
    return action
```

Hàm chỉ chấp nhận ba hành động hợp lệ. Nếu nhận `jump`, `raise ValueError` báo rằng dữ liệu vi phạm quy tắc.

- **`else`:** chạy khi khối `try` không phát sinh ngoại lệ.
- **`finally`:** chạy khi rời cấu trúc xử lý lỗi, thường dùng để dọn dẹp hoặc ghi log.

## 5. Python khác C++ thế nào?

Hai ngôn ngữ đều hỗ trợ kiểm tra dữ liệu, gỡ lỗi và xử lý ngoại lệ. Điểm khác cơ bản về cú pháp:

| Python | C++ |
|---|---|
| `try` | `try` |
| `except` | `catch` |
| `raise` | `throw` |
| Traceback thường được Python in khi ngoại lệ không được xử lý | Thường dùng debugger hoặc stack trace để tìm vị trí lỗi |

Tư duy giống nhau là phát hiện lỗi, tìm nguyên nhân và sửa đúng chỗ. Cú pháp và cách công cụ hiển thị lỗi khác nhau.

## 6. Bài nói ngắn trước thầy

> Thưa thầy, Week 11 nói về debugging và defensive coding. Em học cách đọc traceback để biết loại lỗi và vị trí code liên quan. Em phân biệt dữ liệu nhập sai với lỗi do lập trình viên viết code sai. Em dùng try-except để xử lý lỗi dự kiến, validation để kiểm tra dữ liệu, và raise để báo lỗi khi dữ liệu không hợp lệ. Quy trình debug gồm tái hiện lỗi, đọc thông báo, khoanh vùng, sửa và kiểm tra lại. Python và C++ có cách làm tương tự, nhưng Python dùng except và raise, còn C++ dùng catch và throw.

## 7. Em cần nhớ

**Tìm đúng lỗi — không che giấu lỗi — sửa nguyên nhân — chạy kiểm tra lại.**

Tài liệu này bổ sung phần giải thích bằng tiếng Việt; không thay thế bài học, bài tập hoặc file code gốc của Week 11.
