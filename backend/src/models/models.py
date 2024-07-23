from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ItemBase(SQLModel):
    title: str = Field(nullable=False)
    done: bool = Field(default=False, nullable=False)
    due: datetime = Field(nullable=False)


class Item(ItemBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    modified: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)
