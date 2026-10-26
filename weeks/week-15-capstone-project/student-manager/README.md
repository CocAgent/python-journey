# Student Manager — Week 15 Capstone

## Problem and scope

A terminal app to manage students and scores. Out of scope: GUI, network,
database server, editing/deleting records, multiple concurrent users.

## Features

1. Add a student with validated ID/name/scores.
2. List students with averages and grades.
3. Find students by ID.
4. Save and load JSON records.
5. Reject duplicates and invalid data.

## Setup

Requires Python 3.12+. From this folder:

```powershell
python -m pip install pytest
```

## Usage

```powershell
python main.py
```

Example:

```text
1 Add  2 List  3 Find  4 Save  5 Exit
Choose: 1
ID: S01
Name: Son
Scores, comma-separated: 8,9,7
Added.
Choose: 2
S01 | Son | 8.00 | Excellent
```

Choose 4 to save to `data/students.json`, then 5 to exit.

## Test

```powershell
python -m pytest tests -v
python ../checks/check_capstone_readiness.py .
```

## Structure and design

- `main.py`: terminal I/O and menu.
- `student_manager.py`: calculations, validation and JSON storage.
- `tests/test_student_manager.py`: 10 automated tests.
- `AI_USAGE.md`: disclosure of assistance.

A list of dictionaries fits small records and serializes directly to JSON.
Validation at the storage boundary rejects damaged data.

## Evidence and debugging

Run the commands above locally to obtain test results. Regression case:
an incomplete student JSON record must raise ValueError, not KeyError.
Mechanical readiness is not a final academic grade.

## Known limitations

Save is manual. No edit/delete function, no GUI, no multi-user support.
