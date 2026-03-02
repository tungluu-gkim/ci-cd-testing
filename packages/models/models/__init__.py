"""Models package."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class BaseModel:
    id: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class User(BaseModel):
    name: str = ""
    email: str = ""
