from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from api.events import router as event_router
from api.db.session import init_db
from schemas import MainSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    #before app start app
    init_db()
    yield
    #clean up

app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/v1/events')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> MainSchema:
    return MainSchema(item_id=item_id, q=q)

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}