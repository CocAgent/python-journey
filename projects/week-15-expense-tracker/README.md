# Week 15 Capstone — Expense Tracker

A beginner-friendly console app for recording and reviewing personal expenses.

## Features
- Add transactions with description, category, positive amount and date.
- List saved transactions.
- Calculate total expenses.
- Filter transactions by category (case-insensitive).
- Save and reload data as UTF-8 JSON.
- Monthly report: total for a selected month, totals by category, and largest transaction.
- Handle invalid menu choices, amounts, missing files and malformed JSON.

## Requirements
- Python 3.12+
- pytest for tests

## Run
From this directory:

```bash
python main.py
```

Data is stored in `data/transactions.json` when you choose **Save and exit**.

## Test
Run from this directory so the source package can be imported:

```bash
python -m pytest -q
```

## Structure
- `main.py`: console input/output and menu.
- `src/expense_tracker.py`: transaction model, calculations, reports, filtering and JSON persistence.
- `tests/test_expense_tracker.py`: normal, edge and invalid-data tests.

## Design decisions
- A dataclass represents each transaction and validates its fields.
- Core functions are separate from console input/output so they can be tested directly.
- JSON is sufficient for a small local app; a database is out of scope.
- A missing data file is treated as a new empty tracker, while malformed JSON is reported instead of silently discarded.
- Month reports use ISO dates (YYYY-MM-DD), and category totals combine capitalization variants.

## Known limitations
- This is a single-user local app; it has no authentication or encryption.
- Amounts use float for beginner-level simplicity; a production finance app should use Decimal.
- Editing/deleting transactions and exporting CSV are out of scope.

## Debugging evidence
The loader deliberately distinguishes a missing file from malformed JSON. The former starts an empty tracker; the latter raises a clear ValueError so the user can repair the data instead of losing it silently.

## AI usage
See `AI_USAGE.md` for the assistance and verification disclosure.
