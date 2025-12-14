from order_app.domain.entities.order import Order, OrderItem, OrderStatus
from decimal import Decimal
import pytest
from uuid import UUID, uuid4


@pytest.fixture
def order():
    return Order(
        user_id=uuid4(),
    )


def test_order_initial_status(order):
    assert order.status == OrderStatus.CREATED
    assert order.item_count == 0
    assert order.total_price == Decimal("0")


def test_add_order_item(order):
    item = OrderItem(product_id="prod-1", quantity=2, price_per_unit=Decimal("15.00"))
    order.add_item(item)
    assert order.item_count == 1
    assert order.total_price == Decimal("30.00")
    assert order.items[0] == item


def test_remove_order_item(order):
    item1 = OrderItem(product_id="prod-1", quantity=2, price_per_unit=Decimal("15.00"))
    item2 = OrderItem(product_id="prod-2", quantity=1, price_per_unit=Decimal("25.00"))
    order.add_item(item1)
    order.add_item(item2)

    order.remove_item(item1)
    assert order.item_count == 1
    assert order.total_price == Decimal("25.00")
    assert order.items[0] == item2


def test_clear_order_items(order):
    item1 = OrderItem(product_id="prod-1", quantity=2, price_per_unit=Decimal("15.00"))
    item2 = OrderItem(product_id="prod-2", quantity=1, price_per_unit=Decimal("25.00"))
    order.add_item(item1)
    order.add_item(item2)

    order.clear_items()
    assert order.item_count == 0
    assert order.total_price == Decimal("0")


def test_mark_order_as_paid(order):
    item = OrderItem(product_id="prod-1", quantity=2, price_per_unit=Decimal("15.00"))
    order.add_item(item)

    order.mark_as_paid()
    assert order.status == OrderStatus.PAID
    assert order.updated_at is not None


def test_mark_order_as_paid_invalid_status(order):
    item = OrderItem(product_id="prod-1", quantity=2, price_per_unit=Decimal("15.00"))
    order.add_item(item)

    order.mark_as_paid()
    with pytest.raises(
        ValueError, match="Only orders in CREATED status can be marked as PAID"
    ):
        order.mark_as_paid()
