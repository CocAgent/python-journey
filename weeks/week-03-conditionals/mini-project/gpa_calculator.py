"""
Máy tính điểm GPA 📊
====================================
1. Nhập số lượng môn học
2. Nhập thông tin từng môn: Tên, Số tín chỉ, Điểm hệ 10
3. Quy đổi điểm hệ 10 sang hệ 4: điểm_4 = điểm_10 * 4 / 10
4. Tính GPA = Σ(điểm_4 * tín_chỉ) / Σ tín_chỉ
5. Xếp loại học lực
6. In bảng điểm chi tiết, đẹp mắt
"""

def main():
    print("=" * 50)
    print(f"{'MÁY TÍNH ĐIỂM GPA':^50}")
    print("=" * 50)
    
    while True:
        try:
            num_courses = int(input("Nhập số lượng môn học: "))
            if num_courses <= 0:
                print("Số lượng môn học phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
            
    courses = []
    total_credits = 0
    total_weighted_score = 0
    
    for i in range(1, num_courses + 1):
        print(f"\n--- Môn học thứ {i} ---")
        name = input("Tên môn học: ").strip()
        if not name:
            name = f"Môn học {i}"
            
        while True:
            try:
                credits = int(input("Số tín chỉ: "))
                if credits <= 0:
                    print("Số tín chỉ phải lớn hơn 0. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")
                
        while True:
            try:
                score_10 = float(input("Điểm hệ 10: "))
                if not (0 <= score_10 <= 10):
                    print("Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số thực hợp lệ.")
                
        # Quy đổi sang hệ 4
        score_4 = score_10 * 4.0 / 10.0
        
        courses.append({
            "name": name,
            "credits": credits,
            "score_10": score_10,
            "score_4": score_4
        })
        
        total_credits += credits
        total_weighted_score += score_4 * credits

    if total_credits == 0:
        print("\nKhông có tín chỉ nào để tính toán.")
        return
        
    gpa = total_weighted_score / total_credits
    
    # Xếp loại
    if gpa >= 3.6:
        classification = "Xuất sắc"
    elif gpa >= 3.2:
        classification = "Giỏi"
    elif gpa >= 2.5:
        classification = "Khá"
    elif gpa >= 2.0:
        classification = "Trung bình"
    else:
        classification = "Yếu"
        
    # In kết quả
    print("\n" + "=" * 60)
    print(f"{'BẢNG ĐIỂM CHI TIẾT':^60}")
    print("=" * 60)
    print(f"{'STT':<5}{'TÊN MÔN HỌC':<25}{'TÍN CHỈ':<10}{'ĐIỂM HỆ 10':<12}{'ĐIỂM HỆ 4':<10}")
    print("-" * 60)
    for index, course in enumerate(courses, 1):
        # Truncate course name if too long for display
        display_name = course["name"]
        if len(display_name) > 22:
            display_name = display_name[:19] + "..."
        print(f"{index:<5}{display_name:<25}{course['credits']:<10}{course['score_10']:<12.1f}{course['score_4']:<10.2f}")
    print("-" * 60)
    print(f"Tổng số tín chỉ: {total_credits}")
    print(f"Điểm trung bình tích lũy (GPA): {gpa:.2f} / 4.00")
    print(f"Xếp loại học lực: {classification}")
    print("=" * 60)

if __name__ == "__main__":
    main()
