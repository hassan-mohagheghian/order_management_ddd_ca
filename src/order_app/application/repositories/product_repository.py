from abc import ABC, abstractmethod
from uuid import UUID

from order_app.domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> None:
        """Save a product to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, product_id: UUID) -> Product | None:
        """
        Retrieve a product by its ID.

        Raises:
            ProductNotFoundError: If no product exists with the given ID
        """
        pass
