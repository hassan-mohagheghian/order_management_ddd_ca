from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from order_app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        """Retrieve a user by their unique ID."""
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        """Create a new user in the repository."""
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        """Update an existing user's information."""
        pass

    @abstractmethod
    def delete_user(self, user_id: UUID) -> None:
        """Delete a user from the repository by their ID."""
        pass
