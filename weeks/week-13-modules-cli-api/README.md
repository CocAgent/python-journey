# Tuần 13 — Module · Package · Dependency · CLI · API/HTTP

> **Từ một file Python đến chương trình có cấu trúc, chạy được qua terminal và hiểu dữ liệu HTTP.**
> Python >=3.12 · Không cần Internet/API key để học và làm bài.

## Học xong tuần này, em làm được gì?

1. Chia code thành **module** (file `.py`) và **package** (thư mục gồm các module).
2. `import` hàm từ module khác; dùng `if __name__ == "__main__"` để tránh chạy demo khi import.
3. Biết **virtual environment**, `python -m pip`, dependency và `pyproject.toml` dùng để làm gì.
4. Viết **CLI** nhận `--position`, `--goal` bằng `argparse`, hiểu exit code 0/2.
5. Giải thích **HTTP GET → status → body → JSON**, thử thành công và lỗi bằng dữ liệu giả.
6. Tách **business logic** khỏi CLI/HTTP adapter: `core → adapter → CLI`.

**Đây là chương trình offline course-local**, không phải API, adapter hay giao thức của VuaCóc production.

## Bắt đầu trong 5 phút

Mở terminal tại **gốc repository** `python-journey/`.

```bash
python --version
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
python weeks/week-13-modules-cli-api/cli.py --position 3 --goal 1
python weeks/week-13-modules-cli-api/cli.py --position 2 --goal 2
python weeks/week-13-modules-cli-api/cli.py --position 99 --goal 4
python weeks/week-13-modules-cli-api/checks/check_week.py
```

| Lệnh | Kết quả quan sát |
|---|---|
| position 1, goal 4 | JSON có `"action": "right"` |
| position 3, goal 1 | JSON có `"action": "left"` |
| position 2, goal 2 | JSON có `"action": "wait"` |
| position 99, goal 4 | thông báo dữ liệu sai, exit code **2** |
| check_week.py | `Week 13 solution checks: PASS` |

Quy ước vị trí `0..4` và ba action là **ví dụ học tập**, không phải hợp đồng sản xuất.

## Lộ trình học: 4 chặng dễ hiểu

| Chặng | Câu hỏi | Học ở đâu | Lệnh thử |
|---|---|---|---|
| 1. Module & package | Làm sao dùng hàm từ file khác? | [notes](notes.md#1-module-là-gì) | `python -m examples.ex01_modules` |
| 2. CLI & dependency | Truyền tham số và cài thư viện đúng Python nào? | [notes](notes.md#3-cli--chương-trình-nhận-lệnh-từ-terminal) | `python -m examples.ex02_cli --position 1 --goal 4` |
| 3. HTTP & JSON | Dữ liệu GET gửi/nhận ra sao? | [notes](notes.md#4-http-get-status-code-và-json) | `python -m examples.offline_http` |
| 4. Boundary | Vì sao không cho core đọc network trực tiếp? | [mini-project](mini-project/README.md) | `python -m examples.ex04_adapter` |

**Quan trọng:** các lệnh `python -m examples...` chạy **sau khi đổi vào thư mục tuần**:

```bash
cd weeks/week-13-modules-cli-api
python -m examples.ex01_modules
python -m examples.ex02_cli --position 1 --goal 4
python -m examples.offline_http
python -m examples.ex04_adapter
python -m bot_course.cli --position 1 --goal 4
```

Sau đó trở về gốc repo để chạy check tổng:

```bash
cd ../..
python weeks/week-13-modules-cli-api/checks/check_week.py
```

## Hình dung cấu trúc project

```text
week-13-modules-cli-api/
├── cli.py                  # cổng chạy thuận tiện từ repo root
├── bot_course/
│   ├── __init__.py         # package
│   ├── core.py             # quyết định left/right/wait
│   ├── adapter.py          # kiểm input, định dạng course-local
│   ├── cli.py              # argparse + xử lý lỗi người dùng
│   └── http_foundation.py  # Request + parse phản hồi GIẢ, không gọi mạng
├── examples/               # bốn ví dụ nhỏ
├── exercises/              # bài để em tự làm (có TODO)
├── solutions/              # lời giải tham khảo — xem sau khi thử
├── checks/                 # tự kiểm offline
└── mini-project/           # tích hợp một ứng dụng CLI
```

`CLI → adapter → core` là **hướng phụ thuộc**: core không import CLI, HTTP hay framework.

## Bài tập và tự kiểm

1. Làm lần lượt [Exercise 01–04](exercises/README.md), dự đoán output trước.
2. Khi bí, mở [hints theo ba mức](hints.md) thay vì xem lời giải ngay.
3. Chạy bài em viết bằng `python -m exercises.ex01_modules` (tương tự 02–04).
4. Sau khi hoàn thành mới đối chiếu [solutions](solutions/README.md).
5. Chạy [check tổng](checks/README.md); đây là kiểm tra **reference**, không chấm tự động TODO của em.
6. Thực hiện [mini-project](mini-project/README.md), ghi một bug và cách sửa.

```bash
# chạy từ gốc repository, không cần Internet
python weeks/week-13-modules-cli-api/checks/check_week.py

# nếu đã cài pytest trong môi trường dev:
python -m pytest weeks/week-13-modules-cli-api/tests -q
```

## Dependency và virtual environment

Nếu chỉ chạy bài này, **không cần cài package bên thứ ba**. Khi học `venv` và `pip`, xem [giải thích trong notes](notes.md#2-package-dependency-venv-và-pip) và [SETUP.md](../../SETUP.md).

## Các lỗi sinh viên thường gặp

| Dấu hiệu | Vì sao? | Cách sửa |
|---|---|---|
| `ModuleNotFoundError: bot_course` | chạy trực tiếp file nằm trong `exercises/` từ sai thư mục | đứng tại week root, chạy `python -m exercises.ex01_modules` |
| `unrecognized arguments` | gõ sai `--position`, `--goal` hoặc `--turn` | chạy `--help` |
| `invalid int value` | `argparse` đòi integer | nhập số nguyên, ví dụ `--goal 4` |
| `Lỗi dữ liệu` | position/goal không thuộc `0..4` | chọn giá trị hợp lệ |
| `JSONDecodeError` / `ValueError` | body không phải JSON object hợp lệ | kiểm status, encoding, shape; không giả định network luôn đúng |
| `pip` cài sai môi trường | chạy lệnh `pip` khác Python đang dùng | dùng `python -m pip` sau khi chọn interpreter |

## Hoàn thành khi

- [ ] Em phân biệt được module, package, dependency, CLI và HTTP.
- [ ] Em chạy được demo `left/right/wait` và giải thích main guard.
- [ ] Em kiểm được một input sai và một phản hồi HTTP lỗi mà không gọi mạng.
- [ ] Em tự làm ít nhất 3/4 bài tập và trình bày được một bài.
- [ ] Em chạy check tham khảo, ghi một bug đã sửa và một giới hạn.
- [ ] Em giải thích được tại sao **Bot Core không phụ thuộc HTTP/CLI**.

Learning loop: **Learn → Build → Test → Debug → Improve → Commit → Prove**.
