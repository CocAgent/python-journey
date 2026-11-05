"""Reference 02 — đọc nested data và không đánh tráo thiếu/sai kiểu."""


def summarize_learner(learner: dict[str, object]) -> str:
    """Định dạng learner report khi dữ liệu theo đúng schema bài học."""
    name = learner.get("name")
    scores = learner.get("scores")
    if not isinstance(name, str) or not name.strip():
        return "Dữ liệu không hợp lệ"
    if not isinstance(scores, list) or not scores:
        return "Dữ liệu không hợp lệ"
    for score in scores:
        if type(score) is not int or not 0 <= score <= 10:
            return "Dữ liệu không hợp lệ"

    progress = learner.get("progress")
    week_text = "chưa rõ"
    if "progress" in learner:
        if not isinstance(progress, dict):
            return "Dữ liệu không hợp lệ"
        if "week" in progress:
            week = progress["week"]
            if type(week) is not int or not 1 <= week <= 15:
                return "Dữ liệu không hợp lệ"
            week_text = str(week)

    average = sum(scores) / len(scores)
    return f"{name.strip()}: trung bình {average:.1f}, tuần {week_text}"


if __name__ == "__main__":
    print(summarize_learner({"name": "An", "scores": [8, 9, 7]}))
