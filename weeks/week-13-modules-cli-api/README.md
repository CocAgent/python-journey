# Tuần 13 — Modules · Packages · Dependencies · CLI · API/HTTP

Tuần này bạn chia chương trình thành module/package, tạo CLI nhỏ và hiểu
request/response HTTP qua ví dụ offline trung lập.

## Outcomes

- import standard-library và module tự viết;
- tạo package với __init__.py và main guard;
- hiểu vai trò venv, python -m pip và pyproject.toml;
- nhận argument bằng argparse;
- nhận biết GET, status code, JSON response, timeout/error;
- giữ Bot Core tách khỏi Transport/Adapter.

Core checks không gọi mạng và không dùng endpoint VuaCóc production.

    python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
    python weeks/week-13-modules-cli-api/checks/check_week.py

Xem [notes](notes.md), [package](bot_course/),
[cách chạy exercises](exercises/README.md),
[hints](hints.md) và [mini-project](mini-project/README.md).
