from abc import ABC, abstractmethod
from domain.entities.product import Product
from uuid import UUID


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> None:
        """Save a product to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, product_id: UUID):
        """Retrieve a product by its ID."""
        pass

    @abstractmethod
    def get_by_user(self, user_id: UUID) -> list[Product]:
        """Retrieve all products for a specific user."""
        pass
