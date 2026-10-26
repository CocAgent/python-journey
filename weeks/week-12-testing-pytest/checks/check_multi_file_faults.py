"""Thử nhiều lỗi cố ý trong các tệp pricing, storage và service.

Mỗi lỗi chỉ được đưa vào bản sao ở thư mục tạm, không sửa tệp thật.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

WEEK_ROOT = Path(__file__).resolve().parents[1]
SOURCE = WEEK_ROOT / "examples" / "multi_file_lab"
TESTS = WEEK_ROOT / "examples" / "test_multi_file_lab.py"

# Mỗi phép biến đổi nằm ở một vị trí cụ thể trong tệp đích.
FAULTS = (
    ("pricing.py", "Tính nhầm phép cộng thay cho phép nhân",
     "return quantity * unit_price", "return quantity + unit_price"),
    ("pricing.py", "Chấp nhận sai số lượng -1",
     "if quantity < 0 or unit_price < 0:", "if quantity < -1 or unit_price < 0:"),
    ("storage.py", "Đọc tệp nhưng trả về dữ liệu rỗng",
     "return json.loads(content)", "return {}"),
    ("storage.py", "Không chuyển lỗi JSON thành thông báo có ích",
     "except json.JSONDecodeError as exc:", "except TypeError as exc:"),
    ("service.py", "Tính sai tổng do làm mất đơn giá",
     "total = calculate_total(quantity, unit_price)",
     "total = calculate_total(quantity, 0)"),
    ("service.py", "Tạo đơn hàng nhưng quên lưu tệp",
     "save_order(path, order)", "# save_order(path, order)"),
)


def run_case(
    fault: tuple[str, str, str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Chạy test trong bản sao riêng, trả lại kết quả thực tế của pytest."""
    with TemporaryDirectory(prefix="python-journey-multifile-") as directory:
        sandbox = Path(directory)
        target = sandbox / "multi_file_lab"
        shutil.copytree(SOURCE, target)
        shutil.copy2(TESTS, sandbox / "test_multi_file_lab.py")

        if fault is not None:
            filename, _, original, replacement = fault
            path = target / filename
            content = path.read_text(encoding="utf-8")
            if content.count(original) != 1:
                raise ValueError(f"Không thể tạo lỗi: {filename} / {original}")
            path.write_text(
                content.replace(original, replacement, 1), encoding="utf-8"
            )

        return subprocess.run(
            [sys.executable, "-m", "pytest", "test_multi_file_lab.py", "-q",
             "-p", "no:cacheprovider"],
            cwd=sandbox,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )


def main() -> int:
    """Chỉ PASS nếu bộ test đúng và phát hiện cả sáu lỗi cố ý."""
    try:
        baseline = run_case()
        if baseline.returncode != 0:
            print("FAIL: bộ kiểm thử gốc chưa đạt. Chưa được thử lỗi cố ý.")
            print((baseline.stdout + baseline.stderr)[-2000:])
            return 1
        print("PASS: chương trình đúng vượt qua bộ kiểm thử tham chiếu.")

        missed = []
        for fault in FAULTS:
            filename, label, _, _ = fault
            result = run_case(fault)
            # Exit 1 kèm chỉ báo failed: test thực sự bắt được hành vi sai.
            if result.returncode == 1 and "failed" in result.stdout.lower():
                print(f"PHÁT HIỆN: {filename} — {label}")
            else:
                missed.append(f"{filename}: {label} (exit={result.returncode})")

        if missed:
            for error in missed:
                print(f"CHƯA PHÁT HIỆN: {error}")
            return 1

        print(f"PASS: phát hiện {len(FAULTS)}/{len(FAULTS)} lỗi trong 3 tệp.")
        print("Đây là phép thử minh họa; không phải bằng chứng hết mọi lỗi.")
        return 0
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        print(f"KHÔNG CHẠY ĐƯỢC PHÉP THỬ: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
