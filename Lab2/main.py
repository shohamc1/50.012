from fastapi import FastAPI

from crud import *
from schema import *
from model import *
from database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from endpoints.Product import *
from endpoints.Challenges import *


@app.get("/")
def hello():
    return "Hello"
