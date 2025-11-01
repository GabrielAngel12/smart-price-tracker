# api/schemas.py
from pydantic import BaseModel
import datetime
from typing import List, Optional

class PriceHistoryBase(BaseModel):
    price: float

class PriceHistory(PriceHistoryBase):
    id: int
    scraped_at: datetime.datetime

    class Config:
        orm_mode = True # Permite que Pydantic lea datos de modelos de SQLAlchemy

class ProductBase(BaseModel):
    url: str
    name: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    prices: List[PriceHistory] = []

    class Config:
        orm_mode = True