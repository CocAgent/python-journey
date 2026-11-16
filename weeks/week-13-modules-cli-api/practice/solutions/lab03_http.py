"""Lab 3 solution: parse status/JSON + business validation."""

from bot_course.http_foundation import parse_json_response
from practice.study_core import status_for_score, validate_score


def read_score_response(status: int, body: bytes) -> dict[str, object]:
    data = parse_json_response(status, body)
    if "score" not in data:
        raise ValueError("Phản hồi thiếu trường score")
    score = validate_score(data["score"])
    return {"score": score, "status": status_for_score(score)}


def main() -> None:
    print(read_score_response(200, b'{"score": 8}'))


if __name__ == "__main__":
    main()
