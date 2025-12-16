from dataclasses import dataclass

from order_app.application.dtos.order_dtos import ItemRequest
from order_app.application.use_cases.create_order import (
    CreateOrderRequest,
    CreateOrderUseCase,
)
from order_app.interface.common.operation_result import OperationResult
from order_app.interface.presenters.base import OrderPresenter
from order_app.interface.view_models.order_vm import OrderViewModel


@dataclass
class ItemRequestData:
    product_id: str
    quantity: int


@dataclass
class CreateOrderRequestData:
    user_id: str
    items: list[ItemRequestData]


@dataclass
class CreateOrderResponseData:
    order_id: str


@dataclass
class OrderController:
    create_order_use_case: CreateOrderUseCase
    presenter: OrderPresenter

    def handle_create(
        self, request_data: CreateOrderRequestData
    ) -> OperationResult[OrderViewModel]:
        request = CreateOrderRequest(
            user_id=request_data.user_id,
            items=[
                ItemRequest(product_id=item.product_id, quantity=item.quantity)
                for item in request_data.items
            ],
        )
        response = self.create_order_use_case.execute(request)
        if response.is_success:
            view_model = self.presenter.present_order(response.value)
            return OperationResult.succeed(view_model)
        else:
            error_vm = self.presenter.present_error(
                response.error.message, response.error.code
            )
            return OperationResult.fail(error_vm.message, error_vm.code)
