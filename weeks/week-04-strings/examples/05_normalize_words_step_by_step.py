"""Ví dụ 05 — Chuẩn hóa khoảng trắng, đếm đúng TỪ thay vì chuỗi con.

Chạy từ gốc repo, không dùng Internet hoặc file:
    python weeks/week-04-strings/examples/05_normalize_words_step_by_step.py
"""

raw = "  PYTHON    la   Python   "
clean = raw.strip()
words = clean.lower().split()
normalized = " ".join(words)

print(f"Đầu vào: {raw!r}")
print(f"Sau strip: {clean!r}")
print(f"Sau split: {words}")
print(f"Sau join: {normalized!r}")
print(f"Số từ: {len(words)}")
print(f"Số từ 'python': {words.count('python')}")

# count trên chuỗi đếm cả 'python' trong 'pythonic'.
another = "python pythonic python"
print(f"Đếm chuỗi con: {another.count('python')}")
print(f"Đếm từ đơn giản: {another.split().count('python')}")

# Strings là immutable: phép thay thế trả chuỗi mới.
replaced = normalized.replace("python", "PY")
print(f"Sau replace: {replaced}")
print(f"Chuỗi gốc vẫn giữ: {normalized}")
