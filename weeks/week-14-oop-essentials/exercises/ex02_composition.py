# Bài 2: Composition - Bot sử dụng strategy

class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


def di_ve_dich(state):
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state):
    doi_thu = state.get("opponent_position")
    if doi_thu is not None and abs(doi_thu - state["position"]) <= 1:
        return "wait"
    return di_ve_dich(state)


def balanced(state):
    return di_ve_dich(state)


def aggressive(state):
    return di_ve_dich(state)


# Thử thay đổi chiến lược mà không sửa class Bot
trang_thai = {"position": 1, "opponent_position": 4, "goal": 4}
bot = Bot(defensive)
print("Phòng thủ:", bot.choose_action(trang_thai))

bot.strategy = balanced
print("Cân bằng:", bot.choose_action(trang_thai))

bot.strategy = aggressive
print("Tấn công:", bot.choose_action(trang_thai))
