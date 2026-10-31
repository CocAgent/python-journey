"""Lab 3 — đọc HTTP response giả lập, KHÔNG gọi mạng.

Dùng bot_course.http_foundation.parse_json_response và
practice.study_core.status_for_score.
"""


def read_score_response(status: int, body: bytes) -> dict[str, object]:
    """TODO: status + JSON object + score -> dict hoặc ValueError."""
    return {"todo": "Lab 3 chưa xử lý HTTP response"}


def main() -> None:
    print(read_score_response(200, b'{"score": 8}'))


if __name__ == "__main__":
    main()
