# Mini-project — Decision Dashboard

Xây một dashboard terminal đọc structured state và đưa ra một recommendation
có thể giải thích. Project luyện data modeling, không yêu cầu file I/O.

## Data model tối thiểu

Model của bạn cần:

- một `dict` chính;
- ít nhất một nested `dict` hoặc `list`;
- một `set` cho tags, capabilities hoặc allowed values;
- một quyết định về field nào bắt buộc và field nào tùy chọn.

## Functions tối thiểu

1. `validate_state(state)` kiểm tra các field bắt buộc;
2. `summarize_state(state)` tạo summary dễ đọc;
3. `recommend_action(state)` trả recommendation;
4. `main()` ghép luồng chạy.

Basic type hints được khuyến khích khi chúng làm input/output rõ hơn.

## Definition of done

- [ ] Starter được hoàn thiện và chạy từ terminal.
- [ ] Dict, set và nested data đều có vai trò rõ ràng.
- [ ] Recommendation dựa trên 2–4 rules dễ giải thích.
- [ ] Có normal case, boundary case và optional field bị thiếu.
- [ ] Output giải thích data-modeling decision.
- [ ] Commit ghi lại evidence và một lỗi đã sửa.

Chạy từ repository root:

```bash
python weeks/week-08-dicts-sets/mini-project/starter.py
```

Bạn có thể dùng state của riêng mình. Nếu dùng bot state, đó chỉ là:

```text
COURSE TEACHING MODEL
NOT VUACOC PRODUCTION CONTRACT
```

## Bài đệm trước Decision Dashboard

Để tránh nhầm `dict.get` với validation hoặc `set` với
list có thứ tự, hãy xem [3 ví dụ có giải thích](../WORKED-EXAMPLES.md)
và tự hoàn thiện [4 bài tương tự](../practice/README.md).
Khi quay lại Dashboard, hãy vẽ:

```text
Required fields → Valid? → Summarize → Recommend → Explain
```

Với input không hợp lệ, đừng in một recommendation như thể
schema đã được xác nhận. Các action và vị trí chỉ là
**teaching model course-local**, không thuộc production VuaCóc.

Bộ bổ sung không thay yêu cầu hoàn thành và thang điểm hiện hành.
