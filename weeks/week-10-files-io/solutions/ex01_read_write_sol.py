"""Lời giải Bài tập 01: Đọc và ghi file text"""
# TODO 1
quotes = [
    "Code is read more often than it is written.\n",
    "Simplicity is the ultimate sophistication.\n",
    "Talk is cheap. Show me the code.\n",
    "First, solve the problem. Then, write the code.\n",
    "Any fool can write code that a computer can understand.\n",
]
with open("quotes.txt", "w", encoding="utf-8") as f:
    f.writelines(quotes)

# TODO 2
with open("quotes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")

# TODO 3
with open("quotes.txt", "a", encoding="utf-8") as f:
    f.write("Python is fun!\n")
    f.write("Keep coding!\n")

# TODO 4
with open("quotes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.strip().split("\n")
    words = content.split()
    chars = len(content)
print(f"Dòng: {len(lines)}, Từ: {len(words)}, Ký tự: {chars}")

# TODO 5
with open("quotes.txt", "r", encoding="utf-8") as f_in:
    with open("quotes_upper.txt", "w", encoding="utf-8") as f_out:
        f_out.write(f_in.read().upper())
