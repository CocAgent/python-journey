"""Tạo, đọc và cập nhật một dictionary nhỏ."""


def show_profile(profile: dict[str, object]) -> None:
    """In các field chính của learner profile."""
    print(f"Tên: {profile['name']}")
    print(f"Tuần hiện tại: {profile['week']}")
    print(f"Mục tiêu: {profile.get('goal', 'Chưa đặt')}")


def update_progress(profile: dict[str, object], completed: int) -> None:
    """Cập nhật số bài đã hoàn thành trong profile."""
    profile["completed"] = completed


def main() -> None:
    """Minh họa vòng đời cơ bản của một dict."""
    learner = {
        "name": "An",
        "week": 8,
        "completed": 2,
    }

    show_profile(learner)
    update_progress(learner, 3)
    learner["goal"] = "Hiểu nested data"

    print(f"Đã hoàn thành: {learner['completed']}")
    print(f"Các key: {list(learner.keys())}")


if __name__ == "__main__":
    main()
