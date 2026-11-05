"""Lab 4 solution: form adapter, explicit fail-closed validation."""

from practice.study_core import status_for_score, validate_score


def make_student_report(payload: dict[str, object]) -> dict[str, object]:
    if not isinstance(payload, dict):
        raise ValueError("Form phải là dict")

    name = payload.get("student")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("student phải là tên không rỗng")

    if "score" not in payload:
        raise ValueError("Form thiếu score")

    score = validate_score(payload["score"])
    return {"student": name.strip(), "score": score, "status": status_for_score(score)}


def main() -> None:
    print(make_student_report({"student": "  An  ", "score": 7.5}))


if __name__ == "__main__":
    main()
