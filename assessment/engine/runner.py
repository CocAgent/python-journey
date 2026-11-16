"""Local-only subprocess runner. A timeout is NOT a security sandbox."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RunResult:
    stdout: str
    stderr: str
    returncode: int | None
    error: str | None = None


def run_python(script: Path, *, timeout: float = 3.0) -> RunResult:
    """Run a *trusted/local* file in a temporary cwd; never use for untrusted code."""
    environment = {
        key: value
        for key, value in os.environ.items()
        if key in {"PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "LANG", "LC_ALL"}
    }
    environment["PYTHONNOUSERSITE"] = "1"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        with tempfile.TemporaryDirectory(prefix="ag01-run-") as workdir:
            process = subprocess.run(
                [sys.executable, "-B", str(script)],
                cwd=workdir,
                env=environment,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
            )
            return RunResult(
                stdout=process.stdout[:10000],
                stderr=process.stderr[:2000],
                returncode=process.returncode,
            )
    except subprocess.TimeoutExpired:
        return RunResult("", "", None, "TIMEOUT")
    except OSError:
        return RunResult("", "", None, "EXECUTION_ERROR")
