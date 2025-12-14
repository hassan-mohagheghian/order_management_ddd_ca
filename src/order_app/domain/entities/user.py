from dataclasses import dataclass, field
import datetime
from typing import Optional
from .entity import Entity


from enum import Enum, auto


class UserRole(Enum):
    MANAGER = auto()
    CUSTOMER = auto()


@dataclass
class User(Entity):
    name: str
    email: str
    role: UserRole = field(default_factory=lambda: UserRole.CUSTOMER)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    updated_at: Optional[datetime.datetime] = None

    def update_role(self, role: UserRole) -> None:
        self.role = role
        self.updated_at = datetime.datetime.now()

    @property
    def is_manager(self) -> bool:
        return self.role == UserRole.MANAGER

    @property
    def is_customer(self) -> bool:
        return self.role == UserRole.CUSTOMER
