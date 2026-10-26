# Week 15 — Python Capstone

> **Focus:** Integration · Testing · Debugging · Documentation · Git/GitHub

Week 15 brings the course together in one small but complete Python project. The goal is not to write the most code; it is to deliver a working, testable program that solves a clear problem and that you can explain.

## Official requirements

The canonical project brief and grading rubric are maintained in FINAL_PROJECT.md. This folder does not introduce a separate rubric.

A successful capstone should include:

- at least **four meaningful business features**;
- functions and modules with clear responsibilities;
- validation and helpful error handling;
- at least **five meaningful tests**, including edge or invalid-input cases;
- a polished README.md with setup, usage, tests, examples, design decisions, and limitations;
- an AI_USAGE.md disclosure when AI assistance was used;
- a reviewable Git history and a reproducible demo.

## Suggested workflow

1. **Define** the problem and list what is out of scope.
2. **Build** a minimal end-to-end workflow before adding extra features.
3. **Test** normal, empty, boundary, and invalid-input cases.
4. **Debug** failures and add regression tests for fixed bugs.
5. **Document** how to install, run, and verify the project.
6. **Commit** changes in small, descriptive commits.

## Repository map

| Path | Purpose |
|---|---|
| FINAL_PROJECT.md | Official brief and rubric |
| notes.md | Integration and handoff checklist |
| hints.md | Hints for completing the capstone |
| checks/ | Mechanical readiness checker |
| submission/ | Example capstone implementation |

## Example capstone — Personal Expense Tracker

The submission folder contains a small console application demonstrating add/list/filter/total features, JSON persistence, validation, and tests. Treat it as a learning reference: run the tests, inspect the implementation, and be ready to explain the design decisions before adapting it for your own submission.

## Run the example

From the repository root:

```bash
python weeks/week-15-capstone-project/submission/main.py
```

## Run tests

From the submission directory:

```bash
python -m unittest -v
```

## Readiness check

To inspect your own capstone folder, run:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py path/to/my-project
```

The checker reports structural evidence; it does not replace the official rubric or a human review.

## Before handoff

- [ ] Four or more meaningful features work.
- [ ] At least five meaningful tests pass.
- [ ] Invalid input and common file errors are handled.
- [ ] README setup, usage, tests, examples, and limitations are accurate.
- [ ] AI_USAGE.md honestly describes assistance and verification.
- [ ] I can explain the important functions and design decisions.

---
**Deliverable:** a working Python project, tests, documentation, and a demo that can be reproduced by another person.
