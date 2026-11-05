"""Mini-project Tuần 14: Demo chạy thử Bot với Composition."""

from bot import Bot
from strategies import balanced, defensive


def main() -> None:
    # 1. Khởi tạo bot với chiến lược phòng thủ
    my_bot = Bot(defensive, name="IronShield")
    print(f"Khởi tạo: {my_bot}")

    # Tình huống 1: Đối thủ đang ở sát (cách 1 ô)
    state_threat = {"position": 2, "goal": 5, "opponent_position": 3}
    action_1 = my_bot.choose_action(state_threat)
    print(f"State có đối thủ sát cạnh: {state_threat} -> Action: {action_1} (chờ)")

    # 2. Đổi chiến lược sang balanced mà không sửa code Bot
    my_bot.strategy = balanced
    action_2 = my_bot.choose_action(state_threat)
    print(f"Sau khi đổi sang balanced: Action: {action_2} (tiếp tục đi về đích)")

    # Tình huống 3: Mục tiêu bên trái
    state_left = {"position": 5, "goal": 1}
    print(f"Mục tiêu bên trái: {state_left} -> Action: {my_bot.choose_action(state_left)}")

    # Tình huống 4: Đã ở tại đích
    state_at_goal = {"position": 5, "goal": 5}
    print(f"Đã tại đích: {state_at_goal} -> Action: {my_bot.choose_action(state_at_goal)}")


if __name__ == "__main__":
    main()
