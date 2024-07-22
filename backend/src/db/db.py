from os import getenv

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

from ..models import models

load_dotenv()
db_schema = getenv("DB_SCHEMA")
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_host = getenv("DB_HOST")
db_port = getenv("DB_PORT")
db_name = getenv("DB_NAME")
db_url = f"{db_schema}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
