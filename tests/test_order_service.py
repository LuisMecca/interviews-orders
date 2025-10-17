# tests/test_order_service.py
from src.order_service import process_data, processed_orders_format
import pytest


def test_status_ok_basic():
    data = [{"id": 1, "amount": 100}]
    out = process_data(data)
    assert out[0].status == "ok"


def test_status_error_amount_zero():
    data = [{"id": 2, "amount": 0}]
    out = process_data(data)
    assert out[0].status == "error"


@pytest.mark.parametrize(
        "orders, expected_processed_orders",
        [
         (None, "This could not be formatted"),
         ("Any string", "This could not be formatted"),
         ([], []),
         (
            [
                {"id": 1, "amount": 100, "priority": False},
                {"id": 2, "amount": 50, "priority": True},
                {"id": 3, "amount": 0}
            ],
            [
                {'id': 2, 'priority': True, 'status': 'ok',},
                {'id': 1, 'priority': False, 'status': 'ok',},
                {'id': 3, 'priority': False, 'status': 'error',},
            ]
        )   
        ]
)
def test_orders_path(orders, expected_processed_orders):
    out = process_data(orders)
    actual_processed_orders = processed_orders_format(out)
    assert actual_processed_orders == expected_processed_orders

