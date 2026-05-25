"""
Text Analyzer 📝
====================================
1. Nhập văn bản trực tiếp hoặc đọc từ file.
2. Thống kê: số ký tự (tổng số và không tính khoảng trắng), số từ, số câu.
3. Xác định từ dài nhất và ngắn nhất.
4. Thống kê tần suất xuất hiện của các từ, tìm top 5 từ phổ biến nhất.
5. Hiển thị báo cáo thống kê trực quan và đẹp mắt.
"""

import os
import re

def clean_text_to_words(text):
    # Chuyển về chữ thường
    text_lower = text.lower()
    # Loại bỏ các ký tự đặc biệt và dấu câu, thay thế bằng khoảng trắng
    cleaned = re.sub(r'[^\w\s]', ' ', text_lower)
    # Tách từ
    words = cleaned.split()
    return words

def analyze_text(text):
    if not text.strip():
        return None

    # 1. Đếm ký tự
    char_count_total = len(text)
    char_count_no_space = len(text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t", ""))

    # 2. Đếm số câu
    # Một câu thường kết thúc bằng các dấu ., !, ?
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    if sentence_count == 0 and len(text.strip()) > 0:
        sentence_count = 1

    # 3. Đếm từ
    words = clean_text_to_words(text)
    word_count = len(words)

    if word_count == 0:
        return {
            "char_count_total": char_count_total,
            "char_count_no_space": char_count_no_space,
            "word_count": 0,
            "sentence_count": sentence_count,
            "longest_word": "",
            "shortest_word": "",
            "top_words": []
        }

    # 4. Tìm từ dài nhất và ngắn nhất
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    # 5. Đếm tần suất từ
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sắp xếp để tìm top 5
    sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    top_words = sorted_words[:5]

    return {
        "char_count_total": char_count_total,
        "char_count_no_space": char_count_no_space,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "top_words": top_words
    }

def main():
    print("=" * 60)
    print(f"{'TEXT ANALYZER 📝':^60}")
    print("=" * 60)
    print("1. Nhập văn bản trực tiếp từ bàn phím")
    print("2. Đọc văn bản từ file (.txt)")
    print("-" * 60)
    
    choice = input("Lựa chọn của bạn (1/2): ").strip()
    text = ""

    if choice == "2":
        file_path = input("Nhập đường dẫn tới file (.txt): ").strip()
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                print(f"Đọc thành công từ file: {file_path}")
            except Exception as e:
                print(f"Có lỗi khi đọc file: {e}")
                return
        else:
            print("File không tồn tại! Vui lòng chạy lại chương trình.")
            return
    else:
        print("Nhập văn bản của bạn (Nhấn Enter hai lần liên tiếp để kết thúc):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)

    if not text.strip():
        print("Văn bản trống. Không có gì để phân tích!")
        return

    results = analyze_text(text)
    
    print("\n" + "=" * 60)
    print(f"{'KẾT QUẢ PHÂN TÍCH VĂN BẢN':^60}")
    print("=" * 60)
    
    print(f"{'THÔNG SỐ':<35}{'GIÁ TRỊ':>25}")
    print("-" * 60)
    print(f"{'- Tổng số ký tự (cả khoảng trắng):':<35}{results['char_count_total']:>25,}")
    print(f"{'- Số ký tự không tính khoảng trắng:':<35}{results['char_count_no_space']:>25,}")
    print(f"{'- Tổng số từ:':<35}{results['word_count']:>25,}")
    print(f"{'- Tổng số câu:':<35}{results['sentence_count']:>25,}")
    
    if results['word_count'] > 0:
        print(f"{'- Từ dài nhất:':<35}{f'{results['longest_word']} ({len(results['longest_word'])} ký tự)':>25}")
        print(f"{'- Từ ngắn nhất:':<35}{f'{results['shortest_word']} ({len(results['shortest_word'])} ký tự)':>25}")
    
    print("-" * 60)
    print(f"{'TOP 5 TỪ XUẤT HIỆN NHIỀU NHẤT':^60}")
    print("-" * 60)
    if results['top_words']:
        print(f"{'HẠNG':<10}{'TỪ':<35}{'TẦN SUẤT':>15}")
        print("-" * 60)
        for idx, (word, freq) in enumerate(results['top_words'], 1):
            print(f"{idx:<10}{word:<35}{freq:>15,}")
    else:
        print("Không có từ nào để thống kê.")
    print("=" * 60)

if __name__ == "__main__":
    main()
