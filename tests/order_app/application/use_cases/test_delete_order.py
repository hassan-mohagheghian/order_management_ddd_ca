from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from order_app.application.use_cases.delete_order import (
    DeleteOrderRequest,
    DeleteOrderUseCase,
)
from order_app.domain.entities.user import UserRole


def test_delete_non_existing_order_raises(order_repository):
    use_case = DeleteOrderUseCase(order_repository=order_repository)
    order_id = uuid4()
    user_id = uuid4()
    order_repository.get_by_id.return_value = None

    request = DeleteOrderRequest(
        order_id=order_id, user_id=user_id, role=UserRole.CUSTOMER
    )

    with pytest.raises(ValueError, match=f"Order with ID {order_id} not found"):
        use_case.execute(request)
    order_repository.get_by_id.assert_called_once_with(order_id)
    order_repository.delete.assert_not_called()


def test_delete_existing_order_with_permission_by_customer(order_repository):
    use_case = DeleteOrderUseCase(order_repository=order_repository)
    order_id = uuid4()
    order_owner_id = uuid4()

    mock_order = MagicMock()
    mock_order.user_id = order_owner_id
    order_repository.get_by_id.return_value = mock_order

    request = DeleteOrderRequest(
        order_id=order_id, user_id=order_owner_id, role=UserRole.CUSTOMER
    )

    use_case.execute(request)

    order_repository.get_by_id.assert_called_once_with(order_id)
    order_repository.delete.assert_called_once_with(order_id)


def test_delete_existing_order_with_permission_by_manager(order_repository):
    use_case = DeleteOrderUseCase(order_repository=order_repository)
    order_id = uuid4()
    order_owner_id = uuid4()
    manager_id = uuid4()

    mock_order = MagicMock()
    mock_order.user_id = order_owner_id
    order_repository.get_by_id.return_value = mock_order

    request = DeleteOrderRequest(
        order_id=order_id, user_id=manager_id, role=UserRole.MANAGER
    )

    use_case.execute(request)

    order_repository.get_by_id.assert_called_once_with(order_id)
    order_repository.delete.assert_called_once_with(order_id)


def test_delete_order_without_permission_raises(order_repository):
    use_case = DeleteOrderUseCase(order_repository=order_repository)
    order_id = uuid4()
    order_owner_id = uuid4()
    other_user_id = uuid4()
    mock_order = MagicMock()
    mock_order.user_id = order_owner_id

    order_repository.get_by_id.return_value = mock_order

    request = DeleteOrderRequest(
        order_id=order_id, user_id=other_user_id, role=UserRole.CUSTOMER
    )

    with pytest.raises(
        ValueError, match="You don't have permission to delete this order"
    ):
        use_case.execute(request)
    order_repository.get_by_id.assert_called_once_with(order_id)
    order_repository.delete.assert_not_called()
