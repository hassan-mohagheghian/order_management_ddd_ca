from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class OrderViewModel:
    id: str
    user_id: str
    items: list[dict]
    created_at: str
    updated_at: Optional[str]
    total_price: str
