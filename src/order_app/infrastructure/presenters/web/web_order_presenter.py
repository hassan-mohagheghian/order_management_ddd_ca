from dataclasses import dataclass

from order_app.application.use_cases.create_order import CreateOrderResponse
from order_app.interface.presenters.base import OrderPresenter
from order_app.interface.view_models.base import ErrorViewModel
from order_app.interface.view_models.order_vm import OrderViewModel


@dataclass
class WebOrderPresenter(OrderPresenter):
    def present_order(self, response: CreateOrderResponse) -> OrderViewModel:
        return OrderViewModel(
            id=response.order_id,
            items=response.items,
            created_at=response.created_at,
            updated_at=response.updated_at,
            total_price=response.total_price,
        )

    def present_error(self, error_msg, code=None) -> ErrorViewModel:
        return ErrorViewModel(message=error_msg, code=code)
