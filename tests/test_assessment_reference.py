"""Regression test cho nguyên tắc chấm an toàn từ bộ đề Drive lưu trữ.

Không đọc Drive, không lấy đáp án gốc, không chạy bài nộp của sinh viên.
"""

from decimal import Decimal

import pytest

from assessment_reference import (
    RunResult,
    illustrative_exam_score,
    output_matches,
    question_score,
    run_trusted_example,
)


@pytest.mark.parametrize(
    ("stdout", "expected", "matches"),
    [
        ("1\n", ("1",), True),
        ("100\n", ("1",), False),
        ("1\n", ("100",), False),
        ("Diem: 10\n", ("Diem: 1",), False),
        ("Kết quả: đúng\n", ("Kết quả: đúng",), True),
        ("Kết quả: ĐÚNG\n", ("Kết quả: đúng",), False),
        ("dòng 1\ndòng 2\n", ("dòng 1",), False),
        ("a\nb\n", ("a", "b"), True),
        ("dòng đầu  \n", ("dòng đầu",), True),
    ],
)
def test_output_requires_exact_lines(stdout, expected, matches):
    """Sai một ký tự có nghĩa không được PASS chỉ vì chứa chuỗi con."""
    assert output_matches(RunResult(0, stdout, ""), expected) is matches


def test_nonzero_exit_does_not_count_as_pass() -> None:
    """In ra đáp án rồi gặp exception vẫn là chạy sai."""
    result = RunResult(1, "Kết quả: đúng\n", "Traceback ...")
    assert not output_matches(result, ("Kết quả: đúng",))


def test_timeout_never_counts_as_pass() -> None:
    result = RunResult(None, "Kết quả: đúng\n", "", timed_out=True)
    assert not output_matches(result, ("Kết quả: đúng",))


def test_expected_output_must_not_be_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        output_matches(RunResult(0, "", ""), ())


def test_question_score_examples() -> None:
    assert question_score((True, True)) == Decimal("2.00")
    assert question_score((True, False)) == Decimal("1.00")
    assert question_score((False, False)) == Decimal("0.00")
    assert question_score((True, False, False)) == Decimal("0.67")


@pytest.mark.parametrize("cases", [(), (1,), (True, "False")])
def test_question_score_rejects_missing_or_non_boolean_cases(cases) -> None:
    with pytest.raises((ValueError, TypeError)):
        question_score(cases)


def test_five_questions_total_exactly_ten() -> None:
    assert illustrative_exam_score(((True,),) * 5) == Decimal("10.00")
    assert illustrative_exam_score(((False,),) * 5) == Decimal("0.00")
    assert illustrative_exam_score(((True, False),) * 5) == Decimal("5.00")


def test_exam_score_rejects_wrong_question_count() -> None:
    with pytest.raises(ValueError, match="five"):
        illustrative_exam_score(((True,),) * 6)


def test_trusted_cli_receives_stdin_and_returns_stdout(tmp_path) -> None:
    """Ví dụ do test tự tạo; không lấy code sinh viên hoặc mã từ Drive."""
    script = tmp_path / "trusted_example.py"
    script.write_text(
        "value = input()\nprint('Kết quả: ' + value)\n", encoding="utf-8"
    )
    result = run_trusted_example(script, stdin="xin chào\n")
    assert result.returncode == 0
    assert output_matches(result, ("Kết quả: xin chào",))
    assert result.stderr == ""


def test_crashed_cli_cannot_pass_even_when_stdout_matches(tmp_path) -> None:
    script = tmp_path / "trusted_error.py"
    script.write_text(
        "print('OK')\nraise RuntimeError('lỗi có chủ đích')\n",
        encoding="utf-8",
    )
    result = run_trusted_example(script)
    assert result.returncode != 0
    assert "RuntimeError" in result.stderr
    assert not output_matches(result, ("OK",))


def test_trusted_cli_timeout_is_recorded(tmp_path) -> None:
    script = tmp_path / "trusted_loop.py"
    script.write_text("while True:\n    pass\n", encoding="utf-8")
    result = run_trusted_example(script, timeout_seconds=0.2)
    assert result.timed_out
    assert result.returncode is None


def test_runner_rejects_invalid_timeout_and_missing_file(tmp_path) -> None:
    script = tmp_path / "missing.py"
    with pytest.raises(ValueError):
        run_trusted_example(script, timeout_seconds=0)
    with pytest.raises(FileNotFoundError):
        run_trusted_example(script)
