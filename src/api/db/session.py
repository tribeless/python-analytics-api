import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL # type: ignore

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL needs to be set")

engine = sqlmodel.create_engine(DATABASE_URL) # type: ignore

def init_db():
    print("DB Initialised")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session