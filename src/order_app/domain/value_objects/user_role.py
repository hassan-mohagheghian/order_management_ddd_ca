from enum import Enum, auto


class UserRole(Enum):
    MANAGER = auto()
    CUSTOMER = auto()

    @classmethod
    def from_str(cls, role: str):
        return cls[role.upper()]
