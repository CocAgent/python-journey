
import pytest

try:
    from .decision import LOCAL_ACTIONS, choose_action, validate_turn
except ImportError:
    from decision import LOCAL_ACTIONS, choose_action, validate_turn


# Hàm hiển thị kết quả kiểm thử
def show_result(name, actual, expected):
    status = "PASS" if actual == expected else "FAIL"

    print(f"\n--- {name} ---")
    print(f"Kết quả thực tế : {actual}")
    print(f"Kết quả mong đợi: {expected}")
    print(f"Trạng thái       : {status}")

    if actual != expected:
        print(f"Lý do sai: Mong đợi '{expected}' nhưng nhận '{actual}'")


# TEST 1: Trường hợp bình thường
def test_normal_case():
    actual = choose_action(1, 4)
    expected = "right"

    show_result("TEST 1 - Normal Case", actual, expected)
    assert actual == expected
    assert actual in LOCAL_ACTIONS


# TEST 2: Đã đến mục tiêu
def test_edge_case_at_goal():
    actual = choose_action(4, 4)
    expected = "wait"

    show_result("TEST 2 - Edge Case", actual, expected)
    assert actual == expected


# TEST 3: Dữ liệu không hợp lệ
def test_invalid_turn():
    print("\n--- TEST 3 - Invalid Input ---")
    print("Đầu vào          : turn = 0")
    print("Kết quả mong đợi: ValueError")

    with pytest.raises(ValueError, match="positive"):
        validate_turn(0)

    print("Kết quả thực tế : ValueError")
    print("Trạng thái       : PASS")


# TEST 4: Kiểm tra lỗi cũ
def test_regression_position_past_goal_moves_left():
    actual = choose_action(4, 1)
    expected = "left"

    show_result("TEST 4 - Regression", actual, expected)
    assert actual == expected


# TEST 5: Cố tình kiểm tra sai
def test_wrong_case():
    actual = choose_action(1, 4)
    expected = "left"

    show_result("TEST 5 - Wrong Case", actual, expected)

    assert actual == expected, (
        f"Nhân vật ở vị trí 1, mục tiêu ở vị trí 4. "
        f"Hướng đúng là '{actual}' nhưng test mong đợi '{expected}'."
    )
