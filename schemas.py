from typing import Optional
from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, example=["PC"])
    price: int = Field(gt=0, example=[10000])
    description: Optional[str] = Field(None, example=["美品です"])
