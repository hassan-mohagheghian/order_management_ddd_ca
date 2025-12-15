from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from order_app.domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        """Save an order to the repository."""
        pass

    def delete(self, order_id: UUID) -> None:
        """Delete an order from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Order:
        """
        Retrieve an order by its ID.

        Raises:
            OrderNotFoundError: If no order exists with the given ID
        """
        pass

    @abstractmethod
    def get_list(self, user_id: Optional[UUID] = None) -> list[Order]:
        """Retrieve list of orders optionally filtered by specific user ID."""
        pass
