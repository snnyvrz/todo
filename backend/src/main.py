from fastapi import FastAPI

from .db.db import create_db_and_tables

app = FastAPI()
create_db_and_tables()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
