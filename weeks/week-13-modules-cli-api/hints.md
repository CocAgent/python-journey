# Gợi ý ba mức — Week 13

**Hãy tự thử trước khi mở từng mức.** Gợi ý không thay lời giải trong
[solutions](solutions/README.md).

## Exercise 01 — Module và main guard

- **Mức 1:** Hàm cần dùng nằm ở `bot_course/core.py`.
- **Mức 2:** Dùng `from bot_course.core import ...`, viết `main()`.
- **Mức 3:** Đặt `main()` trong `if __name__ == "__main__":`.
  Chạy `python -m exercises.ex01_modules` từ week root.

## Exercise 02 — argparse

- **Mức 1:** Thêm một option để nhận số lượt.
- **Mức 2:** `parser.add_argument("--turn", type=int, required=True)`.
- **Mức 3:** `parse_args()` trả Namespace; thử thiếu option và `--turn abc`.

## Exercise 03 — HTTP offline

- **Mức 1:** Có `fixture` JSON bytes và hàm `parse_json_response`.
- **Mức 2:** Gọi `parse_json_response(200, fixture)`, lấy `lesson`.
- **Mức 3:** Thử status `500` trong `try/except ValueError`,
  xác nhận không có dữ liệu “thành công” được in khi lỗi.

## Exercise 04 — Adapter course-local

- **Mức 1:** State gồm `position` và `goal`.
- **Mức 2:** `from bot_course.adapter import course_local_action`.
- **Mức 3:** Thử `position=True` và `position=99`, giải thích
  vì sao đều bị từ chối.

## Khi báo lỗi import

1. Em đang ở thư mục nào? `pwd` (Linux/macOS) hoặc `cd` (Windows).
2. Em đang chạy **file path** hay **`python -m module`**?
3. `bot_course` nằm ở đâu so với working directory?
4. Không thêm `sys.path.insert` vào module core chỉ để “chữa cháy”.

## Khi báo lỗi HTTP

- Đầu tiên kiểm **status**, sau đó **encoding/JSON**, cuối cùng **schema**.
- Không bắt `except:` chung rồi in “thành công”.
- Chưa cần gọi HTTP thật; đủ kiểm thử bằng static body.
