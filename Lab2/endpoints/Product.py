import enum
from typing import List, Optional

from sqlalchemy.orm import Session
from fastapi import Depends

from main import app, get_db
from schema.Product import Product, ProductCreate, ProductDelete
from schema.Error import Message
from crud.Product import create_product, get_products, delete_product


class sort_options(enum.Enum):
    rating_desc = "rating-desc"
    rating_asc = "rating-asc"


@app.post("/product/", response_model=Product, responses={400: {"model": Message}})
def post_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@app.get("/product/", response_model=List[Product])
def read_products(
    db: Session = Depends(get_db),
    sortBy: Optional[sort_options] = None,
    count: Optional[int] = None,
    offset: Optional[int] = None,
):
    products = get_products(db, sortBy, count, offset)
    return products


@app.put("/product/", response_model=Product, responses={400: {"model": Message}})
def del_product(product: ProductDelete, db: Session = Depends(get_db)):
    return delete_product(db, product)
