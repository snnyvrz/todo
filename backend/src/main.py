from typing import List
from fastapi import FastAPI
from sqlmodel import Session, select

from .models.models import Item

from .db.db import create_db_and_tables, engine

app = FastAPI()
create_db_and_tables()


@app.get("/items")
async def get_items() -> List[Item]:
    with Session(engine) as session:
        results = session.exec(select(Item)).all()
        return list(results)


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
