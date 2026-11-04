tests = {
    # Câu 1a: Nhập 2 số thực, in tổng và hiệu
    "Cau1a": [
        {"input": "5\n", "expected": ["Duong"]},
        {"input": "-10\n", "expected": ["Am"]},
        {"input": "0\n", "expected": ["Khong"]}
    ],

    # Câu 1b: Nhập tên và tuổi, in theo mẫu
    "Cau1b": [
        {"input": "Ha Noi\n24\n", "expected": "ha noi co ma vung 24"},
        {"input": "Đà Nẵng\n236\n", "expected": "da nang co ma vung 236"}
    ],

    # Câu 2a: In bảng bình phương các số nguyên từ 1 đến 10
    "Cau2a": [
        {"input": "-5\n5\n", "expected": ["-15"]},   # -5+-4+-3+-2+-1 = -15
        {"input": "-3\n2\n", "expected": ["-6"]},    # -3+-2+-1 = -6
        {"input": "0\n5\n", "expected": ["0"]},      # Không có số âm
        {"input": "-2\n-2\n", "expected": ["-2"]},   # Chỉ có -2
        {"input": "1\n4\n", "expected": ["0"]}       # Không có số âm
    ],

    # Câu 2b: 
    "Cau2b":[
        # Chuỗi "Python", đếm nguyên âm từ vị trí 2 đến 5 là "ytho" (chỉ 'o'), kết quả: 1
        {"input": "Python\n2\n5\n", "expected": ["1"]},

        # Chuỗi "Education", đếm từ 1 đến 9 (toàn bộ), có 'E','u','a','i','o' = 5 nguyên âm
        {"input": "Education\n1\n9\n", "expected": ["5"]},

        # Chuỗi "abcdef", từ 2 đến 5 là "bcde", nguyên âm chỉ 'e' → 1
        {"input": "abcdef\n2\n5\n", "expected": ["1"]},

        # Chuỗi "aeiouAEIOU", từ 1 đến 10 (toàn bộ), tất cả đều nguyên âm → 10
        {"input": "aeiouAEIOU\n1\n10\n", "expected": ["10"]},

        # Chuỗi "xyz", từ 1 đến 3, không có nguyên âm → 0
        {"input": "xyz\n1\n3\n", "expected": ["0"]}
    ],
    # Câu 3:
    "Cau3a": [
        {
            "input": "",
            "expected": ["[100, 3.14, 200]"]
        }
    ], 
    "Cau3b": [
        {
            "input": "",
            "expected": [
                "1",                       # 200 xuất hiện 1 lần
                "3",                       # "banana" ở index 3
                "[100, 'apple', 'grape', 3.14, 'banana', 200, None]" # sau khi chèn
            ]
        }
    ],

   
    # 4a: 
    "Cau4a": [
        {"input": "", "expected": ["()", "(5,)", "(10, 'apple', 3.14)"]}
    ],

    # 4b: 
    "Cau4b":  [
        {"input": "", "expected": ["TypeError"]}
    ],


    # Câu 5a: 
    "Cau5a": [
        {"input": "", "expected": ["45"]}
    ],

    # Câu 5b: 
    "Cau5b": [
        {"input": "", "expected": ["apple"]}
    ]
}
