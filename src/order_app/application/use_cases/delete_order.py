from dataclasses import dataclass
from uuid import UUID

from order_app.domain.entities.user import UserRole
from order_app.domain.repositories import OrderRepository


@dataclass
class DeleteOrderRequest:
    order_id: UUID
    user_id: UUID
    role: UserRole


@dataclass
class DeleteOrderUseCase:
    order_repository: OrderRepository

    def execute(self, request: DeleteOrderRequest) -> None:
        order = self.order_repository.get_by_id(request.order_id)
        if not order:
            raise ValueError(f"Order with ID {request.order_id} not found")

        if request.role != UserRole.MANAGER and order.user_id != request.user_id:
            raise ValueError("You don't have permission to delete this order")

        self.order_repository.delete(request.order_id)
