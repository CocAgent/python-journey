"""Các ca kiểm thử công khai cho Đề ôn tập 01.

Mỗi trong 10 bài nhỏ được tối đa 1.00 điểm. Các bài giống nhau về
kiến thức với đề mẫu Drive nhưng là bộ ôn tập mới, không phải đề thi chính thức.
Đáp án tham khảo và các ca kiểm thử đều công khai cho mục đích học.
"""

import json

CASES = json.loads(r'''{
  "Cau1a": {
    "function": "parity",
    "cases": [
      {
        "args": [
          4
        ],
        "returns": "Chan",
        "type": "str"
      },
      {
        "args": [
          7
        ],
        "returns": "Le",
        "type": "str"
      },
      {
        "args": [
          0
        ],
        "returns": "Chan",
        "type": "str"
      },
      {
        "args": [
          -3
        ],
        "returns": "Le",
        "type": "str"
      },
      {
        "args": [
          true
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "4"
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau1b": {
    "function": "greet",
    "cases": [
      {
        "args": [
          "An",
          20
        ],
        "returns": "Xin chào An, bạn 20 tuổi.",
        "type": "str"
      },
      {
        "args": [
          "  Hà  ",
          22
        ],
        "returns": "Xin chào Hà, bạn 22 tuổi.",
        "type": "str"
      },
      {
        "args": [
          "Mít",
          0
        ],
        "returns": "Xin chào Mít, bạn 0 tuổi.",
        "type": "str"
      },
      {
        "args": [
          "",
          18
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "A",
          121
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "A",
          true
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau2a": {
    "function": "sum_even",
    "cases": [
      {
        "args": [
          2,
          10
        ],
        "returns": 30,
        "type": "int"
      },
      {
        "args": [
          5,
          11
        ],
        "returns": 24,
        "type": "int"
      },
      {
        "args": [
          -2,
          2
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          3,
          3
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          4,
          4
        ],
        "returns": 4,
        "type": "int"
      },
      {
        "args": [
          6,
          2
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          true,
          10
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau2b": {
    "function": "count_digits_slice",
    "cases": [
      {
        "args": [
          "abc12345",
          1,
          8
        ],
        "returns": 5,
        "type": "int"
      },
      {
        "args": [
          "a1b2c3d4e5",
          2,
          9
        ],
        "returns": 4,
        "type": "int"
      },
      {
        "args": [
          "python3.9",
          7,
          9
        ],
        "returns": 2,
        "type": "int"
      },
      {
        "args": [
          "abcdef",
          1,
          6
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          "a１２b",
          1,
          4
        ],
        "returns": 0,
        "type": "int"
      },
      {
        "args": [
          "a2b",
          2,
          2
        ],
        "returns": 1,
        "type": "int"
      },
      {
        "args": [
          "abc",
          0,
          2
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "abc",
          2,
          4
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "",
          1,
          1
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau3a": {
    "function": "only_strings",
    "cases": [
      {
        "args": [
          [
            100,
            "apple",
            3.14,
            "banana",
            200,
            null
          ]
        ],
        "returns": [
          "apple",
          "banana"
        ],
        "type": "list"
      },
      {
        "args": [
          [
            "a",
            "b",
            1
          ]
        ],
        "returns": [
          "a",
          "b"
        ],
        "type": "list"
      },
      {
        "args": [
          []
        ],
        "returns": [],
        "type": "list"
      },
      {
        "args": [
          [
            true,
            false,
            0,
            ""
          ]
        ],
        "returns": [
          ""
        ],
        "type": "list"
      },
      {
        "args": [
          "not-a-list"
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau3b": {
    "function": "inventory_steps",
    "cases": [
      {
        "args": [
          [
            100,
            "apple",
            3.14,
            "banana",
            200,
            null
          ]
        ],
        "returns": {
          "after_append": [
            100,
            "apple",
            3.14,
            "banana",
            200,
            null,
            "mango"
          ],
          "after_remove": [
            100,
            "apple",
            "banana",
            200,
            null,
            "mango"
          ],
          "after_reverse": [
            "mango",
            null,
            200,
            "banana",
            "apple",
            100
          ]
        },
        "type": "dict"
      },
      {
        "args": [
          [
            "pear",
            3.14
          ]
        ],
        "returns": {
          "after_append": [
            "pear",
            3.14,
            "mango"
          ],
          "after_remove": [
            "pear",
            "mango"
          ],
          "after_reverse": [
            "mango",
            "pear"
          ]
        },
        "type": "dict"
      },
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          "wrong"
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau4a": {
    "function": "tuple_positions",
    "cases": [
      {
        "args": [
          {
            "__tuple__": [
              "apple",
              "banana",
              "cherry",
              "date",
              "coc"
            ]
          }
        ],
        "returns": [
          "apple",
          "cherry",
          "coc"
        ],
        "type": "tuple"
      },
      {
        "args": [
          {
            "__tuple__": [
              1,
              2,
              3
            ]
          }
        ],
        "returns": [
          1,
          3,
          3
        ],
        "type": "tuple"
      },
      {
        "args": [
          {
            "__tuple__": []
          }
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          {
            "__tuple__": [
              1,
              2
            ]
          }
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          [
            "a",
            "b",
            "c"
          ]
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau4b": {
    "function": "tuple_combine",
    "cases": [
      {
        "args": [
          {
            "__tuple__": [
              1,
              2
            ]
          },
          {
            "__tuple__": [
              3,
              4
            ]
          }
        ],
        "returns": [
          [
            1,
            2,
            3,
            4
          ],
          [
            1,
            2,
            1,
            2,
            1,
            2
          ]
        ],
        "type": "tuple"
      },
      {
        "args": [
          {
            "__tuple__": []
          },
          {
            "__tuple__": [
              "A"
            ]
          }
        ],
        "returns": [
          [
            "A"
          ],
          []
        ],
        "type": "tuple"
      },
      {
        "args": [
          {
            "__tuple__": [
              "X"
            ]
          },
          {
            "__tuple__": []
          }
        ],
        "returns": [
          [
            "X"
          ],
          [
            "X",
            "X",
            "X"
          ]
        ],
        "type": "tuple"
      },
      {
        "args": [
          [
            1,
            2
          ],
          {
            "__tuple__": [
              3
            ]
          }
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau5a": {
    "function": "char_frequency",
    "cases": [
      {
        "args": [
          "hello world"
        ],
        "returns": {
          "h": 1,
          "e": 1,
          "l": 3,
          "o": 2,
          " ": 1,
          "w": 1,
          "r": 1,
          "d": 1
        },
        "type": "dict"
      },
      {
        "args": [
          ""
        ],
        "returns": {},
        "type": "dict"
      },
      {
        "args": [
          "aAa"
        ],
        "returns": {
          "a": 2,
          "A": 1
        },
        "type": "dict"
      },
      {
        "args": [
          "aáa"
        ],
        "returns": {
          "a": 2,
          "á": 1
        },
        "type": "dict"
      },
      {
        "args": [
          123
        ],
        "raises": "ValueError"
      }
    ]
  },
  "Cau5b": {
    "function": "high_scores",
    "cases": [
      {
        "args": [
          {
            "An": 8,
            "Binh": 6,
            "Cuong": 9,
            "Dung": 5,
            "Hoa": 8
          },
          8
        ],
        "returns": [
          "An",
          "Cuong",
          "Hoa"
        ],
        "type": "list"
      },
      {
        "args": [
          {
            "An": 8,
            "Binh": 6
          },
          6
        ],
        "returns": [
          "An",
          "Binh"
        ],
        "type": "list"
      },
      {
        "args": [
          {
            "An": 8,
            "Binh": 6
          },
          10
        ],
        "returns": [],
        "type": "list"
      },
      {
        "args": [
          {},
          5
        ],
        "returns": [],
        "type": "list"
      },
      {
        "args": [
          {
            "An": true
          },
          5
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          {
            "An": 11
          },
          8
        ],
        "raises": "ValueError"
      },
      {
        "args": [
          {
            "An": 8
          },
          true
        ],
        "raises": "ValueError"
      }
    ]
  }
}''')
EXPECTED_FILES = tuple(CASES)
