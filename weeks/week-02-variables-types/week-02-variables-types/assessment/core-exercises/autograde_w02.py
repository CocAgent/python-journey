"""Week 02 formative grading for ORIGINAL exercises only, not a mock exam.

Only use locally with your own/trusted code. Timeout/process isolation is NOT
a security sandbox and must not be used for untrusted submissions in CI/VPS.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WEEK = ROOT.parents[1]
RUBRIC = ROOT / "rubric.json"
RUNNER = ROOT / "runner_w02.py"
TODO = re.compile(r"^\s*#\s*TODO\s+([0-9]+)\b")
NUMBER = re.compile(r"(?<![\d.])[-+]?\d+(?:\.\d+)?(?![\d.])")
BOOLEAN = re.compile(r"\b(?:True|False)\b")
WATCHED = ("ten", "tuoi", "diem_tb", "dang_hoc", "a", "b", "x")


def split_todos(source: str) -> dict[int, str]:
    """Use the TODO boundaries of the unchanged exercise files."""
    index = None
    sections: dict[int, list[str]] = {}
    for line in source.splitlines():
        marker = TODO.match(line)
        if marker:
            index = int(marker.group(1))
            sections[index] = []
        elif index is not None:
            sections[index].append(line)
    return {index: "\n".join(lines) + "\n" for index, lines in sections.items()}


def run_fragment(code: str, user_input: str) -> dict:
    """Run exactly ONE TODO with fresh stdin; ignore optional TODOs completely."""
    env = {
        key: val for key, val in os.environ.items()
        if key in {"PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "LANG", "LC_ALL"}
    }
    env["PYTHONNOUSERSITE"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        with tempfile.TemporaryDirectory(prefix="w02-core-") as workdir:
            script = Path(workdir) / "learner_todo.py"
            script.write_text(code, encoding="utf-8")
            process = subprocess.run(
                [sys.executable, "-I", "-B", "-X", "utf8", str(RUNNER), str(script), user_input],
                stdin=subprocess.DEVNULL, cwd=workdir, env=env,
                capture_output=True, text=True, encoding="utf-8",
                errors="replace", timeout=4, check=False,
            )
        if process.returncode != 0:
            return {"ok": False, "error": "PROCESS_ERROR", "message": process.stderr[-180:]}
        return json.loads(process.stdout.strip())
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "TIMEOUT", "message": "Quá 4 giây"}
    except (OSError, ValueError) as error:
        return {"ok": False, "error": "RUN_ERROR", "message": str(error)[:120]}


def call_nodes(tree: ast.AST, name: str) -> list[ast.Call]:
    return [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == name
    ]


def has_call_on(tree: ast.AST, fn: str, name: str) -> bool:
    return any(
        node.args and isinstance(node.args[0], ast.Name)
        and node.args[0].id == name
        for node in call_nodes(tree, fn)
    )


def has_operator(tree: ast.AST, kind: type) -> bool:
    return any(
        isinstance(node, ast.BinOp) and isinstance(node.op, kind)
        for node in ast.walk(tree)
    )


def assignment(tree: ast.AST, name: str, number: int | float) -> bool:
    return any(
        isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
        and isinstance(node.value, ast.Constant)
        and type(node.value.value) in (int, float)
        and node.value.value == number
        for node in ast.walk(tree)
    )


def output_numbers(text: str) -> list[float]:
    return [float(part) for part in NUMBER.findall(text)]


def contains_all_numbers(text: str, expected: list[float], tol: float = 0.016) -> bool:
    """Find numeric outputs in expected order without matching substrings.

    Other numeric labels may appear before/between answers. This remains a
    formative heuristic; instructors handle valid alternate output formats.
    """
    available = output_numbers(text)
    cursor = 0
    for wanted in expected:
        while cursor < len(available) and not math.isclose(
            available[cursor], wanted, abs_tol=tol, rel_tol=0
        ):
            cursor += 1
        if cursor == len(available):
            return False
        cursor += 1
    return True


def printed(tree: ast.AST, name: str) -> int:
    return sum(
        int(any(isinstance(node, ast.Name) and node.id == name
                for node in ast.walk(p)))
        for p in call_nodes(tree, "print")
    )


def swap_ast(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        left = node.targets[0]
        right = node.value
        if not isinstance(left, (ast.List, ast.Tuple)) or not isinstance(right, (ast.List, ast.Tuple)):
            continue
        if len(left.elts) != 2 or len(right.elts) != 2:
            continue
        if all(isinstance(n, ast.Name) for n in (*left.elts, *right.elts)):
            if [n.id for n in left.elts] == ["a", "b"] and [n.id for n in right.elts] == ["b", "a"]:
                return True
    return False


def bool_args(tree: ast.AST) -> set[str]:
    result = set()
    for node in call_nodes(tree, "bool"):
        if node.args:
            try:
                value = ast.literal_eval(node.args[0])
                result.add(type(value).__name__ + ":" + repr(value))
            except (ValueError, TypeError, SyntaxError):
                pass
    return result


TEST_CASE_FILES = {
    "ex01_variables.py": "cases_ex01_variables.json",
    "ex02_type_conversion.py": "cases_ex02_type_conversion.json",
    "ex03_input_calc.py": "cases_ex03_input_calc.json",
}
TEST_CASE_DIR = ROOT / "tests"
INPUT_CRITERIA = {
    "W02.EX02.BMI", "W02.EX03.FOUR",
    "W02.EX03.CIRCLE", "W02.EX03.DISCOUNT",
}


def load_test_cases() -> dict[str, list[tuple[str, list[float]]]]:
    """Read the independent exercise test bank, fail closed on mismatched rubric.

    This is a PUBLIC formative case bank, not protected exam tests.
    The tests do not import learner code; only the trusted local grader runs it.
    """
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    by_file = {
        task["file"]: {item["id"] for item in task["criteria"]}
        for task in rubric["tasks"]
    }
    if set(by_file) != set(TEST_CASE_FILES):
        raise ValueError("TEST_SUITE_MISMATCH: unexpected exercises in rubric")
    collected: dict[str, list[tuple[str, list[float]]]] = {}
    for exercise, filename in TEST_CASE_FILES.items():
        document = json.loads((TEST_CASE_DIR / filename).read_text(encoding="utf-8"))
        if (
            document.get("schema_version") != "1.0"
            or document.get("exercise") != exercise
            or set(document.get("cases", {})) != by_file[exercise]
        ):
            raise ValueError(f"TEST_SUITE_MISMATCH: {filename} criteria/rubric")
        for cid, scenarios in document["cases"].items():
            if not isinstance(scenarios, list):
                raise ValueError(f"TEST_SUITE_INVALID: {cid} must be a list")
            if cid in INPUT_CRITERIA and len(scenarios) < 4:
                raise ValueError(f"TEST_SUITE_INCOMPLETE: {cid}")
            if cid not in INPUT_CRITERIA and scenarios:
                raise ValueError(f"TEST_SUITE_INVALID: {cid} has unexpected stdin tests")
            if not scenarios:
                continue
            normalized = []
            for scenario in scenarios:
                if (
                    not isinstance(scenario, dict)
                    or set(scenario) != {"input", "expected"}
                    or not isinstance(scenario["input"], str)
                    or not isinstance(scenario["expected"], list)
                    or not scenario["expected"]
                    or any(type(n) not in (int, float) for n in scenario["expected"])
                ):
                    raise ValueError(f"TEST_SUITE_INVALID: bad scenario for {cid}")
                normalized.append((scenario["input"], scenario["expected"]))
            collected[cid] = normalized
    return collected


def test_suite_audit() -> dict:
    """Enumerate EVERY rubric criterion and every case file, without executing code."""
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    loaded = load_test_cases()
    tasks = []
    for task in rubric["tasks"]:
        tasks.append({
            "exercise": task["file"],
            "criteria": [
                {
                    "id": item["id"],
                    "todo": item["source_todo"],
                    "points": item["points"],
                    "input_cases": len(loaded.get(item["id"], [])),
                }
                for item in task["criteria"]
            ],
        })
    digest = hashlib.sha256()
    for name in TEST_CASE_FILES.values():
        digest.update((TEST_CASE_DIR / name).read_bytes())
    return {
        "week": "W02",
        "criteria_count": sum(len(item["criteria"]) for item in tasks),
        "exercises_count": len(tasks),
        "dynamic_case_count": sum(map(len, loaded.values())),
        "rubric_points": sum(
            item["points"] for task in tasks for item in task["criteria"]
        ),
        "test_suite_sha256": digest.hexdigest(),
        "tasks": tasks,
        "official_score": None,
    }


def check_one(cid: str, code: str) -> tuple[float, str, list[dict]]:
    """A fraction from 0..1; each result is formative, never official."""
    if not code.strip() or not any(
        line.strip() and not line.lstrip().startswith("#") for line in code.splitlines()
    ):
        return 0.0, "TODO chưa làm.", []
    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        return 0.0, f"SyntaxError trong TODO: dòng {error.lineno}.", []

    samples = load_test_cases()
    observations = []
    for input_text, _ in samples.get(cid, [("", [])]):
        observations.append(run_fragment(code, input_text))
    first = observations[0]
    if not first.get("ok"):
        return 0.0, f"{first.get('error')}: {first.get('message', '')}", observations
    stdout = str(first.get("stdout", ""))
    variables = first.get("vars", {})

    if cid == "W02.EX01.PROFILE":
        types = {"ten": "str", "tuoi": "int", "diem_tb": "float", "dang_hoc": "bool"}
        good_vars = all(variables.get(name, {}).get("type") == typ for name, typ in types.items())
        good_calls = all(has_call_on(tree, "type", name) for name in types)
        good_output = (
            all(str(variables[name]["value"]) in stdout for name in types if name in variables)
            and all(typ in stdout for typ in types.values())
            and bool(stdout.strip())
        )
        valid = good_vars and good_calls and good_output
        reason = "Cần bốn biến ten/tuoi/diem_tb/dang_hoc đúng kiểu và in giá trị, type()."
    elif cid == "W02.EX01.SWAP":
        valid = (
            assignment(tree, "a", 10) and assignment(tree, "b", 20)
            and swap_ast(tree)
            and variables.get("a", {}).get("value") == 20
            and variables.get("b", {}).get("value") == 10
        )
        reason = "Cần khởi tạo a=10, b=20 rồi hoán đổi a,b=b,a không dùng biến tạm."
    elif cid == "W02.EX01.AUG":
        operations = [
            type(node.op) for node in ast.walk(tree)
            if isinstance(node, ast.AugAssign)
            and isinstance(node.target, ast.Name) and node.target.id == "x"
        ]
        valid = (
            assignment(tree, "x", 100)
            and all(operation in operations for operation in (ast.Add, ast.Sub, ast.Mult, ast.FloorDiv))
            and printed(tree, "x") >= 4
            and variables.get("x", {}).get("type") in ("int", "float")
        )
        reason = "Cần x=100; dùng +=, -=, *=, //= và in x sau từng bước. Giá trị tăng/giảm tự chọn."
    elif cid == "W02.EX02.TEXT":
        valid = (
            "50" in [str(int(n)) for n in output_numbers(stdout) if n.is_integer()]
            and has_call_on(tree, "int", "so_text")
            and has_operator(tree, ast.Add)
        )
        reason = "Chuyển so_text='42' bằng int(), cộng 8 rồi in 50."
    elif cid == "W02.EX02.PI":
        valid = (
            contains_all_numbers(stdout, [3])
            and assignment(tree, "pi", 3.14159)
            and has_call_on(tree, "int", "pi")
        )
        reason = "Dùng int(pi) với pi=3.14159 và in 3 (cắt, không làm tròn)."
    elif cid == "W02.EX02.BOOL":
        required = {
            "int:0", "int:1", "str:''", "str:'hello'",
            "list:[]", "list:[1, 2]",
        }
        valid = (
            required.issubset(bool_args(tree))
            and BOOLEAN.findall(stdout) == ["False", "True", "False", "True", "False", "True"]
        )
        reason = "In sáu bool() theo thứ tự đề: 0,1,'','hello',[],[1,2]."
    elif cid in samples:
        structural = True
        if cid == "W02.EX02.BMI":
            structural = len(call_nodes(tree, "input")) >= 2 and has_operator(tree, ast.Div)
        elif cid == "W02.EX03.FOUR":
            structural = (
                len(call_nodes(tree, "input")) >= 2
                and all(has_operator(tree, kind) for kind in (ast.Add, ast.Sub, ast.Mult, ast.Div))
            )
        elif cid == "W02.EX03.CIRCLE":
            structural = (
                len(call_nodes(tree, "input")) >= 1
                and has_operator(tree, ast.Mult)
            )
        elif cid == "W02.EX03.DISCOUNT":
            structural = (
                len(call_nodes(tree, "input")) >= 2
                and has_operator(tree, ast.Mult)
                and has_operator(tree, ast.Sub)
            )
        good = 0
        for response, (_stdin, expected) in zip(observations, samples[cid]):
            if response.get("ok") and contains_all_numbers(
                str(response.get("stdout", "")), expected
            ):
                good += 1
        if not structural:
            if good:
                return (
                    0.0,
                    "REVIEW: Có kết quả trùng mẫu nhưng chưa nhận diện được "
                    "phép toán/input theo yêu cầu; nhờ giảng viên xem mã.",
                    observations,
                )
            return 0.0, "Thiếu input() hoặc phép toán của TODO gốc.", observations
        return (
            good / len(samples[cid]),
            f"Đạt {good}/{len(samples[cid])} bộ input kiểm thử đa dạng.",
            observations,
        )
    else:
        return 0.0, f"Chưa có tiêu chí chấm cho {cid}", observations
    return float(valid), "Đạt tiêu chí." if valid else reason, observations


def grade(source_folder: Path, mode: str) -> dict:
    rubric_bytes = RUBRIC.read_bytes()
    rubric = json.loads(rubric_bytes)
    tasks = []
    score = 0.0
    for task in rubric["tasks"]:
        file_path = source_folder / task["file"]
        source = file_path.read_text(encoding="utf-8") if file_path.is_file() and not file_path.is_symlink() else ""
        bodies = split_todos(source)
        results = []
        for criterion in task["criteria"]:
            fraction, reason, observations = check_one(
                criterion["id"], bodies.get(criterion["source_todo"], "")
            )
            earned = round(criterion["points"] * fraction, 3)
            score += earned
            results.append({
                "id": criterion["id"], "todo": criterion["source_todo"],
                "passed": fraction == 1.0, "earned": earned,
                "maximum": criterion["points"], "reason": reason,
                "observations": [
                    {"ok": bool(item.get("ok")), "error": item.get("error")}
                    for item in observations
                ],
            })
        tasks.append({
            "file": task["file"], "title": task["title"],
            "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest()
            if source else None,
            "criteria": results,
        })
    return {
        "schema_version": rubric["schema_version"],
        "week": "W02",
        "mode": mode,
        "assessment_type": "formative_original_exercises",
        "rubric_sha256": hashlib.sha256(rubric_bytes).hexdigest(),
        "test_suite_sha256": test_suite_audit()["test_suite_sha256"],
        "auto_score": round(score, 2),
        "auto_max_points": rubric["auto_max_points"],
        "official_score": None,
        "optional_excluded": rubric["optional_not_scored"],
        "tasks": tasks,
        "warning": "Chỉ đánh giá TODO bắt buộc của 3 exercises. Không phải điểm chính thức hay sandbox.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week 02 — chấm chính ba file exercises/")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--student", action="store_true", help="Chấm mã exercise của sinh viên")
    mode.add_argument("--reference", action="store_true", help="Kiểm fixture giáo viên, không phải bài sinh viên")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args(argv)
    source_folder = ROOT / "fixtures" / "reference" if args.reference else WEEK / "exercises"
    try:
        result = grade(source_folder, "reference" if args.reference else "student")
    except (OSError, ValueError) as exc:
        print(f"Lỗi bộ chấm: {exc}", file=sys.stderr)
        return 2
    for task in result["tasks"]:
        for check in task["criteria"]:
            status = (
                "PASS" if check["passed"] else
                "REVIEW" if check["reason"].startswith("REVIEW:") else "RETRY"
            )
            print(
                f"{status} {check['id']}: "
                f"{check['earned']:.2f}/{check['maximum']:.2f} — {check['reason']}"
            )
            if args.verbose and check["observations"]:
                print(f"    Chi tiết thực thi: {check['observations']!r}"[:700])
    print(
        f"{result['mode'].upper()}: {result['auto_score']:.2f}/10.00 "
        "(chỉ 3 file exercises/, không gồm thử thách)."
    )
    print("ĐIỂM TỰ LUYỆN — KHÔNG PHẢI ĐIỂM CHÍNH THỨC.")
    if args.json_out:
        try:
            target = args.json_out.resolve()
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except OSError as exc:
            print(f"Không ghi được JSON: {exc}", file=sys.stderr)
            return 2
    return 0 if result["auto_score"] == result["auto_max_points"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
