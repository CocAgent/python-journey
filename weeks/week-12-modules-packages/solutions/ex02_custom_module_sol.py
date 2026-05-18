"""Lời giải Bài tập 02: Tạo module riêng

Tạo file my_utils.py cùng thư mục với nội dung:

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")

if __name__ == "__main__":
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°F = {fahrenheit_to_celsius(100):.1f}°C")
    print(f"10km = {km_to_miles(10):.2f} miles")
    print(f"racecar palindrome: {is_palindrome('racecar')}")
    print(f"Vowels in hello: {count_vowels('hello')}")
"""

# Sau khi tạo my_utils.py, import ở đây:
# from my_utils import celsius_to_fahrenheit, is_palindrome
# print(celsius_to_fahrenheit(37))
# print(is_palindrome("racecar"))
