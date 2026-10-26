"""Unit tests for the Expense Tracker core logic."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from expense_tracker import add_expense, filter_expenses, load_expenses, save_expenses, total_expenses


def sample_expenses():
    return [
        {"id": 1, "description": "Lunch", "amount": 45000, "category": "Food"},
        {"id": 2, "description": "Bus", "amount": 12000, "category": "Transport"},
    ]


class ExpenseTrackerTests(unittest.TestCase):
    def test_add_expense_trims_fields_and_assigns_id(self):
        items = sample_expenses()
        added = add_expense(items, " Coffee ", 20000, " Food ")
        self.assertEqual(added["id"], 3)
        self.assertEqual(added["description"], "Coffee")
        self.assertEqual(added["category"], "Food")

    def test_rejects_empty_description(self):
        with self.assertRaisesRegex(ValueError, "description"):
            add_expense([], "  ", 100, "Food")

    def test_rejects_empty_category(self):
        with self.assertRaisesRegex(ValueError, "category"):
            add_expense([], "Snack", 100, " ")

    def test_rejects_non_positive_amount(self):
        for amount in (0, -10):
            with self.subTest(amount=amount), self.assertRaisesRegex(ValueError, "amount"):
                add_expense([], "Snack", amount, "Food")

    def test_total_expenses(self):
        self.assertEqual(total_expenses(sample_expenses()), 57000)

    def test_empty_total_is_zero(self):
        self.assertEqual(total_expenses([]), 0)

    def test_filter_is_case_insensitive(self):
        self.assertEqual([x["description"] for x in filter_expenses(sample_expenses(), "fOoD")], ["Lunch"])

    def test_missing_file_loads_empty_list(self):
        with TemporaryDirectory() as temp:
            self.assertEqual(load_expenses(Path(temp) / "missing.json"), [])

    def test_save_and_load_round_trip(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "expenses.json"
            original = sample_expenses()
            save_expenses(path, original)
            self.assertEqual(load_expenses(path), original)

    def test_invalid_json_raises_clear_error(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "broken.json"
            path.write_text("{broken", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid JSON"):
                load_expenses(path)

    def test_non_list_json_is_rejected(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "object.json"
            path.write_text(json.dumps({"id": 1}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must be a list"):
                load_expenses(path)


if __name__ == "__main__":
    unittest.main()
