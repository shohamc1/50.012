from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
    rating: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductDelete(BaseModel):
    id: int
