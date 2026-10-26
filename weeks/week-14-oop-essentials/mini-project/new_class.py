""" AI BOT """


class DefensiveStrategy:
    def choose_action(self, state):
        position = state["position"]
        opponent = state["opponent_position"]
        goal = state["goal"]

        if abs(position - opponent) <= 1:
            return "defend"

        if position < goal:
            return "move_right"
        elif position > goal:
            return "move_left"
        else:
            return "wait"


class BalancedStrategy:
    def choose_action(self, state):
        position = state["position"]
        opponent = state["opponent_position"]
        goal = state["goal"]

        if abs(position - opponent) <= 1:
            return "attack"

        if position < goal:
            return "move_right"
        elif position > goal:
            return "move_left"
        else:
            return "wait"


class AggressiveStrategy:
    def choose_action(self, state):
        position = state["position"]
        opponent = state["opponent_position"]

        if abs(position - opponent) <= 1:
            return "attack"

        if position < opponent:
            return "move_right"
        elif position > opponent:
            return "move_left"
        else:
            return "wait"


class Bot:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.hp = 100

    def choose_action(self, state):
        return self.strategy.choose_action(state)

    def show_info(self):
        print("Bot:", self.name)
        print("HP:", self.hp)
        print("Strategy:", self.strategy.__class__.__name__)

    def take_damage(self, amount):
        if amount <= 0:
            print("Damage must be positive!")
            return

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

        print(self.name, "received", amount, "damage.")
        print("HP remaining:", self.hp)


def main():
    bot1 = Bot("Defensive Bot", DefensiveStrategy())
    bot2 = Bot("Balanced Bot", BalancedStrategy())
    bot3 = Bot("Aggressive Bot", AggressiveStrategy())

    state = {
        "position": 1,
        "opponent_position": 4,
        "goal": 4
    }

    bots = [bot1, bot2, bot3]

    print("=== AI BOT SIMULATION ===")
    print("Game state:", state)
    print()

    for bot in bots:
        bot.show_info()

        action = bot.choose_action(state)
        print("Action:", action)
        print("-" * 30)

    print("\n=== DAMAGE TEST ===")
    bot1.take_damage(30)


if __name__ == "__main__":
    main()
