"""Kiểm tra đầu vào biên của solutions; không kiểm thử student exercises."""

import pytest

from solutions.ex01_hello_sol import favourite_lines, greeting, rectangle
from solutions.ex02_calculator_sol import (
    celsius_to_fahrenheit,
    circle_area,
    remaining_balance,
    share_candy,
)
from solutions.ex03_input_sol import birth_year, mad_lib, total_of


def test_hello_and_empty_favourites():
    assert greeting("An") == "Hello, An!"
    assert favourite_lines([]) == []
    assert favourite_lines(["phở", "Python"]) == [
        "Tôi thích phở",
        "Tôi thích Python",
    ]


@pytest.mark.parametrize(
    ("width", "height", "expected"),
    [
        (2, 2, ["**", "**"]),
        (5, 4, ["*****", "*   *", "*   *", "*****"]),
        (2, 4, ["**", "**", "**", "**"]),
    ],
)
def test_rectangle_valid(width, height, expected):
    assert rectangle(width, height) == expected


@pytest.mark.parametrize(("width", "height"), [(1, 4), (0, 0), (4, 1)])
def test_rectangle_invalid(width, height):
    with pytest.raises(ValueError):
        rectangle(width, height)


def test_arithmetic_normal_and_boundary():
    assert remaining_balance(150_000, 35_000, 3) == 45_000
    assert circle_area(7) == pytest.approx(153.93791)
    assert circle_area(0) == 0
    assert share_candy(100, 7) == (14, 2)
    assert share_candy(12, 3) == (4, 0)
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)


def test_invalid_radius_and_zero_people():
    with pytest.raises(ValueError):
        circle_area(-1)
    with pytest.raises(ValueError):
        share_candy(10, 0)


def test_input_reference_is_optional_preview():
    # Năm 2026 là dữ liệu ví dụ, không khẳng định năm thực tế.
    assert birth_year(2026, 18) == 2008
    assert total_of(2, 3) == 5
    assert mad_lib("An", "vui", "mèo", "3")[0] == (
        "An có một con mèo rất vui."
    )
    with pytest.raises(ValueError):
        birth_year(2026, -1)
