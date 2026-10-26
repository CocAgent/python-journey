# Week 16 Extension — Expense Tracker Reports (self-designed)

**Important:** The repository's official curriculum currently defines 15 weeks. This is a self-designed continuation, not an official Week 16 assignment.

## Implemented extension

The reporting extension is implemented in the Week 15 capstone so it can reuse the same transaction model and JSON data:

- `monthly_total(transactions, year, month)`: sum expenses for a selected month and reject months outside 1–12.
- `category_totals(transactions)`: total spending by category, combining capitalization variants.
- `largest_transaction(transactions)`: return the most expensive record or `None` when empty.
- Console option **5. Báo cáo theo tháng** prints monthly total, category totals, and the largest transaction.

## Exercises / acceptance criteria
1. Read the three reporting functions in `projects/week-15-expense-tracker/src/expense_tracker.py` and explain their return values.
2. Run the full test suite from the project directory: `python -m pytest -q`.
3. Add a test for a month with no expenses.
4. Add a test for an empty category report.
5. Run the app and demonstrate a report for a month that has transactions and one that has none.

## Mini-project
Improve the monthly report with one additional feature of your choice (for example, date-range filtering or CSV export). Keep the logic separate from terminal input/output, add tests, and update the capstone README.

## Verification note
The GitHub connector was used to commit the source and tests, but it does not execute Python in this repository. Run the commands above locally to confirm behavior before submission.
