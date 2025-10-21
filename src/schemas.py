from pydantic import BaseModel
from typing import Union

class MainSchema(BaseModel):
    item_id: int
    q: Union[str, None]
