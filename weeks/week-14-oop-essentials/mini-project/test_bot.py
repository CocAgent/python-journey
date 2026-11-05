"""Bộ kiểm thử cho Mini-project Bot nhiều module.

Chạy lệnh:
python -m pytest weeks/week-14-oop-essentials/mini-project/test_bot.py -v
"""

import sys
from pathlib import Path

# Đảm bảo đường dẫn module luôn khả dụng
sys.path.insert(0, str(Path(__file__).parent))

import pytest

from bot import Bot
from strategies import aggressive, balanced, defensive


def test_defensive_waits_when_opponent_near() -> None:
    """Defensive phải đứng yên khi đối thủ cách tối đa 1 ô."""
    # Đối thủ ở bên phải cách 1 ô
    state_right = {"position": 3, "goal": 0, "opponent_position": 4}
    assert Bot(defensive).choose_action(state_right) == "wait"

    # Đối thủ ở bên trái cách 1 ô
    state_left = {"position": 3, "goal": 6, "opponent_position": 2}
    assert Bot(defensive).choose_action(state_left) == "wait"

    # Đối thủ trùng vị trí (khoảng cách 0)
    state_same = {"position": 3, "goal": 6, "opponent_position": 3}
    assert Bot(defensive).choose_action(state_same) == "wait"


def test_defensive_moves_when_opponent_far() -> None:
    """Defensive di chuyển về đích bình thường khi đối thủ ở khoảng cách an toàn (>1 ô)."""
    state_far = {"position": 2, "goal": 6, "opponent_position": 5}
    assert Bot(defensive).choose_action(state_far) == "right"


def test_balanced_moves_both_directions() -> None:
    """Balanced phải đi đúng chiều về đích cả bên trái và bên phải."""
    bot = Bot(balanced)
    # Đích bên phải
    assert bot.choose_action({"position": 1, "goal": 5}) == "right"
    # Đích bên trái
    assert bot.choose_action({"position": 5, "goal": 1}) == "left"


def test_bot_waits_at_goal() -> None:
    """Tất cả chiến lược đều đứng yên ('wait') khi đã ở đúng vị trí đích."""
    state_at_goal = {"position": 4, "goal": 4}
    for strat in [defensive, balanced, aggressive]:
        assert Bot(strat).choose_action(state_at_goal) == "wait"


def test_runtime_strategy_swap() -> None:
    """Thay đổi bot.strategy trên cùng đối tượng phải đổi hành vi mà không cần sửa class Bot."""
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    bot = Bot(defensive)
    assert bot.choose_action(state) == "wait"

    # Hoán đổi chiến lược sang balanced
    bot.strategy = balanced
    assert bot.choose_action(state) == "left"


def test_defensive_without_opponent_position() -> None:
    """Defensive vẫn hoạt động bình thường kể cả khi state không có khóa opponent_position."""
    state_no_opponent = {"position": 4, "goal": 1}
    bot = Bot(defensive)
    assert bot.choose_action(state_no_opponent) == "left"


def test_state_immutability() -> None:
    """Hàm chiến lược không được tự ý sửa đổi (mutate) nội dung từ điển state."""
    state = {"position": 2, "goal": 5, "opponent_position": 8}
    snapshot = state.copy()
    bot = Bot(defensive)
    _ = bot.choose_action(state)
    assert state == snapshot


def test_custom_strategy_injection() -> None:
    """Kiểm chứng Bot có thể nhận bất kỳ hàm Callable nào thỏa mãn giao diện."""
    history: list[int] = []

    def log_and_wait(s: dict[str, int]) -> str:
        history.append(s["position"])
        return "wait"

    custom_bot = Bot(log_and_wait)
    res = custom_bot.choose_action({"position": 9, "goal": 0})
    assert res == "wait"
    assert history == [9]
