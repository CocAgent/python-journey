"""Lời giải Lab 02 — count trên các từ sau split, không trên chuỗi con."""

sentence = input("Câu: ")
words = sentence.lower().split()

if not words:
    print("Câu không được rỗng")
else:
    normalized = " ".join(words)
    print(f"Chuẩn hóa: {normalized}")
    print(f"Số từ: {len(words)}")
    print(f"Từ python: {words.count('python')}")
