"""Kịch bản chạy thử demo Bot chiến lược nhiều module.

Chạy trực tiếp từ terminal:
python weeks/week-14-oop-essentials/mini-project/main.py
"""

import sys
from pathlib import Path

# Đảm bảo có thể import các module cùng thư mục khi chạy file trực tiếp
sys.path.insert(0, str(Path(__file__).parent))

from bot import Bot
from strategies import balanced, defensive


def main() -> None:
    print("=== DEMO BOT CHIẾN LƯỢC (TUẦN 14 - OOP COMPOSITION) ===\n")

    # Tình huống 1: Bot phòng thủ khi đối thủ ở sát bên
    state_threat = {"position": 3, "goal": 0, "opponent_position": 4}
    bot = Bot(defensive)
    action_1 = bot.choose_action(state_threat)
    print(f"1. Trạng thái có nguy cơ: {state_threat}")
    print(f"   Hành động với chiến lược defensive: '{action_1}' (chờ an toàn)")

    # Tình huống 2: Đổi chiến lược sang balanced trên CÙNG một đối tượng bot
    bot.strategy = balanced
    action_2 = bot.choose_action(state_threat)
    print(f"\n2. Đổi strategy sang balanced (không sửa class Bot):")
    print(f"   Hành động với chiến lược balanced: '{action_2}' (tiến về đích 0)")

    # Tình huống 3: Bot di chuyển về đích cả hai chiều
    state_left = {"position": 5, "goal": 2}
    state_right = {"position": 1, "goal": 4}
    state_arrived = {"position": 3, "goal": 3}
    print(f"\n3. Kiểm tra định hướng:")
    print(f"   Vị trí 5 -> đích 2: '{bot.choose_action(state_left)}'")
    print(f"   Vị trí 1 -> đích 4: '{bot.choose_action(state_right)}'")
    print(f"   Vị trí 3 -> đích 3: '{bot.choose_action(state_arrived)}'")


if __name__ == "__main__":
    main()
