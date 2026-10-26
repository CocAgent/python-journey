"""CI bảo đảm danh mục 20 dự án nguồn Word và rubric Tuần 09 không bị drift."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "weeks/week-09-midterm-project/checks/check_project_catalog.py"


def test_week09_catalog_and_rubric_are_consistent():
    """Kiểm chứng tài liệu tham khảo, không thu bài sinh viên để chấm."""
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "20 nguồn, 10 tiêu chí" in result.stdout
