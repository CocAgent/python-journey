# Week 13 — Giải thích từng bước (không cần biết trước về web)

## 1. Module là gì?

**Module = một file `.py`** chứa các hàm/biến có thể dùng lại. Hình dung:
mỗi file là một ngăn dụng cụ; em chỉ lấy đúng công cụ mình cần.

```python
# bot_course/core.py
def choose_action(position, goal):
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"
```

```python
# examples/ex01_modules.py
from bot_course.core import choose_action
print(choose_action(1, 4))  # right
```

**Package = nhóm các module** (thường có file `__init__.py`). Ở đây
`bot_course` chứa `core.py`, `adapter.py`, `cli.py` và
`http_foundation.py`.

Đọc `from bot_course.core import choose_action` từ trái sang phải:
**package → module → tên hàm**.

### Main guard: tránh chạy ví dụ khi import

```python
def main():
    print("Demo chạy khi gọi chương trình")


if __name__ == "__main__":
    main()
```

Khi em chạy file qua Python, `__name__` là `"__main__"`; khi import,
nó là tên module. Vì thế import không tự gọi `main()`.

### Vì sao `python -m` khác chạy file trực tiếp?

- `python exercises/ex03_http.py`: Python ưu tiên tìm module trong
  `exercises/`, có thể **không thấy** package `bot_course` nằm bên cạnh.
- `python -m exercises.ex03_http` **khi đang ở week root**: Python resolve
  `exercises` theo package/module từ working directory; import sibling
  `bot_course` thành công.
- `python weeks/week-13-modules-cli-api/cli.py` từ repository root:
  Python thêm thư mục chứa `cli.py` vào đường tìm module; đây là entry
  point riêng có thể chạy trực tiếp.

Không chỉnh `sys.path` bên trong module nghiệp vụ chỉ để sửa
`ModuleNotFoundError`. Hãy kiểm **working directory + lệnh chạy** trước.

## 2. Package, dependency, venv và pip

**Package (code)** là nhóm module; **dependency** là thư viện/chương trình
khác project cần để chạy/test. Ví dụ: `argparse`, `json`, `urllib` thuộc
**thư viện chuẩn** (đã có cùng Python) — không cần `pip install argparse`.
`pytest` và `ruff` là **dependency bên ngoài**, dùng để test/lint.

**venv = môi trường Python riêng của project** để tránh xung đột thư viện
giữa các khóa học.

Từ gốc repo, em có thể thử:

```bash
python -m venv .venv
python -m pip --version
python -m pip list
```

Nếu kích hoạt venv, hãy xem [SETUP.md](../../SETUP.md) để biết cách cho
Windows PowerShell và macOS/Linux. Có thể gọi trực tiếp Python của venv
nếu PowerShell chặn script kích hoạt. Không cần sửa policy hệ thống.

### Tại sao `python -m pip` thay vì `pip`?

`python -m pip` chọn pip **của interpreter vừa gọi**. Lệnh `pip`
trên PATH đôi khi thuộc Python khác.

**`pyproject.toml` của repo** lưu dependency group `dev` chứa `pytest`,
`ruff` và cấu hình tool; không đồng nghĩa cả repository là một package
phải publish. Nếu cần cài bộ công cụ cho người duy trì:

```bash
python -m pip install --upgrade "pip>=25.1"
python -m pip install --group dev
```

Các bài W13 chạy bằng standard library, **không cần bước cài trên để học core**.

## 3. CLI — chương trình nhận lệnh từ terminal

**CLI (Command-Line Interface)**: người dùng gửi tham số qua terminal.
`argparse` biến text thành giá trị và tạo `--help` cùng thông báo lỗi.

```bash
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
```

Hành trình dữ liệu:

```text
terminal text "--position 1 --goal 4"
  ↓ argparse: position=1, goal=4 (int)
  ↓ adapter: kiểm cả hai thuộc 0..4
  ↓ core: chọn "right"
  ↓ CLI: in JSON ra terminal
```

`argparse` với `type=int` từ chối `"abc"`, nhưng không tự biết
`99` là vị trí không hợp lệ. Kiểm **kiểu dữ liệu** khác với kiểm
**quy tắc nghiệp vụ**. Xem `bot_course/adapter.py`.

**Exit code**: `0` = hoàn tất; `2` = tham số hoặc dữ liệu nhập sai.
`main()` trả mã; chỉ entry point gọi `raise SystemExit(main())`.

## 4. HTTP GET, status code và JSON

Hình dung em gửi một yêu cầu mượn sách:

```text
CLIENT (ứng dụng)  -- GET /books -->  SERVER
CLIENT             <-- status + body -- SERVER
```

**HTTP GET** thường dùng để **đọc dữ liệu**, không phải để ghi/sửa.
**Status code** nói tình trạng:
- `200`: yêu cầu thành công (thường có dữ liệu);
- `404`: không tìm thấy;
- `500`: server gặp lỗi;
- `503`: server tạm không sẵn sàng.

Một phản hồi còn có **headers** (ví dụ Content-Type), **body** (chuỗi
bytes). JSON là định dạng text, chuyển sang `dict`/`list` bằng
`json.loads()`.

```python
from bot_course.http_foundation import parse_json_response

body = b'{"topic": "python", "count": 3}'
data = parse_json_response(200, body)
print(data["topic"])  # python
```

Trong ví dụ này:
- status phải là 2xx;
- body phải decode được UTF-8 và là JSON hợp lệ;
- bài học **quy ước** response là JSON object (`dict`), không nhận
  list; **HTTP thực tế vẫn có thể trả JSON list**, hoặc trả nội dung khác.

```python
from bot_course.http_foundation import build_get_request

request = build_get_request("https://example.invalid/demo")
print(request.get_method())  # GET
```

**Chỉ tạo `Request` KHÔNG gửi mạng.** Domain `example.invalid` được dùng
cho tài liệu và không dùng để gọi thật. Không có `urlopen()` trong
bài thực hành bắt buộc.

### HTTP client thật (đọc để biết, không chạy ở W13)

Ở một ứng dụng client thực, `urlopen(..., timeout=5)` mới thực hiện
kết nối; cần bắt `TimeoutError`, `urllib.error.URLError`, tách lỗi
status khỏi parse và validate kết quả. Mạng có thể lỗi ngay cả khi code
đúng. Không sử dụng endpoint giả của VuaCóc hoặc thông tin bí mật.

## 5. Core khác adapter thế nào?

```text
CLI → adapter → core
          ↑       ↑
      kiểm input   quyết định thuần
      tạo format   không biết HTTP/CLI
```

- **Core**: `choose_action(1, 4)` trả `right`. Có thể dùng lại nơi khác.
- **Adapter course-local**: kiểm `position/goal` thuộc 0..4, rồi gói
  kết quả thành `dict`.
- **CLI**: nhận tham số, in thông báo lỗi và JSON; không quyết định
  left/right/wait.
- **HTTP foundation**: ví dụ đọc phản hồi giả lập độc lập, **không phải
  adapter production**.

Trong VuaCóc, `VUACOC_RUNTIME_CONTRACT = UNVERIFIED`,
`ARENA_ADAPTER = DESIGN_ONLY`, `PRODUCTION_INTEGRATION = NO`.
Không suy đoán endpoint, timeout, auth hay schema của website thật.

## 6. Em hãy tự dự đoán trước khi chạy

| Tình huống | Dự đoán | Vì sao |
|---|---|---|
| position=2, goal=4 | `right` | chưa đến đích |
| position=4, goal=2 | `left` | đã vượt đích |
| position=3, goal=3 | `wait` | đang ở đích |
| position=100, goal=3 | error, exit 2 | ngoài vùng hợp lệ |
| status=503, body JSON đúng | error | HTTP status không thành công |
| status=200, body b\"not-json\" | error | cú pháp JSON sai |
| status=200, body b\"[]\" | error trong ví dụ này | không phải JSON object |

## 7. Những hiểu lầm cần tránh

- `import` không phải copy/paste code; dependency vẫn phải chạy được
  trong Python environment.
- `type hint` giúp đọc và dùng công cụ phân tích, không tự validation
  input khi chạy.
- `status=200` không đảm bảo JSON hợp lệ.
- `Request(...)` không có nghĩa HTTP đã được gửi.
- CLI, HTTP, core và adapter có nhiệm vụ khác nhau; giữ tách để dễ test.
- Không học framework lớn trước khi hiểu các thành phần nhỏ.

Đi tiếp [Exercise 01–04](exercises/README.md), [gợi ý](hints.md),
[lời giải](solutions/README.md) và [mini-project](mini-project/README.md).
