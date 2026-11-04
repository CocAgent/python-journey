# Repository test suite

The `tests/` directory contains **maintainer-owned, automated checks** for the
Python Journey codebase. Its purpose is to detect regressions, verify the
integrity of teaching materials and reference implementations, and provide
repeatable quality evidence for proposed changes.

It is **not** the submission directory, a substitute for classroom assessment,
or a security boundary for running untrusted programs.

## Scope and ownership

| Layer | Typical location | Responsibility |
|---|---|---|
| Cross-cutting checks | `tests/test_course_structure.py`, `tests/test_week_owned_checks.py` | Validate repository structure, paths, and integration contracts |
| Learning-material examples | `tests/test_week*_guided_practice.py`, other `tests/test_week*.py` | Check that published examples, references and navigation work as documented |
| Shared helpers | `tests/assessment_reference.py`, with corresponding tests | Test helper behavior against controlled fixtures; do not assume production safety |
| Week-local checks | `weeks/<week>/checks/` and week-local test directories | Own the learning outcomes and acceptance checks of that particular week |
| Optional self-study exercises | `review/`, `weeks/<week>/practice/` | Check a student's own work only when explicitly invoked in learner mode |

The root test suite may **invoke** a week-local checker as an integration
gate. The underlying exercise contracts, expected outputs and reference
solutions should remain with the owning week or exercise. Avoid duplicating
an entire grading specification in multiple locations.

## Run checks

Execute commands from the **repository root**, using the supported Python
version and the project configuration.

```bash
# Run the repository's default pytest selection
python -m pytest

# Run only maintainer tests
python -m pytest tests -q

# Diagnose one focused check
python -m pytest tests/test_course_structure.py -q

# Validate other course invariants where available
python scripts/verify_course.py

# Static checks used by the project
ruff check scripts tests projects/vuacoc-bot-journey
```

Consult `pyproject.toml` and `.github/workflows/` for the current authoritative
test selection, supported interpreters and CI gate. Local `PASS` results should
be distinguished from a confirmed CI result.

## What a successful test run means

- A **maintainer reference PASS** indicates that the checked reference
  material met the automated assertions in that run.
- A student starter containing intentional `TODO` or
  `NotImplementedError` may be **expected to FAIL** before the learner
  completes it. Root CI should not require unfinished student work to PASS.
- A **learner PASS** applies only when the checker was run against the learner's
  actual implementation, with the relevant inputs and constraints.
- No finite automated test suite proves complete correctness, security,
  academic authorship or achievement of all learning outcomes.

Never report a reference PASS as proof of learner completion. Test output
should make the selected mode and the code under test unambiguous.

## Test design guidelines

1. **Deterministic:** fixed inputs and explicit expected behavior. Avoid
   network access, wall-clock assumptions, uncontrolled randomness and
   reliance on unordered collection display.
2. **Isolated:** use temporary directories and fixture data; do not modify
   real submissions, secrets, user files or production infrastructure.
3. **Observable:** verify return values, types, state changes, expected
   exceptions and process status—not just the presence of a printed phrase.
4. **Representative:** cover ordinary inputs, boundaries, empty/missing
   values, invalid data and regressions when applicable.
5. **Focused:** keep each test small, readable and attributable to a
   concrete documented requirement; add regression coverage when fixing bugs.
6. **Versioned:** keep tests, examples and their contractual documentation
   in the same change; do not silently relax a failing assertion.
7. **Respect ownership:** place exercise-specific tests near the exercise,
   and reserve root `tests/` for shared and integration gates.
8. **Safe by design:** subprocess timeouts can prevent common hangs, but
   **do not sandbox arbitrary code**. Use proper container/VM isolation,
   resource limits, minimal permissions and network restrictions for
   submissions from untrusted sources.

## Contributing a new check

Identify a requirement or regression and the directory that owns it.
Write a minimal reproducible case, including expected behavior and invalid
inputs where relevant. Run the focused test and local quality checks.
Include documentation updates when commands, file paths, modes or learning
contracts change. Confirm the required CI jobs before merging.

For work involving assessment design, automated scoring, or migration of
historical exam materials, consult [the assessment review](LEGACY_ASSESSMENT_REVIEW.md)
as **background evidence**, not as a repository-wide scoring policy. The
`review/` directory may offer public practice exams with their own duration,
rubric and self-check scripts; those exercise-specific values should not be
embedded as defaults for the entire test suite.

This README documents **testing responsibilities and conventions**, not
deployment approval, an official examination policy, or a claim that the
repository safely executes untrusted code.
