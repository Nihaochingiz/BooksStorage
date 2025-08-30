from pydantic import BaseModel, ConfigDict
from typing import Optional

class BookAdd(BaseModel):
    name: str
    author: str
    read_year: Optional[int] = None  # ← БЕЗ id здесь!

class BookResponse(BookAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookId(BaseModel):
    id: int