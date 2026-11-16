"""Runner Tuần 01 chỉ cho lời giải mẫu; Python standard-library only."""

import subprocess
import sys
from pathlib import Path

CHECKS = Path(__file__).resolve().parent


def main() -> int:
    for filename in ("check_solutions.py", "check_examples.py"):
        process = subprocess.run(
            [sys.executable, "-B", str(CHECKS / filename)],
            cwd=CHECKS.parents[2],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
            timeout=45,
        )
        if process.returncode:
            print(f"Week 01 reference checks: FAIL — {filename}")
            print(process.stdout + process.stderr)
            return 1
        print(process.stdout.strip())
    print("Week 01 reference checks: PASS (không chấm sinh viên)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
