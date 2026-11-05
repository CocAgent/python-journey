"""Lời giải Lab 03 — kiểm TOÀN BỘ mã, không kiểm khớp một phần."""

import re

code = input("Mã vé: ").strip()
if re.fullmatch(r"EV-[0-9]{3}", code) is not None:
    print(f"Mã hợp lệ: {code}")
else:
    print("Mã không hợp lệ")
