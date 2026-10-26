# Personal Expense Tracker

A beginner-friendly Python command-line app for recording expenses, reviewing spending, filtering by category, and saving data locally.

## Features

- Add an expense with a description, category, and positive amount.
- List all recorded expenses.
- Calculate total spending.
- Filter expenses by category (case-insensitive).
- Save and load records using UTF-8 JSON.
- Validate user input and report malformed saved data clearly.

## Requirements

- Python 3.10 or newer.
- No third-party runtime dependencies.
- `unittest` is included with Python.

## Setup

Clone or download the repository and open a terminal in this folder. No extra package installation is required.

## Usage

Run the application:

```bash
python main.py
```

Choose option **5** to save the records and exit. Data is stored in `expenses.json` in this folder.

## Run tests

```bash
python -m unittest -v
```

The test suite covers adding expenses, invalid values, totals, category filtering, missing files, JSON persistence, and malformed input files.

## Project structure

- `main.py` — menu and console input/output.
- `expense_tracker.py` — business logic, validation, and JSON persistence.
- `test_expense_tracker.py` — automated unit tests.
- `AI_USAGE.md` — disclosure of AI assistance and verification.

## Design decisions

- A list of dictionaries is sufficient for this small, single-user app.
- Business logic is separate from terminal input/output so it can be tested directly.
- Amounts are stored as integer VND to avoid floating-point rounding for ordinary currency values.
- A missing data file starts an empty tracker; invalid JSON raises a clear error instead of silently discarding data.

## Example

```text
1. Add expense
Description: Lunch
Category: Food
Amount (VND): 45000
Expense added.
```

## Known limitations

- No editing/deleting expenses, monthly reports, user accounts, or encryption.
- The program is intended for local learning, not production financial recordkeeping.

## AI usage

See `AI_USAGE.md`. Review and understand the code before adapting it for coursework.
