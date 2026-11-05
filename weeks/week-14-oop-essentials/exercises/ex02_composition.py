class Bot:
    def __init__(self, strategy="balanced"):
        self.strategy = strategy

    def _move_to_goal(self, state):
        position = state["position"]
        goal = state["goal"]

        if position < goal:
            return "right"
        if position > goal:
            return "left"
        return "wait"

    def _defensive(self, state):
        opponent_position = state.get("opponent_position")

        if opponent_position is not None:
            if abs(state["position"] - opponent_position) <= 1:
                return "wait"

        return self._move_to_goal(state)

    def choose_action(self, state):
        if callable(self.strategy):
            return self.strategy(state)

        if self.strategy == "defensive":
            return self._defensive(state)
        if self.strategy in ("balanced", "aggressive"):
            return self._move_to_goal(state)

        raise ValueError("Unknown strategy")
