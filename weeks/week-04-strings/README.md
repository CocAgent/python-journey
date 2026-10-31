# Tuần 04 — Strings · Text Processing · Regex Mini-lab

Tuần này bạn chuẩn hóa và phân tích text bằng string methods, rồi dùng regex
chỉ khi text có pattern cần mô tả.

## Outcomes

- indexing, slicing và f-string;
- `strip`, `split`, `join`, `replace`, `find`, `count`;
- text normalization;
- phân biệt khi string methods là đủ và khi regex hữu ích;
- dùng raw string, `re.search`, `re.findall`, `re.fullmatch` với pattern nhỏ.

## Learning path

```text
README → notes → examples → exercises → hints
       → regex mini-lab → machine check → Text Analyzer → evidence
```

Đọc [`notes.md`](notes.md), chạy [`examples/`](examples/), hoàn thành bốn
[`exercises/`](exercises/), xem [`hints.md`](hints.md), chạy
[machine check](checks/README.md), rồi làm [Text Analyzer](mini-project/README.md).

## Xem ví dụ — dự đoán kết quả — tự làm bài tương tự

Bắt đầu từ [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md) để học
theo vòng **Dự đoán → Chạy → Đọc lỗi → Thay input → Tự viết → Kiểm chứng**.

| Ví dụ mới | Kiến thức | Lỗi quan trọng |
|---|---|---|
| `04_predict_slice_and_find.py` | index, slice, `find` | Chuỗi rỗng và `IndexError` |
| `05_normalize_words_step_by_step.py` | `strip/split/join/count/replace` | Đếm `pythonic` nhầm thành từ `python` |
| `06_regex_search_vs_fullmatch.py` | `search/findall/fullmatch` | Chấp nhận nhầm `EV-123X` |

Chạy ở **gốc repository**:

```bash
python weeks/week-04-strings/examples/04_predict_slice_and_find.py
python weeks/week-04-strings/examples/05_normalize_words_step_by_step.py
python weeks/week-04-strings/examples/06_regex_search_vs_fullmatch.py
```

Sau đó mở [**3 bài tương tự**](practice/README.md): truy cập chuỗi,
chuẩn hóa câu và kiểm mã vé giả lập. Mỗi bài có starter TODO,
lời giải tham khảo tách biệt và máy kiểm **chính code sinh viên**:

```bash
python weeks/week-04-strings/practice/checks/check_practice.py --starter
```

**Starter chưa hoàn thiện sẽ FAIL có chủ đích.** Lệnh `--solutions`
chỉ kiểm đáp án mẫu, không chứng minh sinh viên đã tự làm xong.
Bộ thực hành mới không thay bốn exercises, rubric hoặc Text Analyzer cũ.

## Boundary

Pattern email, phone hoặc code trong tuần này là deliberately simplified
teaching pattern, không phải universal validation standard.

## Evidence

- output `Week 04 solution checks: PASS`;
- một case string methods đủ dùng;
- một case regex giúp tìm nhiều pattern;
- normal, no-match và invalid-format cases.
