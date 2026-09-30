"""
Text Analyzer 📝
================
Phân tích văn bản chi tiết: đếm ký tự/từ/câu, tìm từ dài/ngắn,
thống kê tần suất từ và in top 5.
"""

print("=" * 50)
print("         TEXT ANALYZER")
print("=" * 50)

choice = input("Đọc từ file (f) hay nhập tay (t)? [f/t]: ").strip().lower()

if choice == "f":
    filepath = input("Đường dẫn file: ").strip()
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
else:
    text = input("Nhập đoạn văn bản: ")

print("\n" + "=" * 50)
print("         KẾT QUẢ PHÂN TÍCH")
print("=" * 50)

# 1. Đếm số ký tự, số từ, số câu
num_chars = len(text)
num_words = len(text.split())
num_sentences = text.count(".") + text.count("!") + text.count("?")

print(f"\n--- Thống kê cơ bản ---")
print(f"Số ký tự: {num_chars}")
print(f"Số từ: {num_words}")
print(f"Số câu: {num_sentences}")

# 2. Tìm từ dài nhất, từ ngắn nhất
words = text.split()
words_clean = [w.strip(".,!?;:\"'()[]{}") for w in words]
words_nonempty = [w for w in words_clean if w]

if words_nonempty:
    longest = max(words_nonempty, key=len)
    shortest = min(words_nonempty, key=len)
    print(f"\n--- Từ vựng ---")
    print(f"Từ dài nhất: '{longest}' ({len(longest)} ký tự)")
    print(f"Từ ngắn nhất: '{shortest}' ({len(shortest)} ký tự)")

    # 3. Đết tần suất mỗi từ → in top 5
    freq = {}
    for w in words_nonempty:
        w_lower = w.lower()
        if w_lower.isalpha():
            freq[w_lower] = freq.get(w_lower, 0) + 1

    print(f"\n--- Top 5 từ phổ biến ---")
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for i, (word, count) in enumerate(sorted_words[:5], 1):
        print(f"{i}. '{word}' — {count} lần")

print("=" * 50)
