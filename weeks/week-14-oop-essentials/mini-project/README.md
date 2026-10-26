# Mini-project — Strategy Composition

Build a small bot whose movement strategy can be replaced without modifying the Bot class. This project applies the Week 14 lesson: prefer composition when behavior needs to vary independently.

## Requirements

- Implement a `Bot` class that receives a strategy in `__init__`.
- Implement `choose_action(state)` to delegate to the selected strategy.
- Provide `defensive`, `balanced`, and `aggressive` strategies.
- Handle goals on either side of the current position, including `goal=0` and `goal=4`.
- Demonstrate all strategies against multiple states.
- Keep the implementation small; inheritance is not required.

## Files

- `strategy_bot.py` — runnable mini-project and demo.
- `test_strategy_bot.py` — five unit tests covering movement, goal boundaries, defensive behavior, and strategy injection.

## Run the demo

From the repository root:

```bash
python weeks/week-14-oop-essentials/mini-project/strategy_bot.py
```

## Run the tests

Change into the mini-project directory, then run:

```bash
python -m unittest -v
```

## Design note

All three strategies share the same direct movement rule in this course-local example, while the defensive strategy adds a simple adjacent-opponent check. The focus is the replaceable strategy interface, not realistic game AI. Extend the behavior only if you can describe and test the new rule.
