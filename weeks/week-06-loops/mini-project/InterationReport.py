"""Mini-project: Iteration Report."""

# Dữ liệu mẫu
topics = [
    "Variables & Data Types", 
    "Control Flow", 
    "Functions", 
    "List Comprehensions", 
    "Error Handling"
]
scores = [9, 7, 8, 10, 6]

print("=== BÁO CÁO ĐÁNH GIÁ CHUNG ===")
# Dùng zip(..., strict=True) để ghép và enumerate(..., start=1) để đánh số
paired_data = zip(topics, scores, strict=True)

for index, (topic, score) in enumerate(paired_data, start=1):
    print(f"{index}. {topic}: {score}/10")

print("\n=== CHỦ ĐỀ ĐẠT YÊU CẦU (ĐIỂM >= 8) ===")
# Dùng list comprehension để lọc ra các cặp topic và score có điểm >= 8
passed_topics = [(t, s) for t, s in zip(topics, scores, strict=True) if s >= 8]

# In báo cáo kết quả lọc
for index, (topic, score) in enumerate(passed_topics, start=1):
    print(f"{index}. [Pass] {topic} - Điểm: {score}")