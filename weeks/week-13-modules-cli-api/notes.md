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
