from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse

from model.Product import Product
from schema.Product import ProductCreate, ProductDelete


def create_product(db: Session, product: ProductCreate):
    new_product = Product(name=product.name, price=product.price, rating=product.rating)
    db.add(new_product)

    try:
        db.commit()
    except IntegrityError:
        return JSONResponse(
            status_code=400, content={"message": "Column constraints failed."}
        )

    db.refresh(new_product)

    return new_product


get_value = lambda col: col.value if col else None


def get_products(db: Session, sortBy, count, offset):
    map = {
        "rating-desc": Product.rating.desc(),
        "rating-asc": Product.rating.asc(),
        None: None,
    }

    return (
        db.query(Product)
        .order_by(map[get_value(sortBy)])
        .limit(count)
        .offset(offset)
        .all()
    )


def delete_product(db: Session, productDelete: ProductDelete):
    product = db.query(Product).filter(Product.id == productDelete.id).first()

    if product == None:
        return JSONResponse(
            status_code=400, content={"message": "ID did not return any products."}
        )

    db.delete(product)
    db.commit()

    return product
