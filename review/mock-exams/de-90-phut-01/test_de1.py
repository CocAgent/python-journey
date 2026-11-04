"""Public self-study cases for the extended 90-minute exam.

Five questions × 2 points; two tasks each × 1 point. Test outcomes are
fully disclosed, so scores here are formative, not official exam grades.
"""

import json

CASES = json.loads(r'''{
  "Cau1a": {
    "kind": "function",
    "function": "count_divisible_by_three_digits",
    "cases": [
      {
        "args": [
          1
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          3
        ],
        "returns": 1,
        "type": "int"
      },
      {
        "args": [
          30
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          909
        ],
        "returns": 3,
        "type": "int"
      },
      {
        "args": [
          1500
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          1236
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          1501
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          true
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "123"
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau1b": {
    "kind": "function",
    "function": "harmonic_sum",
    "cases": [
      {
        "args": [
          1
        ],
        "returns": 1,
        "type": "float"
      },
      {
        "args": [
          2
        ],
        "returns": 1.5,
        "type": "float"
      },
      {
        "args": [
          3
        ],
        "returns": 1.8333333333333333,
        "type": "float"
      },
      {
        "args": [
          10
        ],
        "returns": 2.9289682539682538,
        "type": "float"
      },
      {
        "args": [
          100
        ],
        "returns": 5.187377517639621,
        "type": "float"
      },
      {
        "args": [
          1500
        ],
        "returns": 7.8907693482881305,
        "type": "float"
      },
      {
        "args": [
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          1501
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          true
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "2"
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau2a": {
    "kind": "function",
    "function": "count_uppercase",
    "cases": [
      {
        "args": [
          "AbC"
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          "Xin Chào THẾ GIỚI"
        ],
        "returns": 9,
        "type": "int"
      },
      {
        "args": [
          ""
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          "abc 123"
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          "ÁaÀz"
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          123
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          null
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau2b": {
    "kind": "function",
    "function": "is_palindrome",
    "cases": [
      {
        "args": [
          "Madam"
        ],
        "returns": true,
        "type": "bool"
      },
      {
        "args": [
          "A man, a plan, a canal: Panama!"
        ],
        "returns": true,
        "type": "bool"
      },
      {
        "args": [
          "abba"
        ],
        "returns": true,
        "type": "bool"
      },
      {
        "args": [
          "python"
        ],
        "returns": false,
        "type": "bool"
      },
      {
        "args": [
          "12 21"
        ],
        "returns": true,
        "type": "bool"
      },
      {
        "args": [
          "   ..."
        ],
        "returns": false,
        "type": "bool"
      },
      {
        "args": [
          ""
        ],
        "returns": false,
        "type": "bool"
      },
      {
        "args": [
          42
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau3a": {
    "kind": "function",
    "function": "count_even_before_zero",
    "cases": [
      {
        "args": [
          [
            2,
            3,
            4,
            5,
            0,
            6
          ]
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          [
            1,
            3,
            5,
            0
          ]
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          [
            0
          ]
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          [
            10,
            10,
            0
          ]
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          [
            2,
            0,
            -1
          ]
        ],
        "returns": 1,
        "type": "int"
      },
      {
        "args": [
          [
            2,
            4
          ]
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            2,
            -1,
            0
          ]
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            true,
            0
          ]
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "1,2,0"
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau3b": {
    "kind": "function",
    "function": "count_value_before_zero",
    "cases": [
      {
        "args": [
          [
            1,
            2,
            2,
            3,
            0,
            2
          ],
          2
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          [
            3,
            3,
            3,
            0
          ],
          3
        ],
        "returns": 3,
        "type": "int"
      },
      {
        "args": [
          [
            0
          ],
          3
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          [
            1,
            2,
            3,
            0
          ],
          9
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          [
            2,
            0,
            -1
          ],
          2
        ],
        "returns": 1,
        "type": "int"
      },
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            1,
            -2,
            0
          ],
          1
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            1,
            0
          ],
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            1,
            0
          ],
          true
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "1,2,0",
          1
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau4a": {
    "kind": "function",
    "function": "make_book",
    "cases": [
      {
        "args": [
          " S01 ",
          " Python cơ bản ",
          " Giảng viên A ",
          2020,
          150000
        ],
        "returns": {
          "id": "S01",
          "title": "Python cơ bản",
          "author": "Giảng viên A",
          "year": 2020,
          "price": 150000
        },
        "type": "dict"
      },
      {
        "args": [
          "B2",
          "OOP",
          "N.N.",
          2100,
          0
        ],
        "returns": {
          "id": "B2",
          "title": "OOP",
          "author": "N.N.",
          "year": 2100,
          "price": 0
        },
        "type": "dict"
      },
      {
        "args": [
          "",
          "OOP",
          "N",
          2020,
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "B",
          " ",
          "N",
          2020,
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "B",
          "OOP",
          "N",
          true,
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "B",
          "OOP",
          "N",
          1899,
          0
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "B",
          "OOP",
          "N",
          2020,
          -1
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "B",
          "OOP",
          "N",
          2020,
          true
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau4b": {
    "kind": "function",
    "function": "remove_book",
    "cases": [
      {
        "args": [
          [
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            },
            {
              "id": "S02",
              "title": "Cấu trúc dữ liệu",
              "author": "Giảng viên B",
              "year": 2024,
              "price": 200000
            }
          ],
          "S01"
        ],
        "returns": [
          {
            "id": "S02",
            "title": "Cấu trúc dữ liệu",
            "author": "Giảng viên B",
            "year": 2024,
            "price": 200000
          }
        ],
        "type": "list"
      },
      {
        "args": [
          [
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            },
            {
              "id": "S02",
              "title": "Cấu trúc dữ liệu",
              "author": "Giảng viên B",
              "year": 2024,
              "price": 200000
            }
          ],
          "S02"
        ],
        "returns": [
          {
            "id": "S01",
            "title": "Python cơ bản",
            "author": "Giảng viên A",
            "year": 2020,
            "price": 150000
          }
        ],
        "type": "list"
      },
      {
        "args": [
          [
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            }
          ],
          "S01"
        ],
        "returns": [],
        "type": "list"
      },
      {
        "args": [
          [
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            },
            {
              "id": "S02",
              "title": "Cấu trúc dữ liệu",
              "author": "Giảng viên B",
              "year": 2024,
              "price": 200000
            }
          ],
          "UNKNOWN"
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [],
          "S01"
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            },
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            }
          ],
          "S01"
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            "bad"
          ],
          "S01"
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            {
              "id": "S01",
              "title": "Python cơ bản",
              "author": "Giảng viên A",
              "year": 2020,
              "price": 150000
            }
          ],
          123
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau5a": {
    "kind": "class",
    "class": "DienThoai",
    "cases": [
      {
        "args": [
          "DT01",
          "Thiết bị A",
          "Hãng A",
          4500,
          12000000
        ],
        "returns": {
          "MaMay": "DT01",
          "TenMay": "Thiết bị A",
          "HangSanXuat": "Hãng A",
          "DungLuongPin": 4500,
          "GiaBan": 12000000,
          "info": "DT01 | Thiết bị A | Hãng A | 4500 mAh | 12000000 VND"
        },
        "type": "class"
      },
      {
        "args": [
          " X1 ",
          "  Máy thử ",
          " Hãng X ",
          1,
          0
        ],
        "returns": {
          "MaMay": "X1",
          "TenMay": "Máy thử",
          "HangSanXuat": "Hãng X",
          "DungLuongPin": 1,
          "GiaBan": 0,
          "info": "X1 | Máy thử | Hãng X | 1 mAh | 0 VND"
        },
        "type": "class"
      },
      {
        "args": [
          "",
          "Máy A",
          "Hãng A",
          4000,
          100
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "DT1",
          "",
          "Hãng A",
          4000,
          100
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "DT1",
          "Máy A",
          "Hãng A",
          true,
          100
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "DT1",
          "Máy A",
          "Hãng A",
          0,
          100
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "DT1",
          "Máy A",
          "Hãng A",
          4000,
          -1
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau5b": {
    "kind": "factory",
    "function": "tao_danh_sach_dien_thoai",
    "cases": [
      {
        "args": [],
        "returns": [
          {
            "MaMay": "DT01",
            "TenMay": "Thiết bị A",
            "HangSanXuat": "Hãng A",
            "DungLuongPin": 4500,
            "GiaBan": 12000000,
            "info": "DT01 | Thiết bị A | Hãng A | 4500 mAh | 12000000 VND"
          },
          {
            "MaMay": "DT02",
            "TenMay": "Thiết bị B",
            "HangSanXuat": "Hãng B",
            "DungLuongPin": 5000,
            "GiaBan": 15000000,
            "info": "DT02 | Thiết bị B | Hãng B | 5000 mAh | 15000000 VND"
          }
        ],
        "type": "list"
      }
    ]
  }
}''')
EXPECTED_FILES = tuple(CASES)
