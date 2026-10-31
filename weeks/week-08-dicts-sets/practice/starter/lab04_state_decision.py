"""Lab 04 — Dict state -> guarded heuristic, COURSE-LOCAL ONLY.

NOT VUACOC PRODUCTION CONTRACT.
state yêu cầu position và goal là int trong [0..4]; opponent_position
là optional int [0..4]. Data sai -> validate False, action "wait",
mô tả "State không hợp lệ" (không nhận đó là quyết định bình thường).
"""


ACTIONS = {"left", "right", "wait"}


def validate_state(state: dict[str, object]) -> bool:
    """Kiểm keys bắt buộc, kiểu int (không bool), giới hạn 0..4."""
    # TODO: position và goal phải tồn tại; đúng type và range.
    # TODO: opponent_position nếu có phải là int 0..4; nếu vắng mặt thì OK.
    raise NotImplementedError("Hoàn thành validate_state")


def choose_action(state: dict[str, object]) -> str:
    """Trả action thuộc ACTIONS, không sửa state; invalid -> wait."""
    # TODO: gọi validate_state trước; invalid hoặc đã tại goal -> wait.
    # TODO: nếu đối thủ cách <=1 vị trí -> wait.
    # TODO: chưa đạt goal thì đi right/left phù hợp.
    raise NotImplementedError("Hoàn thành choose_action")


def explain_decision(state: dict[str, object]) -> str:
    """Trả thông báo rõ nếu invalid; otherwise giải thích position/goal/action."""
    # TODO: invalid -> "State không hợp lệ".
    # TODO: gọi choose_action(state) và trả:
    # f"position={position}, goal={goal}, action={action}"
    raise NotImplementedError("Hoàn thành explain_decision")


if __name__ == "__main__":
    print("COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT")
