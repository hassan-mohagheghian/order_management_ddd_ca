from abc import ABC, abstractmethod
from uuid import UUID

from order_app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        """Save a user to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        """
        Retrieve a user by their unique ID.

        Raises:
            UserNotFoundError: If no user exists with the given ID
        """

        pass

    @abstractmethod
    def get_by_email(self, user_id: UUID) -> User | None:
        """
        Retrieve a user by their email.

        Raises:
            UserNotFoundError: If no user exists with the given email
        """

        pass
