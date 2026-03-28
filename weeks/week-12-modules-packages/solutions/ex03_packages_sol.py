"""Lời giải Bài tập 03: pip & Virtual Environment"""
import string

# TODO 1
# a) pip là trình quản lý gói (package manager) của Python
# b) pip install requests
# c) pip list
# d) requirements.txt liệt kê các thư viện cần thiết để chạy project

# TODO 2 (chạy trong terminal, không phải trong file .py)
# python -m venv myenv
# source myenv/bin/activate    (Linux/Mac)
# myenv\Scripts\activate       (Windows)
# pip install requests
# pip freeze > requirements.txt

# TODO 3
print(f"Chữ cái: {string.ascii_letters}")
print(f"Chữ số: {string.digits}")
print(f"Dấu câu: {string.punctuation}")
