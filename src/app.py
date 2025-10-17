# src/app.py
import json
from pathlib import Path
from .order_service import process_data, processed_orders_format

def main():
    sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_orders.json"
    if sample_path.exists():
        items = json.loads(sample_path.read_text())
    else:
        items = [{"id": 1, "amount": 100, "priority": False},
                 {"id": 2, "amount": 50, "priority": True},
                 {"id": 3, "amount": 0}]

    result = process_data(items)
    print(json.dumps(processed_orders_format(result), indent=2))

if __name__ == "__main__":
    main()
