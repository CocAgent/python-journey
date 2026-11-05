"""Official solutions for ordered conditionals."""


def age_group(age: int) -> str:
    if age < 13:
        return "Thiếu nhi"
    if age < 18:
        return "Thiếu niên"
    if age < 65:
        return "Người lớn"
    return "Người cao tuổi"


def classify_score(score: float) -> str:
    if score < 0 or score > 10:
        return "Không hợp lệ"
    if score >= 9:
        return "Xuất sắc"
    if score >= 8:
        return "Giỏi"
    if score >= 6.5:
        return "Khá"
    if score >= 5:
        return "Trung bình"
    return "Yếu"


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
