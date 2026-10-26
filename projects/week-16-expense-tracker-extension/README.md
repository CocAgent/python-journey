# Week 16 Extension — Expense Tracker Reports (self-designed)

**Important:** The course repository currently defines a 15-week curriculum. This folder is an optional self-designed continuation, not an official Week 16 assignment.

## Goal
Extend the Week 15 Expense Tracker with reusable reporting logic.

## Planned exercises
1. Implement `monthly_total(transactions, year, month)` to sum expenses for a selected month.
2. Implement `category_totals(transactions)` to return totals grouped by category.
3. Implement `largest_transaction(transactions)`, returning `None` for an empty list.
4. Add tests for empty data, month boundaries, and categories with different capitalization.
5. Add a report option to the console menu and update the main project README.

## Mini-project
Create a monthly report that shows total expenses for a selected month, totals by category, and the largest transaction. Keep reporting logic separate from terminal input/output.

## Acceptance criteria
- Invalid months (not 1–12) are rejected.
- Empty data produces clear output rather than an exception.
- At least 5 new meaningful tests cover normal and edge cases.
- Existing Week 15 tests continue to pass.
- README documents the new feature and a sample report.

## Status
This folder documents the extension brief. Implementation should be added here only after the official course scope is confirmed or the learner chooses this self-designed extension.
