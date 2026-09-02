"""Normalize user-facing text with string methods."""

raw_text = "  Python   Journey  "
words = raw_text.strip().lower().split()
normalized = " ".join(words)

print(normalized)
print(normalized.replace("journey", "course"))
print(f"python index={normalized.find('python')}")
