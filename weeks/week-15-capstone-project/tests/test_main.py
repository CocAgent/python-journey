import tempfile
import unittest
from pathlib import Path
from main import add_transaction, calculate_summary, filter_by_category, load_transactions, save_transactions, validate_transaction

class ExpenseTrackerTests(unittest.TestCase):
    def test_add_transaction(self):
        items=[]; add_transaction(items,"income",1000,"Lương")
        self.assertEqual(len(items),1); self.assertEqual(items[0]["amount"],1000.0)
    def test_reject_invalid_amount(self):
        for amount in (0,-1):
            with self.assertRaises(ValueError): validate_transaction("expense",amount,"Ăn uống")
    def test_reject_invalid_type_or_category(self):
        with self.assertRaises(ValueError): validate_transaction("transfer",10,"Khác")
        with self.assertRaises(ValueError): validate_transaction("expense",10," ")
    def test_summary(self):
        items=[validate_transaction("income",1000,"Lương"),validate_transaction("expense",250,"Ăn uống")]
        self.assertEqual(calculate_summary(items),{"income":1000.0,"expense":250.0,"balance":750.0})
    def test_filter_case_insensitive(self):
        items=[validate_transaction("expense",20,"Ăn uống"),validate_transaction("expense",30,"Đi lại")]
        self.assertEqual(len(filter_by_category(items,"ĂN")),1)
    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"data"/"transactions.json"
            save_transactions([validate_transaction("income",99,"Lương")],path)
            self.assertEqual(load_transactions(path)[0]["amount"],99.0)
    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder: self.assertEqual(load_transactions(Path(folder)/"missing.json"),[])
if __name__=="__main__": unittest.main()
