"""Starter for the Week 04 Text Analyzer."""

import re

text = input("Text: ").strip()

if not text:
    print("Text không được rỗng")
else:
    normalized = " ".join(text.lower().split())
    words = normalized.split()
    codes = re.findall(r"PJ-\d{3}", text)
    print(f"normalized={normalized}")
    print(f"characters={len(normalized)}")
    print(f"words={len(words)}")
    print(f"python_count={normalized.count('python')}")
    print(f"course_codes={codes}")
