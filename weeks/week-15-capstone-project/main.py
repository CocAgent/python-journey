"""Expense Tracker — capstone mẫu dùng thư viện chuẩn Python."""
import json
from pathlib import Path
DATA_FILE = Path(__file__).parent / "data" / "transactions.json"

def validate_transaction(kind, amount, category, note=""):
    if kind not in {"income", "expense"}: raise ValueError("Loại giao dịch phải là income hoặc expense.")
    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0: raise ValueError("Số tiền phải lớn hơn 0.")
    if not isinstance(category, str) or not category.strip(): raise ValueError("Danh mục không được để trống.")
    return {"type": kind, "amount": float(amount), "category": category.strip(), "note": str(note).strip()}

def load_transactions(path=DATA_FILE):
    path=Path(path)
    if not path.exists(): return []
    try: data=json.loads(path.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: raise ValueError(f"Không đọc được JSON: {exc}") from exc
    if not isinstance(data,list): raise ValueError("Dữ liệu phải là danh sách.")
    return [validate_transaction(x.get("type"),x.get("amount"),x.get("category"),x.get("note","")) for x in data if isinstance(x,dict)]

def save_transactions(transactions,path=DATA_FILE):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(transactions,ensure_ascii=False,indent=2),encoding="utf-8")

def add_transaction(transactions,kind,amount,category,note=""):
    item=validate_transaction(kind,amount,category,note); transactions.append(item); return item

def calculate_summary(transactions):
    income=sum(t["amount"] for t in transactions if t["type"]=="income")
    expense=sum(t["amount"] for t in transactions if t["type"]=="expense")
    return {"income":income,"expense":expense,"balance":income-expense}

def filter_by_category(transactions,category):
    keyword=category.strip().casefold()
    return [t for t in transactions if keyword in t["category"].casefold()]

def show_transactions(transactions):
    if not transactions: print("Chưa có giao dịch."); return
    for i,t in enumerate(transactions,1):
        print(f'{i}. {"Thu" if t["type"]=="income" else "Chi"} | {t["category"]} | {t["amount"]:,.0f} VNĐ | {t["note"]}')

def main():
    try: transactions=load_transactions()
    except ValueError as exc: print(f"Lỗi dữ liệu: {exc}"); return
    while True:
        print("\\n=== QUẢN LÝ CHI TIÊU ===\\n1. Thêm khoản thu\\n2. Thêm khoản chi\\n3. Xem giao dịch\\n4. Thống kê\\n5. Lọc danh mục\\n6. Lưu và thoát")
        choice=input("Chọn (1-6): ").strip()
        if choice in {"1","2"}:
            try:
                amount=float(input("Số tiền: ")); category=input("Danh mục: "); note=input("Ghi chú: ")
                add_transaction(transactions,"income" if choice=="1" else "expense",amount,category,note); print("Đã thêm.")
            except ValueError as exc: print(f"Không thể thêm: {exc}")
        elif choice=="3": show_transactions(transactions)
        elif choice=="4":
            s=calculate_summary(transactions); print(f'Tổng thu: {s["income"]:,.0f} VNĐ\\nTổng chi: {s["expense"]:,.0f} VNĐ\\nSố dư: {s["balance"]:,.0f} VNĐ')
        elif choice=="5": show_transactions(filter_by_category(transactions,input("Danh mục: ")))
        elif choice=="6":
            try: save_transactions(transactions); print(f"Đã lưu: {DATA_FILE}")
            except OSError as exc: print(f"Không lưu được: {exc}")
            break
        else: print("Vui lòng chọn từ 1 đến 6.")
if __name__=="__main__": main()
