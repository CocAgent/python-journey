"""Chạy thử nghiệm Bot với các kịch bản chiến lược khác nhau."""

from bot import Bot
from strategies import balanced, defensive


def main() -> None:
    print("=== DEMO MINI-PROJECT BOT VỚI COMPOSITION ===")

    # 1. Khởi tạo Bot với chiến lược phòng thủ
    bot = Bot(defensive)
    state_threat = {"position": 3, "goal": 0, "opponent_position": 4}
    action = bot.choose_action(state_threat)
    print(f"Trạng thái có đối thủ sát cạnh: {state_threat}")
    print(f"Hành động phòng thủ (defensive): {action} (đứng yên chờ)")

    # 2. Hoán đổi chiến lược sang cân bằng trong runtime mà không sửa đổi lớp Bot
    bot.strategy = balanced
    action_swap = bot.choose_action(state_threat)
    print(f"Sau khi đổi strategy sang balanced: {action_swap} (tiến về đích bất chấp đối thủ)")

    # 3. Thử nghiệm di chuyển 2 chiều
    print("\nKiểm tra di chuyển 2 chiều:")
    print("Pos 1 -> Goal 5:", bot.choose_action({"position": 1, "goal": 5}))
    print("Pos 5 -> Goal 1:", bot.choose_action({"position": 5, "goal": 1}))
    print("Pos 3 -> Goal 3 (đã tới):", bot.choose_action({"position": 3, "goal": 3}))


if __name__ == "__main__":
    main()

