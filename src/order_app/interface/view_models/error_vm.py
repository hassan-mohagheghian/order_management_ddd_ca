from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ErrorViewModel:
    message: str
    code: Optional[str] = None
