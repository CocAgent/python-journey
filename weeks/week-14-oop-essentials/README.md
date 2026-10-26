# Week 14 — Object-Oriented Programming (OOP)

> **Focus:** Classes and objects · Composition · Strategy pattern · Basic inheritance

Week 14 introduces object-oriented design through small, readable examples. The main lesson is to give each object a clear responsibility and prefer **composition** when behavior needs to be interchangeable. Inheritance is used only when the “is-a” relationship is meaningful.

## Learning outcomes

By the end of this week, you should be able to:

- create classes, objects, instance attributes, methods, and __str__;
- validate object state and keep related behavior together;
- inject a strategy into a class using composition;
- switch between defensive, balanced, and aggressive strategies without changing Bot;
- use basic inheritance for a genuine “is-a” relationship;
- test behavior with goals on both sides of the current position.

## Folder guide

| Path | Purpose |
|---|---|
| notes.md | Core concepts and design notes |
| examples/ | Worked examples |
| exercises/ | Three completed exercises |
| hints.md | Hints and implementation guidance |
| solutions/oop_models.py | Shared reference implementation |
| checks/check_week.py | Automated behavior checks |
| mini-project/ | Strategy Composition mini-project |

## Exercises

1. **Classes and methods** — implement Progress, validate inputs, calculate completion percentage, and provide a readable string representation.
2. **Composition and strategies** — implement Bot with a replaceable strategy; make movement work for both goal=0 and goal=4.
3. **Basic inheritance** — implement Animal and Dog, then demonstrate the inherited “is-a” relationship.

## Mini-project — Strategy Composition

Build a small bot that accepts a strategy in its constructor and runs multiple states with defensive, balanced, and aggressive behavior. See mini-project/README.md and mini-project/strategy_bot.py.

## Run the checks

From the repository root:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Expected result:

```text
Week 14 solution checks: PASS
```

Run each exercise directly:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
python weeks/week-14-oop-essentials/mini-project/strategy_bot.py
```

## Design principles

- Prefer composition when behavior must be replaceable.
- Keep each class focused on one responsibility.
- Test both normal and boundary cases.
- Avoid inheritance hierarchies that do not clarify the model.

---
**Completion checklist:** all three exercises implemented, mini-project included, and machine check available.
