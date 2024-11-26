from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    age: bool = Field(default=False)
