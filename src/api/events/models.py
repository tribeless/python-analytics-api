from typing import List, Optional
import sqlmodel
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # id: int
    page: Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(default_factory=get_utc_now, sa_type=sqlmodel.DateTime(timezone=True), nullable=False)

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="This is my default description")

class EventUpdateSchema(SQLModel):
    description: str