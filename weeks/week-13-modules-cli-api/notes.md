# Week 13 — Modules, CLI và HTTP foundation

## Module và package

Một file .py là module. Một directory có __init__.py có thể là package.
Import rõ tên giúp biết dependency đi theo hướng nào.

    from bot_course.core import choose_action

Main guard giữ code chạy CLI khỏi chạy lúc import.

## Dependencies

Tạo environment bằng python -m venv .venv; dùng python -m pip để chắc pip
thuộc đúng interpreter. pyproject.toml mô tả project/tooling và nhóm dependency
maintainer; không phải mọi repository đều là package để publish.

## CLI

argparse chuyển command-line text thành giá trị có tên. CLI gọi core rồi in
evidence, còn decision logic không đọc trực tiếp sys.argv.

## HTTP request/response

    client -- GET request --> server
    client <-- status + headers + body -- server
    JSON text → json.loads(...) → Python dict/list

Network có thể timeout, DNS fail hoặc trả non-2xx status. Core grading dùng
static fixture nên chạy offline. urllib.request.Request chỉ minh họa request
trung lập; không gọi live service.

## Adapter boundary

    Bot Core ≠ Transport/Adapter

Core nhận course state và trả action. Adapter serialize/translate dữ liệu.
Production VuaCóc contract vẫn UNVERIFIED; không đoán endpoint, auth hay schema.

## Import path và cách chạy module

Khi chạy `python path/to/file.py`, Python ưu tiên directory chứa file đó. Khi
chạy `python -m package.module`, Python bắt đầu từ working directory và resolve
package theo tên. Week 13 dùng module mode để exercises thấy package sibling:

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex03_http
```

Không chỉnh `sys.path` trong bot core. Entry-point infrastructure có thể chịu
trách nhiệm bootstrap, còn module nghiệp vụ giữ import rõ ràng.

## Dependency group của repository

Repository khai báo `pytest` và Ruff trong nhóm `dev` của `pyproject.toml`.
Pip hỗ trợ `--group` từ phiên bản 25.1, vì vậy kiểm tra hoặc nâng pip trước:

```bash
python -m pip install --upgrade "pip>=25.1"
python -m pip install --group dev
```

## Network error boundary

Một HTTP client thật phải đặt timeout và xử lý lỗi transport tách khỏi lỗi
parse/validation:

```python
from urllib.error import URLError
from urllib.request import urlopen

from bot_course.http_foundation import parse_json_response


def fetch_json(request):
    try:
        with urlopen(request, timeout=5) as response:
            status = response.status
            body = response.read()
    except (TimeoutError, URLError) as error:
        print(f"Không thể kết nối: {error}")
        return None
    else:
        return parse_json_response(status, body)
```

Ví dụ bắt buộc của khóa vẫn dùng static fixture để test chạy offline và không
phụ thuộc một dịch vụ bên ngoài.
