# Baseline bots

Ba baseline nhỏ cung cấp điểm so sánh minh bạch cho Line Arena. Tất cả đều
deterministic, không randomness, không hidden state và không network.

| Baseline | Policy |
|---|---|
| WaitBot | luôn trả `wait` |
| ForwardBot | đi một bước về `goal`, hoặc `wait` nếu đã tới goal |
| CautiousBot | `wait` khi opponent cách không quá một bước, còn lại đi về goal |

Các bot dùng course-local state/action contract trong
[`../local_arena/CONTRACT.md`](../local_arena/CONTRACT.md).

> This is a Python Journey teaching contract. It is not the production
> contract of vuacoc.com.

Baseline dùng để quan sát và giải thích behavior. Student Bot không bắt buộc
thắng baseline ở W07 và không có win-percentage requirement trong project này.
