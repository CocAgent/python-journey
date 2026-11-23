"""Offline Week02 student experience, with trusted fixtures only."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "weeks/week-02-variables-types/assessment/core-exercises"
sys.path.insert(0, str(CORE))

from autograde_w02 import (  # noqa: E402
    check_one,
    contains_all_numbers,
    grade,
    split_todos,
)
from student_journey import HINTS, main, render_report  # noqa: E402

REFERENCE = CORE / "fixtures" / "reference"


def test_reference_remains_full_score_with_more_cases() -> None:
    data = grade(REFERENCE, "reference")
    assert data["auto_score"] == 10
    assert data["official_score"] is None
    for task in data["tasks"]:
        for criterion in task["criteria"]:
            if criterion["id"] in {
                "W02.EX02.BMI",
                "W02.EX03.FOUR",
                "W02.EX03.CIRCLE",
                "W02.EX03.DISCOUNT",
            }:
                assert len(criterion["observations"]) == 6


def test_ordered_numbers_do_not_accept_rearranged_answers() -> None:
    assert contains_all_numbers("Tổng 10 Hiệu 6 Tích 16 Thương 4", [10, 6, 16, 4])
    assert not contains_all_numbers("Tích 16 Tổng 10 Hiệu 6 Thương 4", [10, 6, 16, 4])
    assert not contains_all_numbers("Tổng 100 Hiệu 6 Tích 16 Thương 4", [10, 6, 16, 4])


def test_fake_constant_discount_is_not_credited() -> None:
    code = (
        "gia = float(input())\n"
        "giam = float(input())\n"
        "print('400000 175000 75000 90000')\n"
    )
    earned, reason, _ = check_one("W02.EX03.DISCOUNT", code)
    assert earned == 0
    assert "REVIEW" in reason or "Thiếu" in reason


def test_alternative_output_labels_of_four_math_operations() -> None:
    source = (REFERENCE / "ex03_input_calc.py").read_text(encoding="utf-8")
    code = split_todos(source)[1].replace(
        'print("Tổng:", so_a + so_b)', 'print("A+B =", so_a + so_b)'
    ).replace(
        'print("Hiệu:", so_a - so_b)', 'print("A-B =", so_a - so_b)'
    )
    fraction, _, _ = check_one("W02.EX03.FOUR", code)
    assert fraction == 1


def test_badly_ordered_computation_output_needs_retry() -> None:
    code = (
        "a = float(input())\nb = float(input())\n"
        "print(a*b)\nprint(a+b)\nprint(a-b)\nprint(a/b)\n"
    )
    fraction, _, _ = check_one("W02.EX03.FOUR", code)
    assert fraction == 0


def test_all_mandatory_todos_have_three_hints() -> None:
    data = grade(REFERENCE, "reference")
    ids = {c["id"] for task in data["tasks"] for c in task["criteria"]}
    assert set(HINTS) == ids
    assert all(len(hints) == 3 for hints in HINTS.values())


def test_offline_html_reference_cli(tmp_path: Path) -> None:
    html_path = tmp_path / "report.html"
    json_path = tmp_path / "result.json"
    assert main([
        "--reference", "--report", str(html_path),
        "--json-out", str(json_path),
    ]) == 0
    output = html_path.read_text(encoding="utf-8")
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert "MẪU GIẢNG VIÊN" in output
    assert "Chiếc ba lô biến" in output
    assert "Phép thuật chuyển kiểu" in output
    assert "Xưởng máy tính mini" in output
    assert output.count('class="stage"') == 3
    assert "10.00/10" in output
    assert "<script" not in output
    assert 'src="http' not in output
    assert data["official_score"] is None
    assert '"An"' not in json.dumps(data, ensure_ascii=False)
    assert not any(
        "stdout" in item or "vars" in item
        for task in data["tasks"]
        for check in task["criteria"]
        for item in check["observations"]
    )


def test_html_hints_reveal_only_for_retry(tmp_path: Path) -> None:
    data = grade(tmp_path, "student")
    output = render_report(data)
    assert output.count('class="hint"') == 30
    assert output.count("Gợi ý mức 3") == 10
    assert "0.00/10" in output
    assert "official_score: null" in output
    assert "KẾT QUẢ TỰ LUYỆN" in output


def test_html_escapes_errors_and_never_embeds_code() -> None:
    data = grade(REFERENCE, "reference")
    data["tasks"][0]["criteria"][0]["reason"] = '<script>alert("x")</script>'
    output = render_report(data)
    assert '<script>alert("x")</script>' not in output
    assert "&lt;script&gt;" in output
    assert "ten = \"An\"" not in output


def test_student_report_from_blank_exercises_is_not_fake_success(
    tmp_path: Path,
) -> None:
    # grade() on an empty temporary folder is a valid zero baseline.
    data = grade(tmp_path, "student")
    assert data["auto_score"] == 0
    assert all(
        not item["passed"] for task in data["tasks"]
        for item in task["criteria"]
    )



def test_student_cli_with_blank_exercises_creates_report(
    tmp_path: Path, monkeypatch,
) -> None:
    import student_journey  # noqa: PLC0415

    fake_week = tmp_path / "week-02"
    exercises = fake_week / "exercises"
    exercises.mkdir(parents=True)
    for filename, count in (
        ("ex01_variables.py", 4),
        ("ex02_type_conversion.py", 5),
        ("ex03_input_calc.py", 4),
    ):
        (exercises / filename).write_text(
            "\n".join(f"# TODO {n}: chưa làm" for n in range(1, count + 1))
            + "\n",
            encoding="utf-8",
        )
    monkeypatch.setattr(student_journey, "WEEK", fake_week)
    target = tmp_path / "student.html"
    assert student_journey.main(["--student", "--report", str(target)]) == 1
    page = target.read_text(encoding="utf-8")
    assert "KẾT QUẢ TỰ LUYỆN TRÊN MÁY CÁ NHÂN" in page
    assert "0.00/10" in page
    assert page.count('class="stage"') == 3
