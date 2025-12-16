from abc import ABC
from dataclasses import dataclass
from typing import Optional

from order_app.interface.common.operation_result import ErrorViewModel
from order_app.interface.view_models.order_vm import OrderViewModel


@dataclass
class OrderPresenter(ABC):
    def present_order(self, response: CreateOrderResponse) -> OrderViewModel:
        pass

    def present_error(
        self, error_msg: str, code: Optional[str] = None
    ) -> ErrorViewModel:
        pass
