# src/order_service.py
from dataclasses import dataclass, asdict
from typing import List, Optional, Union

OrderDict = dict[str, int|bool]

@dataclass
class ProcessedOrder:
    id: int
    status: str
    priority: Optional[bool] = False


def handle_orders(
    orders: List[OrderDict],
) -> Union[List[ProcessedOrder], str]:
    if type(orders) != list:
        return "This is not an orders list"
    
    processed_orders: List[ProcessedOrder] = []
    for order in orders:  # type: ignore[assignment]
        if order.get("amount", -1) <= 0:
            processed_orders.append(ProcessedOrder(id=order.get("id"), status="error"))
            continue
        processed_orders.append(ProcessedOrder(id=order["id"], status="ok", priority=order.get("priority", False)))

    processed_orders = sorted(processed_orders, key=lambda order: order.priority, reverse=True)
    return processed_orders


def process_data(items):
    return handle_orders(items)


def processed_orders_format(orders: List[ProcessedOrder]) -> dict[str, str|bool]:
    return [asdict(order) for order in orders] if type(orders) == list else "This could not be formatted"