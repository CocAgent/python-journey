# W13 — Modules, CLI + Arena Adapter Boundary

## Python focus

Modules, packages, dependencies, CLI và API/HTTP concepts.

## Milestone

Tách code thành hai vùng trách nhiệm:

```text
bot core → quyết định từ course state
adapter  → chuyển đổi giữa core và môi trường bên ngoài
```

Bot core phải chạy và test độc lập. Một CLI local có thể nhận teaching input,
gọi core và in teaching action để chứng minh boundary.

```text
ARENA_ADAPTER_STATUS = DESIGN_ONLY
VUACOC_RUNTIME_CONTRACT = UNVERIFIED
```

## Design questions

- Module nào sở hữu decision logic?
- Dữ liệu nào đi qua adapter boundary?
- Lỗi chuyển đổi được báo ở đâu?
- Làm sao test bot core mà không cần runtime?

## Constraints

- Không tạo endpoint giả.
- Không đoán authentication, request/response schema hoặc submission command.
- Không để network call nằm trong bot core.

## Evidence

- Sơ đồ module và dependency direction.
- CLI local hoặc contract local có nhãn teaching-only.
- Bot core tests vẫn chạy không cần adapter.
- Các câu hỏi production chưa đo được trỏ tới `INTEGRATION_CONTRACT.md`.
