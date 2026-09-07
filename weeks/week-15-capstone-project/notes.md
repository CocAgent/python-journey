# Week 15 — Integration checklist

Canonical requirements và rubric: [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## Build

- chốt problem statement và out-of-scope;
- nối các phần đã có thành một luồng chạy được;
- không thêm feature lớn chỉ để demo trông nhiều hơn.

## Test và debug

- chạy normal, edge, invalid và regression cases liên quan;
- giữ failure message hoặc replay hữu ích;
- phân biệt known limitation với software defect.

## README

- mục tiêu và scope;
- cách setup/chạy/test;
- input/output mẫu;
- design decision và trade-off;
- known failures/limitations;
- AI usage disclosure nếu có.

## Git/GitHub evidence

- commit message mô tả thay đổi;
- worktree sạch khi handoff;
- history cho thấy Learn → Build → Test → Debug → Improve → Commit → Prove.

## Optional VuaCóc local tournament

    python projects/vuacoc-bot-journey/local_arena/tournament_cli.py

Kết quả này chỉ chứng minh behavior trong course-local model, không chứng minh
tương thích production VuaCóc.
