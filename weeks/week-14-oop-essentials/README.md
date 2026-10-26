# Week 14 — Object-Oriented Programming (OOP)

> **Focus:** Classes and objects · Composition · Strategy pattern · Basic inheritance

Week 14 introduces object-oriented design through small, readable examples. The main lesson is to give each object a clear responsibility and prefer **composition** when behavior needs to be interchangeable. Inheritance is used only when the “is-a” relationship is meaningful.

## Learning outcomes

By the end of this week, you should be able to:

- create classes, objects, instance attributes, methods, and `__str__`;
- validate object state and keep related behavior together;
- inject a strategy into a class using composition;
- switch between defensive, balanced, and aggressive strategies without changing `Bot`;
- use basic inheritance for a genuine “is-a” relationship;
- test behavior with goals on both sides of the current position.

## Folder guide

| Resource | What it contains |
|---|---|
| [Notes](notes.md) | Core concepts and design notes |
| [Examples](examples/) | Worked examples |
| [Exercise 1 — Classes](exercises/ex01_classes.py) | Class, object, validation, methods, and string representation |
| [Exercise 2 — Composition](exercises/ex02_composition.py) | A replaceable strategy and movement toward different goals |
| [Exercise 3 — Inheritance](exercises/ex03_inheritance.py) | A simple `Animal` / `Dog` “is-a” relationship |
| [Hints](hints.md) | Implementation guidance |
| [Reference solution](solutions/oop_models.py) | Shared reference implementation |
| [Automated check](checks/check_week.py) | Behavior checks for the week |
| [Mini-project guide](mini-project/README.md) | Strategy Composition requirements |
| [Mini-project code](mini-project/strategy_bot.py) | Runnable implementation |
| [Mini-project tests](mini-project/test_strategy_bot.py) | Five unit tests |

## Exercises

1. **Classes and methods** — implement `Progress`, validate inputs, calculate completion percentage, and provide a readable string representation.
2. **Composition and strategies** — implement `Bot` with a replaceable strategy; make movement work for both `goal=0` and `goal=4`.
3. **Basic inheritance** — implement `Animal` and `Dog`, then demonstrate the inherited “is-a” relationship.

## Mini-project — Strategy Composition

Build a small bot that accepts a strategy in its constructor and runs multiple states with defensive, balanced, and aggressive behavior. The focus is on interchangeable behavior, not on creating a large inheritance hierarchy.

## Run the checks

From the repository root:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Expected result:

```text
Week 14 solution checks: PASS
```

Run the exercises directly:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
```

Run the mini-project demo:

```bash
python weeks/week-14-oop-essentials/mini-project/strategy_bot.py
```

Run its unit tests from the mini-project directory:

```bash
python -m unittest -v
```

## Design principles

- Prefer composition when behavior must be replaceable.
- Keep each class focused on one responsibility.
- Test both normal and boundary cases.
- Avoid inheritance hierarchies that do not clarify the model.

---
**Completion checklist:** all three exercises implemented, mini-project and tests included, and the automated behavior check documented.
