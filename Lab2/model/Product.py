from sqlalchemy import Column, Integer, String, Float

from database import Base, engine


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), unique=True)
    price = Column(Integer)
    rating = Column(Float)


Base.metadata.create_all(engine)
