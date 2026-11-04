tests = {
    # Câu 1a: Nhập 2 số thực, in tổng và hiệu
    "Cau1a":  [
        {"input": "4\n", "expected": ["chan"]},
        {"input": "7\n", "expected": ["le"]},
        {"input": "0\n", "expected": ["chan"]},
        {"input": "-3\n", "expected": ["le"]}
    ],

    # Câu 1b: Nhập tên và tuổi, in theo mẫu
    "Cau1b": [
        {"input": "An\n20\n", "expected": "Xin chào An, bạn 20 tuổi."},
        {"input": "Long\n18\n", "expected": "Xin chào Long, bạn 18 tuổi."},
        {"input": "Hà\n22\n", "expected": "Xin chào Hà, bạn 22 tuổi."}
    ],

    # Câu 2a: In bảng bình phương các số nguyên từ 1 đến 10
    "Cau2a":  [
        {"input": "2\n10\n", "expected": ["30"]},   # 2+4+6+8+10=30
        {"input": "5\n11\n", "expected": ["24"]},   # 6+8+10=24
        {"input": "3\n3\n", "expected": ["0"]},     # 3 là lẻ, không có số chẵn
        {"input": "4\n4\n", "expected": ["4"]},     # 4 là chẵn
        {"input": "-2\n2\n", "expected": ["0"]}     # -2+0+2=0
    ],

    # Câu 2b: 
    "Cau2b":[
        {"input": "abc12345\n1\n8\n", "expected": ["5"]},      # 5 chữ số từ vị trí 4 đến 8 là 1,2,3,4,5
        {"input": "a1b2c3d4e5\n2\n9\n", "expected": ["4"]},   # 1,2,3,4 trong chuỗi từ vị trí 2 đến 9
        {"input": "python3.9\n7\n9\n", "expected": ["2"]},    # 3,9 từ vị trí 7 đến 9
        {"input": "abcdef\n1\n6\n", "expected": ["0"]},       # Không có chữ số
        {"input": "a2b\n2\n2\n", "expected": ["1"]}           # Vị trí 2 là '2'
    ],
    # Câu 3:
    "Cau3a": [
        {
            "input": "",
            "expected": ["['apple', 'banana']"]
        }
    ], 

    "Cau3b": [
        {
            "input": "",
            "expected": [
                "[100, 'apple', 3.14, 'banana', 200, None, 'orange']",
                "[100, 'apple', 'banana', 200, None, 'orange']",
                "['orange', None, 200, 'banana', 'apple', 100]"
            ]
        }
    ],
    
    # 4a: List số thực, in max và min (mỗi dòng 1 số)
    "Cau4a":  [
        {"input": "", "expected": ["apple", "cherry", "coc"]}
    ],

    # 4b: Hàm lọc số lẻ trong tuple, in ra tuple kết quả
    "Cau4b": [
        {"input": "", "expected": ["(1, 2, 3, 4)", "(1, 2, 1, 2, 1, 2)"]}
    ],


    # Câu 5a: 
    "Cau5a": [
        {"input": "", "expected": ["{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}"]}
    ],

    # Câu 5b: 
    "Cau5b": [
        {"input": "", "expected": ["['An', 'Cuong', 'Hoa']"]}
    ]
}
