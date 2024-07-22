from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(nullable=False)
    due: datetime = Field(nullable=False)
    modified: datetime = Field(default_factory=datetime.now, nullable=False)
