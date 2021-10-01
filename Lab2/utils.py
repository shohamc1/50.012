from dotenv import load_dotenv
import os


def create_connection_string():
    load_dotenv()
    type = os.getenv("DATABASE_TYPE")
    url = os.getenv("DATABASE_URL")
    name = os.getenv("DATABASE_NAME")
    username = os.getenv("DATABASE_USERNAME")
    password = os.getenv("DATABASE_PASSWORD")

    return f"{type}://{username}:{password}@{url}/{name}"
